# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname arpy

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Library for accessing "ar" files
License:        BSD-3-Clause
URL:            https://github.com/viraptor/arpy
#!RemoteAsset:  sha256:e2ce13869a2df98b420adeaf7429b63796e8c000969d2dfe471854c0be3d9a54
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
