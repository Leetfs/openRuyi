# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname inscriptis

Name:           python-%{srcname}
Version:        2.7.6
Release:        %autorelease
Summary:        Convert HTML to text
License:        Apache-2.0
URL:            https://github.com/weblyzard/inscriptis
#!RemoteAsset:  sha256:b8fe23c5ae4db33c9d1c5e1b7d000dbfa1decbea7b605ac87e0f5d8f8abc3ce6
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(fastapi)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Inscriptis converts HTML documents to plain text.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/inscript
%{_bindir}/inscriptis-api

%changelog
%autochangelog
