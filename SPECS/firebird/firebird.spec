# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global build_number 33856-0

Name:           firebird
Version:        3.0.14
Release:        %autorelease
Summary:        Firebird embedded SQL database engine and client tools
License:        Interbase-1.0 AND LicenseRef-IDPL-1.0 AND BSD-3-Clause AND BSD-4-Clause AND LicenseRef-openRuyi-Public-Domain AND LicenseRef-Spencer-Firebird
URL:            https://firebirdsql.org/
VCS:            git:https://github.com/FirebirdSQL/firebird.git
#!RemoteAsset:  sha256:dce3f26c0f015b3c40f36085f8cc21de58dd568e0f347fdd0fcc7942deda8cff
Source0:        https://github.com/FirebirdSQL/firebird/releases/download/v%{version}/Firebird-%{version}.%{build_number}.tar.bz2
BuildSystem:    autotools

BuildOption(prep):  -n Firebird-%{version}.%{build_number}
BuildOption(conf):  --with-system-editline
BuildOption(conf):  --with-fbbin=%{_bindir}
BuildOption(conf):  --with-fbsbin=%{_sbindir}
BuildOption(conf):  --with-fbconf=%{_sysconfdir}/firebird
BuildOption(conf):  --with-fblib=%{_libdir}
BuildOption(conf):  --with-fbinclude=%{_includedir}
BuildOption(conf):  --with-fbintl=%{_libdir}/firebird/intl
BuildOption(conf):  --with-fbsecure-db=%{_sharedstatedir}/firebird
BuildOption(conf):  --with-fbmsg=%{_datadir}/firebird
BuildOption(conf):  --with-fblog=%{_localstatedir}/log/firebird
BuildOption(conf):  --with-fbplugins=%{_libdir}/firebird/plugins
# Keep the Firebird 3 memory-pool and page-access semantics during optimization.
BuildOption(build):  CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags} -std=gnu++11 -fno-lifetime-dse -fno-strict-aliasing" LDFLAGS="%{build_ldflags}"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cloop
BuildRequires:  firebird-btyacc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
%ifarch riscv64
BuildRequires:  pkgconfig(atomic_ops)
%endif
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libtommath)
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(zlib)
Requires:       icu4c

%patchlist
# Firebird CORE-5779, backported to 3.0 by Debian.
# https://github.com/FirebirdSQL/firebird/commit/1e8e7858db84750a77006d307bf28e9686f9414e
1000-firebird-riscv64-implementation.patch
# https://github.com/FirebirdSQL/firebird/commit/8a5b97db3cb519363e5436eedafa763d093890eb
1001-firebird-riscv64-build-prefix.patch
# Distribution integration from Debian's Firebird package.
# https://sources.debian.org/patches/firebird3.0/3.0.14.ds7-1/packaged-boost.patch/
2000-use-system-boost-headers.patch
# CVE-2026-63266: restrict backup difference files to DatabaseAccess paths.
# https://github.com/FirebirdSQL/firebird/pull/9089
1002-check-backup-difference-file-access.patch
# Downstream integration for the installed SQL and IDL compilers.
# https://github.com/asfernandes/cloop/commit/05a4d28642afce2e8efe43e312aada3f2abb70fa
2002-use-installed-interface-and-sql-generators.patch

%description
Firebird supplies an in-process SQL engine for ODS 12 databases. Its
command-line tools execute SQL and back up or restore local databases.

%package        devel
Summary:        Headers and client development files for Firebird
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description    devel
Firebird client headers, linker files and fb_config for building
applications that use the embedded SQL engine.

%prep -a
autoreconf -fi
sed -n '/Copyright (c) 1989 The Regents/,/^ \*\//p' src/common/enc.cpp > BSD-crypt.txt
awk '/Copyright \([Cc]\)/ { keep=1 } keep {print} keep && /\*\// {exit}' src/common/sha2/sha2.h > BSD-SHA2.txt
test -s BSD-crypt.txt
test -s BSD-SHA2.txt
sed -n '/Copyright (c) 1986, 1993, 1995 by University of Toronto/,/4\. This notice must not be removed or altered\./{s,^[[:space:]]*//[[:space:]]*,,;p;}' src/jrd/SimilarToMatcher.h > Spencer-LICENSE.txt
grep -Fq '4. This notice must not be removed or altered.' Spencer-LICENSE.txt

