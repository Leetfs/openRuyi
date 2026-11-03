# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aliftools

Name:           python-%{srcname}
Version:        0.1.10
Release:        %autorelease
Summary:        Helper tools for building Alif Type Foundry fonts
License:        Apache-2.0
URL:            https://github.com/aliftype/tools
#!RemoteAsset:  sha256:1790c786b097d6c07f13c99cd2d3d1e9845c43d7929c29d564b289aee0f5958b
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Downstream feature selection for the font build tools.
# https://github.com/aliftype/tools/blob/v0.1.10/pyproject.toml
Patch2000:      2000-select-font-build-tools.patch

BuildOption(install):  -l alifTools
# Import the top-level package here and exercise the selected font filters below.
BuildOption(check):  -t

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ufo2ft)
BuildRequires:  python3dist(ufolib2)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Build filters and glyph-name tools for Alif Type Foundry fonts.

%pyproject_extras_subpkg -n python-%{srcname} filters

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Check the placeholder filter options from the installed module.
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 - <<'TEST'
from alifTools.filters import ClearPlaceholdersFilter

assert ClearPlaceholdersFilter().options.anchors
TEST
# Apply the upstream version filter to UFO fonts and check the resulting font version.
%pytest tests/filters_test.py

%files -f %{pyproject_files}
%{_bindir}/strip-glyph-names
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
