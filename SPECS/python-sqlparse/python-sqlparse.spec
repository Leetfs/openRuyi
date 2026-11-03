# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sqlparse

Name:           python-%{srcname}
Version:        0.6.1
Release:        %autorelease
Summary:        Non-validating SQL parser
License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
#!RemoteAsset:  sha256:ca722573f848ff2d30e40ea30f53a104b7dea7635ea9285891263eb2c58fb6e7
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sqlparse is a non-validating SQL parser for Python.  It
provides support for parsing, splitting and formatting SQL statements.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise statement splitting, token grouping and the parser's denial-of-service regressions.
%pytest -v tests

%files -f %{pyproject_files}
%doc CHANGELOG README.md
%{_bindir}/sqlformat

%changelog
%autochangelog
