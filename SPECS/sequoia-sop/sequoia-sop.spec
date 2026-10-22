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

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros

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
