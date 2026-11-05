# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global release_series 26.8.2
%global private_sonames ^(lib.*lo|libuno_[^.]+|libreglo|libunoidl|libxmlreader|libstore)\.so.*$
%global __provides_exclude %{private_sonames}
%global __requires_exclude %{private_sonames}

Name:           libreoffice
Version:        %{release_series}.2
Release:        %autorelease
Summary:        Desktop office suite for OpenDocument and Microsoft Office files
License:        MPL-2.0 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND MIT AND MPL-1.1
URL:            https://www.libreoffice.org/
VCS:            git:https://git.libreoffice.org/core
#!RemoteAsset:  sha256:f0012302d9cc70955bd55890d3aaccf6c55677c4a6a46e1003f996b1b0dae8e7
Source0:        https://download.documentfoundation.org/libreoffice/src/%{release_series}/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:1a3b6077ebfac899f2c31666d283e29e94c2d30704dd162fda7ba06d77212dd2
Source1:        https://download.documentfoundation.org/libreoffice/src/%{release_series}/%{name}-translations-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(prep):  -b 1
BuildOption(conf):  --enable-release-build
BuildOption(conf):  --with-vendor=openRuyi
BuildOption(conf):  --with-lang="en-US zh-CN"
BuildOption(conf):  --with-theme=colibre
BuildOption(conf):  --enable-split-app-modules
BuildOption(conf):  --enable-build-opensymbol
BuildOption(conf):  --enable-python=system
BuildOption(conf):  PYTHON_CFLAGS="$(pkg-config --cflags python3-embed)"
BuildOption(conf):  PYTHON_LIBS="$(pkg-config --libs python3-embed)"
BuildOption(conf):  --disable-fetch-external
BuildOption(conf):  --with-external-tar=%{_sourcedir}
BuildOption(conf):  --with-parallelism=%{_smp_build_ncpus}
BuildOption(conf):  --without-fonts
BuildOption(conf):  --with-java
BuildOption(conf):  --with-jdk-home=%{_libdir}/jvm/java-25-openjdk
BuildOption(conf):  --with-system-hsqldb
BuildOption(conf):  --with-hsqldb-jar=%{_datadir}/java/hsqldb1.8/hsqldb.jar
BuildOption(conf):  --with-hamcrest=%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
BuildOption(conf):  --disable-odk
BuildOption(conf):  --disable-epm
BuildOption(conf):  --disable-skia
BuildOption(conf):  --with-system-dicts
BuildOption(conf):  --with-system-libs
BuildOption(conf):  --with-system-libxml
BuildOption(conf):  --without-system-libfixmath
BuildOption(install):  distro-pack-install
# Run independent gbuild test targets after a failure so each module reports its result.
BuildOption(check):  --keep-going

