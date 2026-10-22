# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sq-cryptoki
Version:        0.2.0
Release:        %autorelease
Summary:        OpenPGP operations using PKCS#11 tokens
License:        LGPL-2.0-or-later AND CC-BY-4.0
URL:            https://sequoia-pgp.org/
VCS:            git:https://gitlab.com/sequoia-pgp/sequoia-cryptoki
#!RemoteAsset:  sha256:894f10b56967a7577c618a7538a03c26e5b2019ad0ec071a8352d82a281f220a
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros
# Additional dependencies required by OBS builds.
BuildRequires:  rust
BuildRequires:  crate(anyhow-1/default) >= 1.0.18

%description
Tool for working with PKCS#11 devices (cryptokis) from Sequoia.

%build -p
export ASSET_OUT_DIR="$PWD/assets"

%build -a
help2man --no-info --version-string=%{version} --name='OpenPGP operations using PKCS#11 tokens' --output=sq-cryptoki.1 target/release/sq-cryptoki

%check -p
export ASSET_OUT_DIR="$PWD/assets"
export RUST_TEST_FLAGS="--release"
export SEQUOIA_CRYPTOKI_BACKEND=softhsm2
export SEQUOIA_CRYPTOKI_MODULE=%{_libdir}/pkcs11/libsofthsm2.so

%install
install -Dm0755 target/release/sq-cryptoki %{buildroot}%{_bindir}/sq-cryptoki
install -Dm0644 sq-cryptoki.1 %{buildroot}%{_mandir}/man1/sq-cryptoki.1

%files
%doc README.md
%license LICENSE-CC-BY-4.0.txt LICENSE-LGPL-2.0.txt LICENSE.txt
%{_bindir}/sq-cryptoki
%{_mandir}/man1/sq-cryptoki.1*

%changelog
%autochangelog
