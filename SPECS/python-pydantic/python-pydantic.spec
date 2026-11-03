# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydantic

Name:           python-%{srcname}
Version:        2.14.2
Release:        %autorelease
Summary:        Data validation using Python type hints
License:        MIT
URL:            https://github.com/pydantic/pydantic
#!RemoteAsset:  sha256:fb7b2db6cefe8414dd612edeede49c4c433acb0432b0f92b95024e45f66c505d
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# This check will result in a circular dependency
# https://github.com/python/mypy/issues/17726
BuildOption(check):  -e "pydantic.mypy"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(annotated-types)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydantic-core)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(typing-inspection)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

# use the pydantic-core provided by the system
%prep -a
rm -f pydantic-core/

%description
Data validation using Python type hints.
Fast and extensible, Pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.9+; validate it with Pydantic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
