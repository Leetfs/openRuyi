# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream liberation-sans-narrow

Name:           fonts-liberation-sans-narrow
Version:        1.07.6
Release:        %autorelease
Summary:        Narrow sans-serif fonts metrically compatible with Arial Narrow
# License.txt contains GPLv2 with Red Hat's embedding and source-access exceptions.
License:        LicenseRef-Liberation-Fonts
URL:            https://github.com/liberationfonts/liberation-sans-narrow
#!RemoteAsset:  sha256:d51c4f321bd108e800638d15c80fada2eb92e3411627bfcfa785c2542d4df8a0
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{upstream}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(prep):  -n %{upstream}-%{version}

BuildRequires:  fontforge
BuildRequires:  fonts-rpm-macros
BuildRequires:  make
BuildRequires:  python3dist(fonttools)

%description
Liberation Sans Narrow provides regular, italic, bold and bold italic
condensed faces for documents using Arial Narrow metrics.

# The upstream Makefile builds the four original SFD files with FontForge.
%conf

%build
%make_build ttf-dir

%install
%install_fonts liberation-narrow-fonts-ttf-%{version}/LiberationSansNarrow-*.ttf liberation-sans-narrow

%check
# Read the family, styles and character coverage from the generated fonts.
python3 - <<'TEST'
from pathlib import Path
from fontTools.ttLib import TTFont

styles = set()
for path in Path("liberation-narrow-fonts-ttf-%{version}").glob("*.ttf"):
    with TTFont(path) as font:
        assert font["name"].getBestFamilyName() == "Liberation Sans Narrow"
        assert {0x41, 0x20AC} <= font.getBestCmap().keys()
        styles.add(font["name"].getBestSubFamilyName())
assert styles == {"Regular", "Italic", "Bold", "Bold Italic"}, styles
TEST

%files
%doc AUTHORS ChangeLog README.rst
%license COPYING License.txt
%font_files liberation-sans-narrow ttf

%changelog
%autochangelog
