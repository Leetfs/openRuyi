# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xml-commons-resolver
Version:        1.2
Release:        %autorelease
Summary:        Resolve XML catalog identifiers in Java
License:        Apache-2.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://xerces.apache.org/xml-commons/components/resolver/
VCS:            svn:https://svn.apache.org/repos/asf/xerces/xml-commons/
#!RemoteAsset:  sha256:55dbe7bd56452c175320ce9a97b752252c5537427221323c72e9b9c1ac221efe
Source0:        https://archive.apache.org/dist/xml/commons/binaries/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4

%description
The Apache resolver translates public identifiers, system identifiers
and URI references using XML Catalogs. It includes SAX and Java XML
transformation adapters for applications that resolve resources offline.

%prep
%autosetup
# The Apache distribution includes both the sources and a prebuilt resolver.
rm -f resolver.jar

%build
ant -nouserlib -f resolver.xml -Dant.build.javac.source=8 -Dant.build.javac.target=8 jar

%install
install -Dpm644 build/resolver.jar %{buildroot}%{_datadir}/java/xml-resolver.jar

%check
# Resolve upstream's catalog, including its delegated system catalog.
mkdir test-classes
cp=build/resolver.jar:%{_datadir}/java/junit4.jar
javac --release 8 -cp "$cp" -d test-classes src/org/apache/xml/resolver/tests/BasicResolverTests.java
java -Dxml.catalog.files="$PWD/src/org/apache/xml/resolver/tests/catalog.xml" -Dxml.catalog.ignoreMissing=true \
    -cp "test-classes:$cp" org.junit.runner.JUnitCore org.apache.xml.resolver.tests.BasicResolverTests

%files
%license LICENSE.resolver.txt NOTICE-resolver.txt
%doc docs/resolver.html
%{_datadir}/java/xml-resolver.jar

%changelog
%autochangelog
