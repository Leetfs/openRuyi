# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python_discovery
%global pypi_name python-discovery

Name:           python-python-discovery
Version:        1.9.0
Release:        %autorelease
Summary:        Python interpreter discovery
License:        MIT
URL:            https://github.com/tox-dev/python-discovery
#!RemoteAsset:  sha256:88beb57e51b919c30f303b053ec41359298ca349192035b0a802c76347ae96d7
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# The Windows interpreter-discovery helpers require Windows APIs during import.
BuildOption(check):  -e 'python_discovery._windows.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{pypi_name} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
python-discovery is a library for discovering Python interpreters installed on a system.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
