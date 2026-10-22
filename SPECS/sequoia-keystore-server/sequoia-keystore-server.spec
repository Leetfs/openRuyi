# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-keystore-server
Version:        0.2.1
Release:        %autorelease
Summary:        Sequoia OpenPGP keystore daemon
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-keystore
#!RemoteAsset:  sha256:d6f0a28a24b299d3c620014ab7b24cf814f08b25310bd4de04271d1dca5aaedc
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros
# Additional dependencies required by OBS builds.
BuildRequires:  rust
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(clap-4/default) >= 4.0.0

Recommends:     gnupg

%description
Sequoia keystore daemon.

%build -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"

%build -a
help2man --no-info --version-string=%{version} --name='Sequoia OpenPGP keystore daemon' --output=sequoia-keystore.1 target/release/sequoia-keystore

%check -p
export PREFIX=%{_prefix}
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"

%install
install -Dm0755 target/release/sequoia-keystore %{buildroot}%{_libexecdir}/sequoia/sequoia-keystore
install -Dm0644 sequoia-keystore.1 %{buildroot}%{_mandir}/man1/sequoia-keystore.1

%files
%doc README.md
%license LICENSE.txt
%{_libexecdir}/sequoia/
%{_mandir}/man1/sequoia-keystore.1*

%changelog
%autochangelog
