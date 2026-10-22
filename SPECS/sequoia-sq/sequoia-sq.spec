# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-sq
Version:        1.5.0
Release:        %autorelease
Summary:        Command-line tools for OpenPGP
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-sq
#!RemoteAsset:  sha256:43f230abc78a8daec8a06cfc8c1191045b7b210fee5bee50dc3f75bd9f22950e
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros
# Additional dependencies required by OBS builds.
BuildRequires:  rust

Recommends:     gnupg
Recommends:     sequoia-keystore-server

%description
Command-line frontends for Sequoia.

%build -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"

%check -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sq %{buildroot}%{_bindir}/sq
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/sq.bash %{buildroot}%{bash_completions_dir}/sq
install -Dm0644 assets/shell-completions/_sq %{buildroot}%{_datadir}/zsh/site-functions/_sq
install -Dm0644 assets/shell-completions/sq.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sq.fish

%files
%doc README.md NEWS
%license LICENSE.txt
%{_bindir}/sq
%{_mandir}/man1/*
%{bash_completions_dir}/sq
%{_datadir}/zsh/site-functions/_sq
%{_datadir}/fish/vendor_completions.d/sq.fish

%changelog
%autochangelog
