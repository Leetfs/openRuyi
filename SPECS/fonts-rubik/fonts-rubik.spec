# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit e337a5f69a9bea30e58d05bd40184d79cc099628

Name:           fonts-rubik
Version:        2.300
Release:        %autorelease
Summary:        Rubik variable sans-serif typeface
License:        OFL-1.1
URL:            https://github.com/googlefonts/rubik
#!RemoteAsset:  sha256:084747d015f017e784d5e9673c1f6479ab36100e3fead20573fef3623e438334
Source0:        %{url}/archive/%{commit}.tar.gz#/rubik-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros
BuildRequires:  python3dist(fontmake)
BuildRequires:  python3dist(fonttools)

%description
Rubik is a sans-serif family with rounded corners. Its upright and italic
fonts cover Hebrew, Cyrillic and Latin and support a variable weight axis.

%prep
%autosetup -n rubik-%{commit}
chmod 0644 AUTHORS.txt CONTRIBUTORS.txt

%build
mkdir built
fontmake -g sources/Rubik.glyphs -o variable --output-path built/Rubik.ttf
fontmake -g sources/Rubik-Italic.glyphs -o variable --output-path built/Rubik-Italic.ttf

%install
%install_fonts built/*.ttf rubik

%check
# Check the weight range, italic flag and Hebrew coverage of the built variable fonts.
python3 - <<'TEST'
from pathlib import Path
from fontTools.ttLib import TTFont

for path in sorted(Path("built").glob("*.ttf")):
    with TTFont(path) as font:
        assert font["name"].getBestFamilyName() == "Rubik"
        axis, = font["fvar"].axes
        assert (axis.axisTag, axis.minValue, axis.maxValue) == ("wght", 300, 900)
        assert bool(font["head"].macStyle & 2) == ("Italic" in path.name)
        assert {0x0041, 0x0410, 0x05D0} <= font.getBestCmap().keys()
TEST

%files
%doc AUTHORS.txt CONTRIBUTORS.txt README.md
%license OFL.txt
%font_files rubik ttf

%changelog
%autochangelog
