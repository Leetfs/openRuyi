# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           jurand
Version:        1.4.0
Release:        %autorelease
Summary:        Remove Java annotations, imports and module requirements
License:        Apache-2.0
URL:            https://github.com/fedora-java/jurand
#!RemoteAsset:  sha256:48ecc1a45f3378e93eb55146605308a93e681e4eb2c7a17d44726ef08a5f7dd4
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  all manpages

BuildRequires:  asciidoctor
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Jurand parses Java source files and removes selected imports, annotations
and module requirements. It can rewrite a source tree in place or write a
transformed source file to standard output.

# The upstream Makefile is ready to use in the source tree.
%conf

%install
buildroot=%{buildroot} bindir=%{_bindir} mandir=%{_mandir} ./install.sh

%files
%doc README.adoc
%license LICENSE NOTICE
%{_bindir}/jurand
%{_mandir}/man1/jurand.1*

%changelog
%autochangelog