BuildRequires:  ant
BuildRequires:  autoconf
BuildRequires:  beanshell
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake(FastFloat)
BuildRequires:  cmake(dragonbox)
BuildRequires:  firebird-devel >= 3
BuildRequires:  flex
BuildRequires:  fontforge
# The RTL fallback test lays out three Hebrew letters in David Libre.
BuildRequires:  fonts-david-libre
BuildRequires:  fonts-dejavu
BuildRequires:  fonts-liberation
# The forcepoint93-1.rtf import requests the distinct narrow family.
BuildRequires:  fonts-liberation-sans-narrow
# Writer layout fixtures request the Graphite family and Rubik by name.
BuildRequires:  fonts-linux-libertine-g
BuildRequires:  fonts-rubik
# The Draw contour-text check renders a Chinese label with a CJK fallback.
BuildRequires:  fonts-noto-sans-cjk-static
BuildRequires:  fonts-noto-static
BuildRequires:  fonts-reem-kufi
BuildRequires:  gcc-c++
BuildRequires:  lpsolve-devel
BuildRequires:  gettext
BuildRequires:  glm-devel
BuildRequires:  gnupg
BuildRequires:  gperf
BuildRequires:  hsqldb1.8
BuildRequires:  hyphen-devel
BuildRequires:  icu4c
BuildRequires:  java-25-openjdk-devel
BuildRequires:  java-hamcrest1.3
BuildRequires:  java-sac
BuildRequires:  java-websocket
BuildRequires:  junit4
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  pentaho-flute
BuildRequires:  pentaho-libbase
BuildRequires:  pentaho-libformula
BuildRequires:  pentaho-librepository
BuildRequires:  pentaho-libserializer
BuildRequires:  pentaho-libloader
BuildRequires:  pentaho-libxml
BuildRequires:  pentaho-libfonts
BuildRequires:  pentaho-liblayout
BuildRequires:  pentaho-flow-engine
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  pkgconf
BuildRequires:  rhino
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat) >= 2.9.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gpgmepp)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz-icu)
BuildRequires:  pkgconfig(harfbuzz-subset)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libeot) >= 0.01
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libexttextcat) >= 3.4.1
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(libnumbertext) >= 1.0.6
BuildRequires:  pkgconfig(mythes)
BuildRequires:  cmake(frozen)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  zxcvbn-c-devel
BuildRequires:  zxing-cpp-devel
BuildRequires:  zxing-cpp(qr-writer)
BuildRequires:  pkgconfig(liblangtag) >= 0.4.0
BuildRequires:  pkgconfig(mdds-3.0) >= 3.0.0
BuildRequires:  pkgconfig(box2d)
BuildRequires:  pkgconfig(libe-book-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3) >= 0.3.21
BuildRequires:  pkgconfig(liborcus-0.21) >= 0.21.0
BuildRequires:  pkgconfig(libcmis-0.6) >= 0.6.1
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(raptor2) >= 2.0.7
BuildRequires:  pkgconfig(redland) >= 1.0.8
BuildRequires:  pkgconfig(coinmp)
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(md4c-html)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pdfium)
BuildRequires:  pdfium(font-mapping)
BuildRequires:  pkgconfig(poppler) >= 0.14
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  poppler-data
BuildRequires:  python-afdko
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmlsec1-nss)
# xmlsec1-nss.pc links against libltdl, whose linker file is owned by libtool.
BuildRequires:  libtool
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(lxml)
BuildRequires:  unzip
BuildRequires:  xorg-server-xvfb
BuildRequires:  texlive-fontsextra
BuildRequires:  texlive-langarabic
BuildRequires:  zip
Requires:       %{name}-base%{?_isa} = %{version}-%{release}
Requires:       %{name}-calc%{?_isa} = %{version}-%{release}
Requires:       %{name}-draw%{?_isa} = %{version}-%{release}
Requires:       %{name}-impress%{?_isa} = %{version}-%{release}
Requires:       %{name}-math%{?_isa} = %{version}-%{release}
Requires:       %{name}-writer%{?_isa} = %{version}-%{release}

