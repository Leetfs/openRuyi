# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-reflector
%define go_import_path  github.com/tkrajina/go-reflector

Name:           go-github-tkrajina-go-reflector
Version:        0.5.8
Release:        %autorelease
Summary:        Convenience helpers around Go reflection
License:        Apache-2.0
URL:            https://github.com/tkrajina/go-reflector
#!RemoteAsset:  sha256:4ad23d4bc92bc8fd2eab009515a123663c3ee4fad127cf3e3617b73c6a6f7711
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-call-the-renamed-Subtract-method-in-tests.patch




BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides convenience helpers for inspecting Go values with the
standard reflection API.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
