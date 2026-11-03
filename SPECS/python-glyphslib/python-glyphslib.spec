# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname glyphslib

Name:           python-%{srcname}
Version:        6.17.1
Release:        %autorelease
Summary:        Bridge from Glyphs source files to UFOs
License:        Apache-2.0
URL:            https://pypi.org/project/glyphsLib/
VCS:            git:https://github.com/googlefonts/glyphsLib
#!RemoteAsset:  sha256:98cc973d768c534b62f70a6de242865b85abc74009c056859c82ea63230833c2
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l glyphsLib +auto
# These UFO feature writers and filters import ufo2ft during module loading.
BuildOption(check):  -e "glyphsLib.featureWriters.markFeatureWriter"
BuildOption(check):  -e "glyphsLib.filters.cornerComponents"
BuildOption(check):  -e "glyphsLib.filters.eraseOpenCorners"

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(openstep-plist)
BuildRequires:  python3dist(ufolib2)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
glyphsLib bridges Glyphs source files (.glyphs) to UFOs and Designspace.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
