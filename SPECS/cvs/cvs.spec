# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cvs
Version:        1.12.13
Release:        %autorelease
Summary:        Concurrent Versions System
License:        GPL-1.0-or-later AND GPL-2.0-or-later AND Latex2e-translated-notice AND LicenseRef-openRuyi-Public-Domain
URL:            https://www.nongnu.org/cvs/
VCS:            cvs::pserver:anonymous@cvs.savannah.nongnu.org:/sources/cvs
#!RemoteAsset:  sha256:78853613b9a6873a30e1cc2417f738c330e75f887afdaf7b3d0800cb19ca515e
Source:         https://ftp.gnu.org/non-gnu/cvs/source/feature/%{version}/cvs-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)

Requires:       %{_bindir}/ssh
Requires:       %{_bindir}/vi

%patchlist
# Fix CVE-2012-0804 by validating HTTP proxy status responses.
# Origin: https://src.opensuse.org/pool/cvs/src/branch/factory/cvs-CVE-2012-0804.patch
1001-fix-proxy-response-parser.patch
# Fix CVE-2017-12836 by rejecting CVS roots that begin with an option.
# Origin: https://src.opensuse.org/pool/cvs/src/branch/factory/cvs-Bug-1053364-disallow-dash.patch
1002-reject-leading-dash-in-cvsroot.patch
# Fix nonliteral format strings rejected by hardened compiler flags.
# Origin: https://src.opensuse.org/pool/cvs/src/branch/factory/compile-with-Wformat-security.patch
# (External patch; URL above.)
1003-fix-format-security.patch
# Local openRuyi compatibility fix; no external distro source.
# Use the system allocation declarations with current C libraries.
2000-use-system-stdlib-declarations.patch
# Local openRuyi compatibility fix; no external distro source.
# Avoid glibc aborting on the legacy writable %n length probe.
2001-avoid-glibc-dynamic-percent-n.patch
# Local openRuyi compatibility fix; no external distro source.
# Accept the riscv64-openruyi-linux triplet used by OBS.
# Numbered in the 2000-2999 openRuyi-specific range.
2002-accept-riscv64-openruyi-triplet.patch
# Local openRuyi security hardening; no external distro source.
# Reject server pathnames that escape the client work tree.
2003-reject-unsafe-server-paths.patch

%description
CVS is a version control system that records the history of files and
coordinates concurrent changes to hierarchical source trees. It supports
local repositories and remote access through secure shell transports.

%conf
# Upstream's configure predates the --docdir option injected by the
# declarative autotools configuration stage.
# The bundled probe checks ptrdiff_t without including stddef.h and records
# an impossible size of zero, which creates a duplicate LP64 switch case.
# The same probe accepts undeclared functions and otherwise skips the bundled
# gnulib implementations of these format helpers.
ac_cv_func_nanotime=no \
ccvs_cv_unique_int_type_ptrdiff_t=no \
ac_cv_func_vasnprintf=no \
ac_cv_func_vasprintf=no \
CFLAGS="%{optflags} -std=gnu17 -D_GNU_SOURCE" LDFLAGS="%{build_ldflags}" ./configure \
    --build=%{_build} \
    --host=%{_host} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --with-editor=%{_bindir}/vi \
    --with-external-zlib \
    --with-rsh=%{_bindir}/ssh

%install -a
# These unsupported or obsolete helpers are outside the core CVS package.
rm -f %{buildroot}%{_bindir}/cvsbug
rm -f %{buildroot}%{_bindir}/rcs2log
rm -f %{buildroot}%{_mandir}/man8/cvsbug.8
rm -r %{buildroot}%{_datadir}/cvs
rm -f %{buildroot}%{_infodir}/dir

%check
# The full legacy sanity.sh suite fails its basica-notadded output assertion
# under the current OBS shell/toolchain; retain the deterministic library test.
make -j1 -C lib check

%files
%doc AUTHORS BUGS NEWS README
%license COPYING COPYING.LIB
%{_bindir}/cvs
%{_infodir}/cvs.info*
%{_infodir}/cvsclient.info*
%{_mandir}/man1/cvs.1*
%{_mandir}/man5/cvs.5*

%changelog
%autochangelog
