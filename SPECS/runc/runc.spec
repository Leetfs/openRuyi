# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Ruoqing He <heruoqing@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0

%define _name           runc
%define go_import_path  github.com/opencontainers/runc
# We don't have network access - 251
#global go_test_ignore_failure 1

Name:           runc
Version:        1.4.3
Release:        %autorelease
Summary:        CLI for running Open Containers
License:        Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT
URL:            https://github.com/opencontainers/runc
#!RemoteAsset:  sha256:e0a89f9e883ce93e740d14bb105b25c665f7d7beade4cfd0714fcafb38855d35
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  go-md2man
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)

Provides:       oci-runtime

%description
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

%prep -a
sed -i 's/ -trimpath//g' Makefile

%build
%set_build_flags
export CGO_CFLAGS=$CFLAGS
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif

mkdir -p GOPATH
pushd GOPATH
    mkdir -p src/%{provider}.%{provider_tld}/%{project}
    ln -s $(dirs +1 -l) src/%{import_path}
popd

pushd GOPATH/src/%{import_path}
export GOPATH=$(pwd)/GOPATH

%make_build runc

sed -i '/\#\!\/bin\/bash/d' contrib/completions/bash/%{name}

%install -a
# generate man pages
man/md2man-all.sh
# install man pages & bash completion
DESTDIR=%{buildroot} PREFIX=%{_prefix} %{__make} install-man install-bash

# TODO: fix this later because right now our macros kinda broken - 251
%check

%files
%license LICENSE vendor/modules.txt
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}*
%{bash_completions_dir}/%{name}

%changelog
%autochangelog
