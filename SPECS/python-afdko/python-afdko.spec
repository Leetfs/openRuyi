# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname afdko

Name:           python-%{srcname}
Version:        5.0.1
Release:        %autorelease
Summary:        Adobe Font Development Kit for OpenType
License:        Apache-2.0
URL:            https://github.com/adobe-type-tools/afdko
#!RemoteAsset:  sha256:083b504a1cd865e8bfbb42134a34318ce42ef5130daebfc5b0e2f2fb444326c5
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
# Accepted upstream for single-glyph and uniform-width fonts.
# https://github.com/adobe-type-tools/afdko/commit/025281e7849e42e556fc0a2e51069b757fdddef4
Patch1:         0001-prevent-underflow-when-trimming-advance-widths.patch
# Downstream support for the exported shared target of system ANTLR.
# https://github.com/adobe-type-tools/afdko/blob/5.0.1/third_party/antlr4cpp/CMakeLists.txt
Patch2000:      2000-link-to-shared-system-antlr-runtime.patch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

# scikit-build-core queries the native CMake executable before emitting wheel requirements.
BuildRequires:  cmake >= 3.16
BuildRequires:  cmake(antlr4-runtime)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  gcc-c++
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
AFDKO builds and inspects OpenType fonts. It includes command-line tools
for compiling feature definitions, merging font programs and converting
PostScript outlines.

%prep -a
sed -i '/^license = "Apache-2.0"$/a license-files = ["LICENSE.md"]' pyproject.toml

%build -p
export FORCE_SYSTEM_ANTLR4=1 FORCE_SYSTEM_LIBXML2=1
export CMAKE_ARGS="-DFETCHCONTENT_FULLY_DISCONNECTED=ON"

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise the tx, makeotf and mergefonts programs used to reconstruct embedded PDF fonts.
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONPATH=%{buildroot}%{python3_sitearch}
python3 -m pytest -q tests/tx_test.py tests/makeotf_test.py tests/mergefonts_test.py

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/addfeatures
%{_bindir}/afdko
%{_bindir}/buildcff2vf
%{_bindir}/buildmasterotfs
%{_bindir}/charplot
%{_bindir}/checkoutlinesufo
%{_bindir}/comparefamily
%{_bindir}/detype1
%{_bindir}/digiplot
%{_bindir}/fontplot
%{_bindir}/fontplot2
%{_bindir}/fontsetplot
%{_bindir}/hintplot
%{_bindir}/makeinstancesufo
%{_bindir}/makeotf
%{_bindir}/makeotfexe
%{_bindir}/mergefonts
%{_bindir}/otc2otf
%{_bindir}/otf2otc
%{_bindir}/otf2ttf
%{_bindir}/otfautohint
%{_bindir}/otfstemhist
%{_bindir}/rotatefont
%{_bindir}/sfntdiff
%{_bindir}/sfntedit
%{_bindir}/spot
%{_bindir}/ttfcomponentizer
%{_bindir}/ttfdecomponentizer
%{_bindir}/ttxn
%{_bindir}/tx
%{_bindir}/type1
%{_bindir}/waterfallplot

%changelog
%autochangelog
