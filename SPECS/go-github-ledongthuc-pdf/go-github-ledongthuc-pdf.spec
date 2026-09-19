# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pdf
%define go_import_path  github.com/ledongthuc/pdf
%define commit_id       6c8c28e0e8a07a3452f9d8cf3090ed6e856d8f24
# pdfpasswd retains the canonical rsc.io/pdf/pdfpasswd import comment.
%define go_test_exclude %{go_import_path}/pdfpasswd

Name:           go-github-ledongthuc-pdf
Version:        0+git20260907.6c8c28e
Release:        %autorelease
Summary:        Go library for reading PDF files
License:        BSD-3-Clause
URL:            https://github.com/ledongthuc/pdf
#!RemoteAsset:  sha256:bd7d725666e2b524505362fe4759911ee1e2e75c801eec73934d761cb3785848
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}




BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a Go library for extracting text and formatting
information from PDF files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
