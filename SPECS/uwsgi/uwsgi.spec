# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           uwsgi
Version:        2.0.31
Release:        %autorelease
Summary:        Application server with Python WSGI support
License:        GPL-2.0-or-later WITH GCC-exception-2.0
URL:            https://uwsgi-docs.readthedocs.io/en/latest/
VCS:            git:https://github.com/unbit/uwsgi
#!RemoteAsset:  sha256:e8f8b350ccc106ff93a65247b9136f529c14bf96b936ac5b264c6ff9d0c76257
Source0:        https://files.pythonhosted.org/packages/source/u/%{name}/%{name}-%{version}.tar.gz
Source1:        openruyi.ini
Source2:        uwsgi.1
BuildSystem:    autotools

BuildOption(build):  PYTHON=%{__python3}
BuildOption(build):  PROFILE=openruyi
BuildOption(build):  CC=%{__cc}
BuildOption(build):  CFLAGS="%{build_cflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(build):  CPUCOUNT=%{_smp_build_ncpus}

BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python-rpm-macros
BuildRequires:  python3dist(requests)

%description
uWSGI is an application server with an embedded Python WSGI plugin, an
HTTP server, process management, caching, and request routing. It can serve
Python web applications directly or behind a web server using the uwsgi
protocol. The Python decorators module is included for applications running
inside uWSGI.

%prep -a
cp %{SOURCE1} buildconf/openruyi.ini
sed -i 's|@PLUGINDIR@|%{_libdir}/%{name}|' buildconf/openruyi.ini

# Upstream configures the build through profiles instead of configure.
%conf

# The upstream Makefile has no install target.
%install
install -Dpm0755 uwsgi %{buildroot}%{_bindir}/uwsgi
install -Dpm0644 uwsgidecorators.py %{buildroot}%{python3_sitelib}/uwsgidecorators.py
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}
install -Dpm0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/uwsgi.1

# The Makefile's check target runs cppcheck; integration and C tests have
# separate entry points. Only the embedded Python plugin is under test.
%check
%set_build_flags
export CPUCOUNT=%{_smp_build_ncpus}
UWSGI_PLUGINS_TEST=python %{__python3} t/runner -v
%{__python3} uwsgiconfig.py --build unittest
%make_build -C unittest
cd unittest
./check_core
./check_regexp

%files
%doc README CONTRIBUTORS
%license LICENSE
%{_bindir}/uwsgi
%{python3_sitelib}/uwsgidecorators.py
%{python3_sitelib}/__pycache__/uwsgidecorators.*.pyc
%{_mandir}/man1/uwsgi.1*

%changelog
%autochangelog
