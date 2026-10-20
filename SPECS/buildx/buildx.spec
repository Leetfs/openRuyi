# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           buildx
%define go_import_path  github.com/docker/buildx
%define buildx_commit   0dbe87f36ed472fe36b6796c3f70b4210a731fc5

Name:           buildx
Version:        0.38.0
Release:        %autorelease
Summary:        Docker CLI plugin for extended build capabilities with BuildKit
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            https://github.com/docker/buildx
#!RemoteAsset:  sha256:f4705415fe4e011f19c6fe0fa324fef81236791815c51bb6210b3bbbca5b1319
Source0:        https://github.com/docker/buildx/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    golang

# Avoid fetching remote repositories in the Git URL-selection tests.
Patch2000:      2000-use-local-git-tracking-refs-in-tests.patch
# The bundled IDNA lookup rejects the invalid UTF-8 normalization fixture.
Patch2001:      2001-test-invalid-utf8-host-rejection.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.26.8
BuildRequires:  go-rpm-macros
BuildRequires:  go-md2man
BuildRequires:  git

Requires:       docker-cli

%description
Buildx extends the Docker command line with BuildKit capabilities, including
multi-platform builds, multiple builder instances, build caching, and Bake
definitions. It can run as a Docker CLI plugin or as the buildx command.

%build
# The main package is in cmd/buildx, and upstream supplies module-mode vendor data.
export GO111MODULE=on
export GOTOOLCHAIN=local
export GOPROXY=off
export CGO_ENABLED=1
# The distribution's debugedit does not support Go's DWARF 5 output.
export GOEXPERIMENT=nodwarf5
%{__go} build -mod=vendor -buildmode=pie -trimpath \
    -ldflags "-X %{go_import_path}/version.Version=v%{version} -X %{go_import_path}/version.Revision=%{buildx_commit}" \
    -o buildx ./cmd/buildx
mkdir -p man completions vendor-licenses
# Convert upstream Markdown references to section 1 man pages with Docker command names.
for page in docs/reference/*.md; do
    name=$(basename "$page" .md | tr '_' '-')
    { printf '# docker-%%s 1\n' "$name"; tail -n +2 "$page"; } | \
        go-md2man > "man/docker-$name.1"
done
./buildx completion bash > completions/bash
./buildx completion zsh > completions/zsh
./buildx completion fish > completions/fish
# Preserve the directory hierarchy of bundled third-party license notices.
find vendor -type f \( -iname 'license*' -o -iname 'copying*' -o -iname 'notice*' \) \
    -exec cp --parents '{}' vendor-licenses/ \;

%install -a
# Expose the standalone command through Docker's plugin search path.
install -d %{buildroot}%{_libexecdir}/docker/cli-plugins
ln -s %{_bindir}/buildx %{buildroot}%{_libexecdir}/docker/cli-plugins/docker-buildx
install -d %{buildroot}%{_mandir}/man1
install -m 0644 man/*.1 %{buildroot}%{_mandir}/man1/
ln -s docker-buildx.1 %{buildroot}%{_mandir}/man1/buildx.1
install -D -m 0644 completions/bash %{buildroot}%{bash_completions_dir}/buildx
install -D -m 0644 completions/zsh %{buildroot}%{zsh_completions_dir}/_buildx
install -D -m 0644 completions/fish %{buildroot}%{fish_completions_dir}/buildx.fish

%check
# The default check's GOPATH mode uses Go 1.20 GODEBUG defaults, causing
# the IPv6 URL parsing tests to fail. Module mode honors go.mod's defaults.
export GO111MODULE=on
export GOTOOLCHAIN=local
export GOPROXY=off
# Upstream's unit-test target skips integrations needing Docker and BuildKit daemons.
export SKIP_INTEGRATION_TESTS=1
%{__go} test -mod=vendor -v ./...

%files
%doc README.md docs
%license LICENSE vendor-licenses
%{_bindir}/buildx
%{_libexecdir}/docker/cli-plugins/docker-buildx
%{_mandir}/man1/buildx.1*
%{_mandir}/man1/docker-buildx*.1*
%{bash_completions_dir}/buildx
%{zsh_completions_dir}/_buildx
%{fish_completions_dir}/buildx.fish

%changelog
%autochangelog
