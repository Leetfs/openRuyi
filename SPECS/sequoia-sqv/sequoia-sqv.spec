# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-sqv
Version:        1.5.0
Release:        %autorelease
Summary:        Simple OpenPGP signature verification
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-sqv
#!RemoteAsset:  sha256:d4eb1f22746894dd654a8fa50576200d047f0de0e1ae2a361d7ebe263d351bc8
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros
# Additional dependencies required by OBS builds.
BuildRequires:  rust
BuildRequires:  crate(anyhow-1/default) >= 1.0.18

%description
A simple OpenPGP signature verification program.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%check -p
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sqv %{buildroot}%{_bindir}/sqv
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/sqv.bash %{buildroot}%{bash_completions_dir}/sqv
install -Dm0644 assets/shell-completions/_sqv %{buildroot}%{_datadir}/zsh/site-functions/_sqv
install -Dm0644 assets/shell-completions/sqv.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sqv.fish

%files
%doc README.md NEWS openpgp-policy.toml
%license LICENSE.txt
%{_bindir}/sqv
%{_mandir}/man1/*
%{bash_completions_dir}/sqv
%{_datadir}/zsh/site-functions/_sqv
%{_datadir}/fish/vendor_completions.d/sqv.fish

%changelog
%autochangelog
