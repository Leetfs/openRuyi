# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httpx2

Name:           python-%{srcname}
Version:        2.12.0
Release:        %autorelease
Summary:        HTTP client for Python
License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
#!RemoteAsset:  sha256:7631fe9887a8a2275f4a2540e053aa670fcc50742864a9ae7c66e609fdcf12cf
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Disable dynamic versioning and use the system TLS backend.
Patch2000:      2000-python-httpx2-use-static-version-and-system-tls.patch

BuildOption(install):  -l %{srcname}
BuildOption(check):   -e %{srcname}.websockets

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(httpcore2)
BuildRequires:  python3dist(idna)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HTTPX 2 provides a next generation HTTP client for Python.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/httpx2

%changelog
%autochangelog