%patchlist
# Backported slideshow support for the system Box2D 3.2 API.
# https://github.com/LibreOffice/core/commit/8927e95539463a027c6f28da2ac5ac46746cf1bd
1000-support-box2d-3.2-slideshow.patch
# Downstream system-library integration for the PDF filters and their upstream tests.
# https://github.com/LibreOffice/core/tree/libreoffice-26.8.2.2/external/pdfium
2000-support-system-pdfium.patch
# Downstream fix for the backend test introduced by LibreOffice.
# https://github.com/LibreOffice/core/commit/25a5b9b136c80c93593097e4463184035218fd56
2001-read-configured-openssl-backend.patch
# Downstream fix for order-dependent Basic and Calc tests.
# https://github.com/LibreOffice/core/tree/libreoffice-26.8.2.2/basic/qa/cppunit
2002-isolate-unit-test-options.patch
# Downstream system library detection from openSUSE Factory revision 324.
# https://api.opensuse.org/public/source/openSUSE:Factory/libreoffice/box2d-detection.patch?rev=324
2003-detect-system-box2d.patch
# Downstream fix for the Box2D 3 body initialization contract.
# https://github.com/erincatto/box2d/blob/v3.2.0/include/box2d/types.h#L220-L222
2004-initialize-slideshow-physics-bodies.patch
# Downstream correction for a font-dependent grid position in the Writer UI test.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sw/qa/uitest/writer_tests2/formatBulletsNumbering.py
2005-select-bullet-by-unicode.patch
# Downstream fix for GnuPG agent sockets under long build paths.
# https://github.com/LibreOffice/core/commit/8ed755cfb0779c3e1119d17a7877768af1a01682
2006-use-short-gpg-test-homes.patch
# Downstream correction to the optimum for the upstream knapsack test data.
# https://github.com/LibreOffice/core/commit/911a57c4d6fc2cbe9d4350189e06a8b733e6f7d3
2007-check-optimal-knapsack-solution.patch
# Downstream fix for reuse of the Writer/Web template across HTML document types.
# https://github.com/LibreOffice/core/commit/303f8e5160ddb39914ba7f669698d5dbe958878a
2008-keep-web-template-out-of-writer-html-import.patch
# Downstream test fix for explicit view modes and formatting marks.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sw/qa/extras/tiledrendering/tiledrendering.cxx
2009-select-writer-view-test-modes.patch
# Downstream fix for regular header and footer text when a system face differs.
# https://github.com/LibreOffice/core/commit/ba4bc66301e0cb30379f19b9c19e320a533daa42
2010-preserve-header-footer-font-style.patch
# Downstream integration with AFDKO 5 for decomposed PDF fonts.
# https://github.com/adobe-type-tools/afdko/releases/tag/5.0.0
2011-use-afdko-makeotf-for-embedded-pdf-fonts.patch
# Downstream adaptation to Noto Sans Arabic 2.013 shaping.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/vcl/qa/cppunit/complextext.cxx
2012-check-fallback-positions-with-split-arabic-glyphs.patch
# Downstream regression check for centered fullwidth CJK punctuation.
# https://github.com/LibreOffice/core/commit/4a92323b54e7d63a8bc0b8e62fdc6b31760dcd05
2013-check-centered-cjk-punctuation-compression.patch
# Downstream integration with distribution-provided fonts for restricted tests.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/solenv/gbuild/CppunitTest.mk
2014-select-the-font-set-for-restricted-cppunit-tests.patch
# Downstream isolation of document-specific formula settings and test locales.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sc/source/ui/docshell/docsh6.cxx
2015-preserve-calc-document-settings-and-test-locales.patch
# Downstream test integration with declared fonts and their verified glyph coverage.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/vcl/unx/generic/fontmanager/fontconfig.cxx
2016-validate-glyph-fallbacks-in-the-declared-test-font-set.patch
# Downstream fix for encoded formula errors on architectures with canonical NaNs.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sc/source/core/tool/scmatrix.cxx
2017-preserve-formula-errors-in-matrix-aggregates.patch
# Downstream test fix for unordered RDF manifest graphs.
# https://www.w3.org/TR/rdf11-concepts/#section-rdf-graph
2018-compare-rdf-statements-independent-of-enumeration-order.patch
# Downstream test fix for the per-view Calc spell-check setting.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sc/source/ui/unoobj/docuno.cxx
2019-initialize-spelling-for-the-calc-view-state-test.patch
# Downstream fix for accessing the per-view clipboard after VCL shutdown.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/desktop/source/lib/lokclipboard.cxx
2020-handle-libreofficekit-clipboard-shutdown.patch
# Downstream test fix for page view mode and text portions in aligned paragraphs.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sw/qa/extras/uiwriter/uiwriter4.cxx
2021-check-writer-page-and-space-layout.patch
# Downstream fix for a glyph fallback match that supplies none of the requested characters.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/vcl/unx/generic/fontmanager/fontconfig.cxx
2022-select-a-font-with-glyphs-for-uncovered-runs.patch
# Downstream test fix for per-view color scheme persistence across chart and pixel tests.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/sw/qa/extras/tiledrendering/tiledrendering.cxx
2023-select-and-restore-writer-pixel-test-theme.patch

%description
LibreOffice provides word processing, spreadsheets, presentations, drawings,
formula editing and database access. This package installs the full suite.

%package        core
Summary:        Shared runtime and desktop integration for LibreOffice
# The SAX locator uses the 64-bit position API added in Expat 2.9.
Requires:       expat%{?_isa} >= 2.9.0
# GPGME uses the external OpenPGP engine for document signing and encryption.
Requires:       gnupg
# The script providers load the system BeanShell and Rhino JARs.
Requires:       beanshell
Requires:       rhino
Requires:       java-25-openjdk
Requires:       java-websocket
Requires:       python-afdko
Requires:       zxing-cpp(qr-writer)
Requires:       pdfium(font-mapping)
Recommends:     fonts-dejavu
Recommends:     fonts-liberation
Recommends:     sane-backends

%description    core
The shared LibreOffice runtime includes the application launcher, UNO
components, document filters and desktop integration.

