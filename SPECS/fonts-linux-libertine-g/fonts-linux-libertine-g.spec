# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-linux-libertine-g
Version:        20120116
Release:        %autorelease
Summary:        Linux Libertine G serif fonts with Graphite features
License:        OFL-1.0-RFN OR (GPL-2.0-only WITH Font-exception-2.0)
URL:            https://numbertext.org/linux/
# VCS: No VCS link available
#!RemoteAsset:  sha256:54adcb2bc8cac0927a647fbd9362f45eff48130ce6e2379dc3867643019e08c5
Source0:        %{url}e7a384790b13c29113e22e596ade9687-LinLibertineG-%{version}.zip
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros
BuildRequires:  harfbuzz-devel
BuildRequires:  python3dist(fonttools)
BuildRequires:  unzip

%description
Linux Libertine G is the Graphite edition of the Linux Libertine serif
family. Its six faces provide ligatures, small capitals, and number styles.

%prep
%autosetup -n LinLibertineG
chmod 0644 GPL.txt LICENCE.txt OFL.txt

%install
# The 2012 generator emits unequal substitution sequences rejected by grcompiler.
# Install the six upstream Graphite faces from the author's release.
%install_fonts LinLibertine_R*_G.ttf linux-libertine-g

%check
# Verify the six released faces, Graphite tables and actual shaping with Graphite2.
python3 - <<'TEST'
from pathlib import Path
from subprocess import check_output
from fontTools.ttLib import TTFont

styles = set()
for path in Path(".").glob("LinLibertine_R*_G.ttf"):
    with TTFont(path) as font:
        assert font["name"].getBestFamilyName() == "Linux Libertine G"
        styles.add(font["name"].getBestSubFamilyName())
        assert {"Silf", "Feat", "Glat", "Gloc", "Sill"} <= set(font.keys())
        assert {0x0041, 0x00E1, 0x0171} <= font.getBestCmap().keys()
    glyphs = check_output(["hb-shape", "--shapers=graphite2", str(path), "office"], text=True)
    assert glyphs.startswith("[") and ".notdef" not in glyphs and "gid0=" not in glyphs, glyphs
assert styles == {"Regular", "Italic", "Semibold", "Semibold Italic", "Bold", "Bold Italic"}, styles
TEST

%files
%doc README
%license GPL.txt LICENCE.txt OFL.txt
%font_files linux-libertine-g ttf

%changelog
%autochangelog
