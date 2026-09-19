# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ujson

Name:           python-%{srcname}
Version:        6.0.0
Release:        %autorelease
Summary:        Ultra fast JSON encoder and decoder for Python
License:        BSD-3-Clause AND TCL
URL:            https://github.com/ultrajson/ultrajson
#!RemoteAsset:  sha256:80e23393feb707582e0ad495c397a4477b646d08094d2df64f7316f9fafd8aae
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C with bindings for
Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%{python3_sitearch}/ujson-stubs/__init__.pyi

%changelog
%autochangelog
