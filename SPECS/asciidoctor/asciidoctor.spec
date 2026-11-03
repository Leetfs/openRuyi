# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           asciidoctor
Version:        2.0.26
Release:        %autorelease
Summary:        AsciiDoc processor and publishing toolchain
License:        MIT
URL:            https://asciidoctor.org/
VCS:            git:https://github.com/asciidoctor/asciidoctor
#!RemoteAsset:  sha256:25c22b934bc0ae2448f2d73d4b2eba0c59e0521cf5e893fb0b0ad54a461bf066
Source0:        https://github.com/asciidoctor/asciidoctor/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  rubygems
Requires:       rubygems

%description
Asciidoctor converts AsciiDoc documents to HTML, DocBook and manual pages.
It provides a command-line processor and an API for Ruby applications.

%prep
%autosetup

%build
gem build %{name}.gemspec

%install
gemdir=$(ruby -rrubygems -e 'print Gem.default_dir')
gem install --local --ignore-dependencies --no-document --env-shebang \
    --install-dir "%{buildroot}$gemdir" --bindir %{buildroot}%{_bindir} %{name}-%{version}.gem
rm -f "%{buildroot}$gemdir/cache/%{name}-%{version}.gem"
install -Dm644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
printf '%%s\n' "$gemdir/gems/%{name}-%{version}" \
    "$gemdir/specifications/%{name}-%{version}.gemspec" > gem-files.list

%check
# The upstream test harness imports Nokogiri and Rouge. Exercise the shipped
# manual and HTML backends against the upstream manual and README.
ruby -Ilib bin/%{name} -b manpage -o generated.1 man/%{name}.adoc
grep -F '.TH "ASCIIDOCTOR"' generated.1
ruby -Ilib bin/%{name} -o readme.html README.adoc
grep -F '<html' readme.html

%files -f gem-files.list
%doc README.adoc CHANGELOG.adoc
%license LICENSE
%{_bindir}/asciidoctor
%{_mandir}/man1/asciidoctor.1*

%changelog
%autochangelog
