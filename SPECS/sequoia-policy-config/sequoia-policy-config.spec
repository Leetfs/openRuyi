# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sequoia-policy-config
Version:        0.8.2
Release:        %autorelease
Summary:        Check Sequoia OpenPGP cryptographic policy configuration
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-policy-config
#!RemoteAsset:  sha256:54ecc2eeefc0ccbba225e6e57ef1cde9df78e55b315e71fd95ebebc5bd1dbbb6
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
Source1:        sequoia-policy-config-check.1
BuildSystem:    rust

BuildOption(build):  --features sequoia-openpgp/crypto-nettle

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros
# Additional dependencies required by OBS builds.
BuildRequires:  rust
BuildRequires:  crate(anyhow-1/default) >= 1.0.18
BuildRequires:  crate(chrono-0.4/default) >= 0.4.0
BuildRequires:  crate(sequoia-openpgp-2) >= 2.4.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(toml-0.8/default) >= 0.8.23

%description
Configure Sequoia using a configuration file.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%check -p
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release --features sequoia-openpgp/crypto-nettle"

%install
install -Dm0755 target/release/sequoia-policy-config-check %{buildroot}%{_bindir}/sequoia-policy-config-check
install -Dm0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/sequoia-policy-config-check.1

%files
%doc README.md openpgp-policy.toml
%license LICENSE.txt
%{_bindir}/sequoia-policy-config-check
%{_mandir}/man1/sequoia-policy-config-check.1*

%changelog
%autochangelog
