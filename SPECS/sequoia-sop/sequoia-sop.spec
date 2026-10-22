# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-sop
Version:        0.38.0
Release:        %autorelease
Summary:        Stateless OpenPGP command-line interface
License:        GPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-sop
#!RemoteAsset:  sha256:a44fb99ec7ca8204ec6617944ae0ae6fe5cd954cb30c85e155b7cfb368b46d81
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildOption(build):  --features cli,cliv

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(sequoia-openpgp-2) >= 2.4.0
BuildRequires:  crate(sequoia-wot-0.15) >= 0.15.0
BuildRequires:  crate(sop-0.8) >= 0.8.1
BuildRequires:  crate(sop-0.8/default) >= 0.8.1
# Additional dependencies required by OBS builds.
BuildRequires:  crate(sequoia-policy-config-0.8) >= 0.8.2
BuildRequires:  crate(aes-0.8) >= 0.8.4
BuildRequires:  crate(aes-gcm-0.10) >= 0.10.3
BuildRequires:  crate(block-padding-0.3) >= 0.3.3
BuildRequires:  crate(blowfish-0.9) >= 0.9.1
BuildRequires:  crate(botan-0.10) >= 0.10.7
BuildRequires:  crate(camellia-0.1) >= 0.1.0
BuildRequires:  crate(cast5-0.11) >= 0.11.1

%description
An implementation of the Stateless OpenPGP Interface using Sequoia.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%check -p
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release --features cli,cliv"

%install
install -Dm0755 target/release/sqop %{buildroot}%{_bindir}/sqop
install -Dm0755 target/release/sqopv %{buildroot}%{_bindir}/sqopv
install -d %{buildroot}%{_mandir}/man1
install -m0644 assets/man-pages/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 assets/shell-completions/sqop.bash %{buildroot}%{bash_completions_dir}/sqop
install -Dm0644 assets/shell-completions/_sqop %{buildroot}%{_datadir}/zsh/site-functions/_sqop
install -Dm0644 assets/shell-completions/sqop.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sqop.fish
install -Dm0644 assets/shell-completions/sqopv.bash %{buildroot}%{bash_completions_dir}/sqopv
install -Dm0644 assets/shell-completions/_sqopv %{buildroot}%{_datadir}/zsh/site-functions/_sqopv
install -Dm0644 assets/shell-completions/sqopv.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sqopv.fish

%files
%doc README.md NEWS openpgp-policy.toml
%license LICENSE.txt
%{_bindir}/sqop
%{_bindir}/sqopv
%{_mandir}/man1/*
%{bash_completions_dir}/sqop
%{_datadir}/zsh/site-functions/_sqop
%{_datadir}/fish/vendor_completions.d/sqop.fish
%{bash_completions_dir}/sqopv
%{_datadir}/zsh/site-functions/_sqopv
%{_datadir}/fish/vendor_completions.d/sqopv.fish

%changelog
%autochangelog