%package        base
Summary:        Database front end for LibreOffice
# Firebird publishes the ODS 12 embedded engine in the primary repository metadata.
Requires:       libEngine12.so()(64bit)
# The embedded SDBC driver loads the configured system HSQLDB 1.8 JAR.
Requires:       hsqldb1.8
# The Report Builder JAR loads these system JARs through its manifest Class-Path.
Requires:       java-sac
Requires:       pentaho-flow-engine
Requires:       pentaho-flute
Requires:       pentaho-libbase
Requires:       pentaho-libfonts
Requires:       pentaho-libformula
Requires:       pentaho-liblayout
Requires:       pentaho-libloader
Requires:       pentaho-librepository
Requires:       pentaho-libserializer
Requires:       pentaho-libxml
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    base
Base edits database forms, queries and reports. It connects to embedded
Firebird and HSQLDB databases as well as external database servers.

%package        calc
Summary:        Spreadsheet editor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    calc
Calc edits spreadsheets, calculates formulas and creates charts.

%package        draw
Summary:        Drawing and diagram editor for LibreOffice
Requires:       poppler-data
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    draw
Draw creates vector drawings, diagrams and multipage illustrations.

%package        impress
Summary:        Presentation editor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    impress
Impress creates slide presentations with drawings, transitions and speaker notes.

%package        math
Summary:        Formula editor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    math
Math typesets mathematical expressions for use in LibreOffice documents.

%package        writer
Summary:        Word processor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    writer
Writer edits text documents and reads and writes OpenDocument Text and Microsoft Word files.

%package        lang-zh-CN
Summary:        Simplified Chinese translations for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Recommends:     (fonts-noto-sans-cjk-vf or fonts-noto-sans-cjk-static)
Supplements:    (%{name}-core and langpacks-zh)

%description    lang-zh-CN
Simplified Chinese menus, messages, templates and configuration resources
for LibreOffice.

%prep -a
autoconf -I m4

%install -a
# LibreOffice also loads localized registries and templates from its own tree.
# Keep its catalog lookup path while allowing find_lang to identify the domains.
resources=%{_libdir}/%{name}/program/resource
catalogs=%{_datadir}/%{name}/locale
install -d "%{buildroot}$catalogs/zh_CN"
mv "%{buildroot}$resources/zh_CN/LC_MESSAGES" "%{buildroot}$catalogs/zh_CN/"
ln -sr "%{buildroot}$catalogs/zh_CN/LC_MESSAGES" "%{buildroot}$resources/zh_CN/LC_MESSAGES"
sed -i "\|$resources/zh_CN/LC_MESSAGES|d" file-lists/lang_zh_CN_list.txt
%find_lang %{name} --all-name

# RPM reads desktop MIME types through these links while the files are staged.
for link in %{buildroot}%{_datadir}/applications/%{name}-*.desktop %{buildroot}%{_bindir}/{%{name},soffice}; do
    target=$(readlink "$link")
    test -f "%{buildroot}$target"
    ln -srf "%{buildroot}$target" "$link"
done

# Bash looks up completions by command name.
completions=%{_datadir}/bash-completion/completions
for cmd in libreoffice loffice lofromtemplate unopkg lowriter loweb lobase localc lodraw loimpress lomath; do
    manifest=$(grep -Flx "%{_bindir}/$cmd" file-lists/{common,writer,base,calc,draw,impress,math}_list.txt)
    ln -s libreoffice.sh "%{buildroot}$completions/$cmd"
    echo "$completions/$cmd" >> "$manifest"
done

# The upstream split installer leaves the BeanShell provider in its original module list.
cat file-lists/orig/gid_Module_Optional_Extensions_Script_Provider_For_BS >> file-lists/common_list.txt

