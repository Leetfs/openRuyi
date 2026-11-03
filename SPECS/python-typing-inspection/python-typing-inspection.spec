# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname typing-inspection
%global pypi_name typing_inspection

Name:           python-typing-inspection
Version:        0.4.4
Release:        %autorelease
Summary:        Runtime typing introspection tools
License:        MIT
URL:            https://github.com/pydantic/typing-inspection
#!RemoteAsset:  sha256:547274fa6b0a561ccf549cc9524b999a578e737d015d8709d021f9d0d13bea47
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
typing-inspection provides tools to inspect type annotations at runtime.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
