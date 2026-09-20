# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name typescript-go
%define go_import_path github.com/microsoft/typescript-go
%ifarch x86_64
%global node_arch x64
%else
%global node_arch %{_arch}
%endif

Name:           typescript
Version:        7.0.2
Release:        %autorelease
Summary:        TypeScript language compiler
License:        Apache-2.0
URL:            https://www.typescriptlang.org/
VCS:            git:https://github.com/microsoft/TypeScript.git
#!RemoteAsset:  sha256:25cca8ec9d89e4ceec5181a677ded2c6d690fa18b81e1277846303973eb71fcf
Source0:        https://github.com/microsoft/typescript-go/archive/refs/tags/typescript/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:da2513f4b95176d6dde8b51aab7afe8a927656c9d277369793f77f7e59371c08
Source1:        https://registry.npmjs.org/typescript/-/typescript-%{version}.tgz
BuildSystem:    golang

BuildOption(prep):  -n typescript-go-typescript-v%{version}

BuildRequires:  go >= 1.26
BuildRequires:  go-rpm-macros
BuildRequires:  nodejs >= 16.20
BuildRequires:  go(github.com/go-json-experiment/json)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mackerelio/go-osstat)
BuildRequires:  go(github.com/peter-evans/patience)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       npm(typescript) = %{version}

Requires:       nodejs >= 16.20

%description
TypeScript is a language for application-scale JavaScript development. This
package provides its native compiler and the matching npm API and CLI wrapper.

%prep -a
tar -xf %{SOURCE1}

%build
%go_common
install -d %{_builddir}/go/src/github.com/microsoft
ln -snf "$(pwd)" %{_builddir}/go/src/%{go_import_path}
go build -trimpath -buildvcs=false -o tsc ./cmd/tsgo

%install
install -Dpm 0755 tsc %{buildroot}%{_libexecdir}/typescript/tsc
install -d %{buildroot}%{_prefix}/lib/node_modules/typescript
cp -a package/bin package/lib package/dist package/vendor package/package.json \
    %{buildroot}%{_prefix}/lib/node_modules/typescript/

# The npm launcher resolves the native executable through this platform package.
platform_dir=%{buildroot}%{_prefix}/lib/node_modules/@typescript/typescript-linux-%{node_arch}
install -d "${platform_dir}/lib"
cat > "${platform_dir}/package.json" <<EOF
{"name":"@typescript/typescript-linux-%{node_arch}","version":"%{version}"}
EOF
ln -s %{_libexecdir}/typescript/tsc "${platform_dir}/lib/tsc"
install -d %{buildroot}%{_bindir}
ln -s ../lib/node_modules/typescript/bin/tsc %{buildroot}%{_bindir}/tsc

%check
%go_common
go test -v ./internal/core ./internal/scanner ./internal/tspath ./internal/bundled
./tsc --version | grep -Fx 'Version %{version}'
node -e 'const ts = require("./package/lib/version.cjs"); if (ts.version !== "%{version}") process.exit(1)'

%files
%doc README.md
%license LICENSE NOTICE.txt
%{_bindir}/tsc
%{_libexecdir}/typescript/
%dir %{_prefix}/lib/node_modules
%{_prefix}/lib/node_modules/typescript/
%dir %{_prefix}/lib/node_modules/@typescript
%{_prefix}/lib/node_modules/@typescript/typescript-linux-%{node_arch}/

%changelog
%autochangelog
