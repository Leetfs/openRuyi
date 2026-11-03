# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond krun 0
%bcond wasm 0
%bcond criu 0
%bcond system_yajl 0

Name:           crun
Version:        1.30.1
Release:        %autorelease
Summary:        OCI runtime written in C
License:        GPL-2.0-only
URL:            https://github.com/containers/crun
#!RemoteAsset:  sha256:99d036d95113552b6df66c7c879432835504bf0e525fc0372745071df129527b
Source0:        https://github.com/containers/crun/releases/download/%{version}/crun-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
%if %{with krun}
BuildOption(conf):  --with-libkrun
%endif
%if %{with wasm}
BuildOption(conf):  --with-wasmedge
%endif
%if %{with criu}
BuildOption(conf):  --enable-criu
%else
BuildOption(conf):  --disable-criu
%endif
%if %{without system_yajl}
BuildOption(conf):  --enable-embedded-yajl
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c) >= 0.14
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  python3-libmount
BuildRequires:  python3
%if %{with system_yajl}
BuildRequires:  pkgconfig(yajl)
%endif
%if %{with krun}
BuildRequires:  pkgconfig(libkrun)
%endif
%if %{with wasm}
BuildRequires:  wasmedge-devel
%endif
%if %{with criu}
BuildRequires:  pkgconfig(criu)
BuildRequires:  pkgconfig(libprotobuf-c)
%endif

Provides:       oci-runtime

%description
crun is a fast and low-memory OCI Container Runtime written in C.

%conf -p
./autogen.sh

%install -a
rm -rf %{buildroot}%{_libdir}/*.a

%check
# The OCI integration tests create container namespaces and mount cgroups;
# the OBS build environment does not provide that runtime setup.

%files
%license COPYING
%{_bindir}/crun
%{_mandir}/man1/crun.1*
%if %{with krun}
%{_bindir}/krun
%{_mandir}/man1/krun.1*
%endif
%if %{with wasm}
%{_bindir}/crun-wasm
%endif

%changelog
%autochangelog