%install
(cd gen && sh install/makeInstallImage.sh)
image=gen/buildroot
install -d %{buildroot}{%{_bindir},%{_includedir}/firebird,%{_libdir},%{_datadir}/firebird,%{_sysconfdir}/firebird}
cp -a "$image"%{_libdir}/libfbclient.so* %{buildroot}%{_libdir}/
cp -a "$image"%{_libdir}/firebird %{buildroot}%{_libdir}/
install -pm 0755 "$image"%{_libdir}/libib_util.so %{buildroot}%{_libdir}/
tar -C "$image"%{_includedir}/firebird --exclude='./impl/boost' -cf - . | tar -C %{buildroot}%{_includedir}/firebird -xf -
install -pm 0644 "$image"%{_includedir}/{ibase.h,iberror.h,ib_util.h} %{buildroot}%{_includedir}/
install -pm 0755 "$image"%{_bindir}/isql %{buildroot}%{_bindir}/firebird-isql
install -pm 0755 "$image"%{_bindir}/gbak "$image"%{_sbindir}/fb_config %{buildroot}%{_bindir}/
install -pm 0644 "$image"%{_sysconfdir}/firebird/{databases.conf,firebird.conf,plugins.conf} %{buildroot}%{_sysconfdir}/firebird/
install -pm 0644 "$image"%{_datadir}/firebird/firebird.msg %{buildroot}%{_datadir}/firebird/

%check
# Compare compiled on-disk page offsets and sizes with the ODS 12 reference.
%make_build -C gen preliminaryCheck
# Exercise the embedded engine, backup and restore from the native build tree.
export FIREBIRD="$PWD/gen/Release/firebird"
export FIREBIRD_BOOT_BUILD=1
export FIREBIRD_MSG="$FIREBIRD"
export LD_LIBRARY_PATH="$FIREBIRD/lib"
export FIREBIRD_LOCK="$PWD/check-lock"
install -d -m 0700 "$FIREBIRD_LOCK"
"$FIREBIRD/bin/isql" -q -bail <<SQL
CREATE DATABASE '$PWD/check.fdb';
CREATE TABLE sample (amount INTEGER);
INSERT INTO sample VALUES (47);
INSERT INTO sample VALUES (64);
COMMIT;
SQL
"$FIREBIRD/bin/gbak" -backup "$PWD/check.fdb" "$PWD/check.fbk"
"$FIREBIRD/bin/gbak" -create "$PWD/check.fbk" "$PWD/restored.fdb"
printf 'SET HEADING OFF;
SELECT SUM(amount) FROM sample;
' | "$FIREBIRD/bin/isql" -q -bail "$PWD/restored.fdb" > query.out
grep -Eq '^[[:space:]]*111[[:space:]]*$' query.out

# Reject a previously registered difference file outside the database access list.
install -d -m 0700 check-allowed
"$FIREBIRD/bin/isql" -q -bail <<SQL
CREATE DATABASE '$PWD/check-allowed/restricted.fdb';
ALTER DATABASE ADD DIFFERENCE FILE '$PWD/outside.delta';
SQL
engine_root=$FIREBIRD
export FIREBIRD="$PWD/check-config"
install -d -m 0700 "$FIREBIRD"
printf 'Providers = Engine12\nDatabaseAccess = Restrict %s/check-allowed\n' "$PWD" > "$FIREBIRD/firebird.conf"
cat > "$FIREBIRD/plugins.conf" <<PLUGINS
Plugin = Engine12 {
    Module = $engine_root/plugins/Engine12
}
PLUGINS
# Firebird's bootstrap mode bypasses the access list for its build-time databases.
unset FIREBIRD_BOOT_BUILD
if printf 'ALTER DATABASE BEGIN BACKUP;\n' |
    "$engine_root/bin/isql" -q -bail -user SYSDBA "$PWD/check-allowed/restricted.fdb" > restricted.log 2>&1; then
    exit 1
fi
cat restricted.log
grep -F 'SQLSTATE = 28000' restricted.log
grep -Ei 'difference file.*(not allowed|denied)' restricted.log
test ! -e "$PWD/outside.delta"

%files
%doc README.md
%license doc/license/IDPL.txt builds/install/misc/IPLicense.txt BSD-crypt.txt BSD-SHA2.txt Spencer-LICENSE.txt
%dir %{_sysconfdir}/firebird
%config(noreplace) %{_sysconfdir}/firebird/*.conf
%{_bindir}/firebird-isql
%{_bindir}/gbak
%{_datadir}/firebird/
%{_libdir}/firebird/
%{_libdir}/libfbclient.so.*
%{_libdir}/libib_util.so

%files devel
%{_bindir}/fb_config
%{_includedir}/firebird/
%{_includedir}/ib_util.h
%{_includedir}/ibase.h
%{_includedir}/iberror.h
%{_libdir}/libfbclient.so

%changelog
%autochangelog