# The installer lists private directories in several application manifests.
# The core runtime owns them so individual applications can be removed safely.
for list in file-lists/*_list.txt; do
    sed -n '/^%%dir /p' "$list"
done | sort -u | sed "\|$resources/zh_CN/LC_MESSAGES|d" > file-lists/directories.list
for list in file-lists/*_list.txt; do
    sed -i '/^%%dir /d' "$list"
done
cat file-lists/common_list.txt file-lists/lang_en_US_list.txt file-lists/gnome_list.txt |
    sort -u > file-lists/core.list
sed -i '/\/LICENSE\(\.html\)\?$/d' file-lists/core.list
sort -u file-lists/base_list.txt file-lists/postgresql_list.txt > file-lists/base.list

%check -p
# Provide a private X display for the upstream desktop and UI tests.
display_file=$(mktemp)
Xvfb -displayfd 3 -screen 0 1280x1024x24 -nolisten tcp 3>"$display_file" &
xvfb_pid=$!
# In chroots without /run/user, gpg-agent opens its socket inside each test home.
LIBO_TEST_GPG_ROOT=$(mktemp -d /tmp/lo-gpg.XXXXXXXX)
export LIBO_TEST_GPG_ROOT
cleanup() {
    kill "$xvfb_pid" 2>/dev/null || :
    rm -f "$display_file"
    for keyring in "$LIBO_TEST_GPG_ROOT"/*; do
        test ! -d "$keyring" || gpgconf --homedir "$keyring" --kill gpg-agent || :
    done
    rm -rf "$LIBO_TEST_GPG_ROOT"
}
trap cleanup EXIT
for attempt in $(seq 100); do
    test ! -s "$display_file" || break
    kill -0 "$xvfb_pid"
    sleep 0.1
done
test -s "$display_file"
export DISPLAY=:$(cat "$display_file")

# Restrict font-sensitive tests to the RPM faces they request. The two PDF
# variable-font fixtures embed their own faces; unrelated TeX static copies
# would shadow those instances. The buildroot has already been installed.
export LIBO_TEST_FONTCONFIG_FILE="$PWD/workdir/openruyi-test-fonts.conf"
python3 - <<'FONTS'
from pathlib import Path
from subprocess import check_output
from xml.etree import ElementTree as ET
import os

fonts = Path("instdir/share/fonts/truetype").resolve()
fonts.mkdir(parents=True, exist_ok=True)
packages = ("fonts-david-libre", "fonts-dejavu", "fonts-linux-libertine-g",
            "fonts-liberation-mono", "fonts-liberation-sans", "fonts-liberation-serif",
            "fonts-liberation-sans-narrow",
            "fonts-noto-sans-cjk-static", "fonts-noto-static", "fonts-reem-kufi", "fonts-rubik")
files = set(check_output(["rpm", "-ql", *packages], text=True).splitlines())
for family in ("Carlito", "Caladea", "Amiri", "Amiri Quran"):
    files.update(check_output(["fc-list", family, "--format", "%%{file}\n"], text=True).splitlines())
for path in sorted(map(Path, files)):
    if path.is_file() and path.suffix.lower() in (".ttf", ".ttc", ".otf"):
        target = fonts / path.name
        if not target.exists():
            target.symlink_to(path)
profile = ET.Element("fontconfig")
ET.SubElement(profile, "include").text = "/etc/fonts/fonts.conf"
ET.SubElement(profile, "reset-dirs")
ET.SubElement(profile, "dir").text = str(fonts)
ET.ElementTree(profile).write(os.environ["LIBO_TEST_FONTCONFIG_FILE"], encoding="utf-8")
FONTS

%files

%files core -f file-lists/core.list -f file-lists/directories.list
%doc README.md
%license COPYING COPYING.LGPL COPYING.MPL
%license %{_libdir}/libreoffice/LICENSE
%license %{_libdir}/libreoffice/LICENSE.html
%dir %{_datadir}/libreoffice
%dir %{_datadir}/libreoffice/locale
%{_libdir}/libreoffice/share/libreofficekit/
%{_datadir}/metainfo/org.libreoffice.kde.metainfo.xml

%files base -f file-lists/base.list
%{_datadir}/metainfo/libreoffice-base.appdata.xml

%files calc -f file-lists/calc_list.txt
%{_datadir}/metainfo/libreoffice-calc.appdata.xml

%files draw -f file-lists/draw_list.txt
%{_datadir}/metainfo/libreoffice-draw.appdata.xml

%files impress -f file-lists/impress_list.txt
%{_datadir}/metainfo/libreoffice-impress.appdata.xml

%files math -f file-lists/math_list.txt

%files writer -f file-lists/writer_list.txt
%{_datadir}/metainfo/libreoffice-writer.appdata.xml

%files lang-zh-CN -f file-lists/lang_zh_CN_list.txt -f %{name}.lang
%lang(zh_CN) %dir %{_datadir}/%{name}/locale/zh_CN
%lang(zh_CN) %dir %{_datadir}/%{name}/locale/zh_CN/LC_MESSAGES
%lang(zh_CN) %{_libdir}/%{name}/program/resource/zh_CN/LC_MESSAGES

%changelog
%autochangelog
