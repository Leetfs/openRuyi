# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jetty
Version:        12.1.14
Release:        %autorelease
Summary:        Jetty HTTP server and Jakarta EE 10 servlet container
License:        EPL-2.0 OR Apache-2.0
URL:            https://jetty.org/
VCS:            git:https://github.com/jetty/jetty.project
#!RemoteAsset:  sha256:a122b1bd0c408ab17d7a5bad65608d92d675abf59a0607cdf3a550ccd6f8efac
Source0:        https://github.com/jetty/jetty.project/archive/refs/tags/jetty-%{version}.tar.gz?/jetty-%{version}.tar.gz
#!RemoteAsset:  sha256:508e0d8115002648b2ee9b66345bf82925c1ba922448c2ba2d409085926ad572
Source1:        https://github.com/jetty/jetty-test-helper/archive/refs/tags/jetty-test-helper-6.4.tar.gz?/jetty-test-helper-6.4.tar.gz
#!RemoteAsset:  sha256:970936de229c235f0fd93bf717c421fdb0731698681fe67e00e426697e337083
Source2:        https://github.com/awaitility/awaitility/archive/refs/tags/awaitility-4.3.0.tar.gz?/awaitility-4.3.0.tar.gz
#!RemoteAsset:  sha256:ebe70e2f96a3bc9b70eece33281a64d6cb3dbeed830a3690e0ea8a9d8dee5fee
Source3:        https://github.com/google/jimfs/archive/refs/tags/v1.3.1.tar.gz?/jimfs-1.3.1.tar.gz
#!RemoteAsset:  sha256:ece67aaeea60a2845010b301f1a4e5bcf9a91fda7594cf3599ad4c9501a29b2c
Source4:        https://maven-central.storage-download.googleapis.com/maven2/com/google/errorprone/error_prone_annotations/2.39.0/error_prone_annotations-2.39.0-sources.jar
#!RemoteAsset:  sha256:adf0898191d55937fb3192ba971826f4f294292c4a960740f3c27310e7b70296
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/jspecify/jspecify/1.0.0/jspecify-1.0.0-sources.jar
#!RemoteAsset:  sha256:371bc06d861278f8048157b5172fd5e830410cdd9cddf1cca02cd9ead7b64fff
Source6:        https://maven-central.storage-download.googleapis.com/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1-sources.jar
#!RemoteAsset:  sha256:2dd9da85182efca525aa269db573e0ed54943767d6af3afc50d0ede51e63d01a
Source7:        https://maven-central.storage-download.googleapis.com/maven2/com/ibm/icu/icu4j/77.1/icu4j-77.1-sources.jar
#!RemoteAsset:  sha256:743acc7bbee15cc835b2ceb98d96ba8d35a6ff35228a1a3291a3d033fbbbf4b1
Source8:        https://raw.githubusercontent.com/eclipse-tycho/tycho/14bb695163b412b2a18258983e535b831db4bf21/tycho-core/src/test/java/org/eclipse/tycho/test/util/HttpServer.java
#!RemoteAsset:  sha256:5af72f261dae28b833ce9c2f1edcd9b0debf476f986b1c27e6602ed4a7af7ec3
Source9:        https://raw.githubusercontent.com/eclipse-tycho/tycho/14bb695163b412b2a18258983e535b831db4bf21/tycho-core/src/test/java/org/eclipse/tycho/test/util/FileServerServlet.java
#!RemoteAsset:  sha256:8fde74d8db76d4d8ebeefb771cc606b5a9fff85a58576b4caf5874adf4314da8
Source10:       https://raw.githubusercontent.com/eclipse-tycho/tycho/14bb695163b412b2a18258983e535b831db4bf21/tycho-core/src/test/java/org/eclipse/tycho/test/util/AbstractMonitorServlet.java
Source11:       build-jetty.py
Source12:       check-jetty.sh
Source13:       TychoServerCompatibility.java
Source14:       OfflineHttpsSite.java
# Stabilize the four-thread tracking assertions on busy virtual-thread schedulers.
Patch1:         0001-Stabilize-virtual-thread-tracking-dump.patch
Patch2:         0002-Restore-four-thread-tracking-coverage.patch
Patch3:         0003-Enable-virtual-thread-tracking-dump.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  maven >= 3.9.9
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  mvn(com.fasterxml.jackson:jackson-bom:pom:) == 2.22.2
BuildRequires:  mvn(io.netty:netty-bom:pom:) == 4.2.18.Final
BuildRequires:  mvn(jakarta.platform:jakarta.jakartaee-bom:pom:) == 10.0.0
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api) == 6.0.0
BuildRequires:  mvn(org.apache.directory.api:api-parent:pom:) == 2.1.8
BuildRequires:  mvn(org.hibernate.search:hibernate-search-bom:pom:) == 8.4.0.Final
BuildRequires:  mvn(org.infinispan:infinispan-bom:pom:) == 16.2.3
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 6.1.3
BuildRequires:  mvn(org.ow2.asm:asm-bom:pom:) == 9.10.1
BuildRequires:  mvn(org.slf4j:slf4j-api) == 2.0.17
BuildRequires:  mvn(org.testcontainers:testcontainers-bom:pom:) == 2.0.5
Provides:       mvn(org.eclipse.jetty:jetty-util) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-jmx) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-io) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-http) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-server) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-security) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-session) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-util-ajax) == %{version}
Provides:       mvn(org.eclipse.jetty.ee10:jetty-ee10-servlet) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-project:pom:) == %{version}
Provides:       mvn(org.eclipse.jetty:jetty-core:pom:) == %{version}
Provides:       mvn(org.eclipse.jetty.ee10:jetty-ee10:pom:) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(com.fasterxml.jackson:jackson-bom:pom:) == 2.22.2
Requires:       mvn(io.netty:netty-bom:pom:) == 4.2.18.Final
Requires:       mvn(jakarta.platform:jakarta.jakartaee-bom:pom:) == 10.0.0
Requires:       mvn(jakarta.servlet:jakarta.servlet-api) == 6.0.0
Requires:       mvn(org.apache.directory.api:api-parent:pom:) == 2.1.8
Requires:       mvn(org.hibernate.search:hibernate-search-bom:pom:) == 8.4.0.Final
Requires:       mvn(org.infinispan:infinispan-bom:pom:) == 16.2.3
Requires:       mvn(org.junit:junit-bom:pom:) == 6.1.3
Requires:       mvn(org.ow2.asm:asm-bom:pom:) == 9.10.1
Requires:       mvn(org.slf4j:slf4j-api) == 2.0.17
Requires:       mvn(org.testcontainers:testcontainers-bom:pom:) == 2.0.5

%description
Jetty provides embeddable HTTP servers, network connectors, session and
security handlers, and a Jakarta Servlet 6.0 container for Java applications.

%prep
%autosetup -p1 -n jetty.project-jetty-%{version}
mkdir -p test-inputs/{helper,awaitility,jimfs,error-prone,jspecify,auto-service,icu4j,tycho}
tar xf %{SOURCE1} --strip-components=1 -C test-inputs/helper
tar xf %{SOURCE2} --strip-components=1 -C test-inputs/awaitility
tar xf %{SOURCE3} --strip-components=1 -C test-inputs/jimfs
# Compile only the named packages of these source-only test dependencies.
unzip -q %{SOURCE4} 'com/*' -d test-inputs/error-prone
unzip -q %{SOURCE5} 'org/*' -d test-inputs/jspecify
unzip -q %{SOURCE6} 'com/*' -d test-inputs/auto-service
unzip -q %{SOURCE7} 'com/*' -d test-inputs/icu4j
install -m644 %{SOURCE8} %{SOURCE9} %{SOURCE10} test-inputs/tycho/

%build
python3 %{SOURCE11} "$PWD" "$PWD/build/bundles"

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} jetty-models pom.xml jetty-core/pom.xml jetty-ee10/pom.xml
for name in jetty-util jetty-jmx jetty-io jetty-http jetty-server jetty-security jetty-session jetty-util-ajax jetty-ee10-servlet; do
    dir=jetty-core/$name
    if test "$name" = jetty-ee10-servlet; then dir=jetty-ee10/$name; fi
    symbolic=org.eclipse.${name//-/.}
    %{_libexecdir}/eclipse-equinox/install-bundles --symbolic-name "$symbolic" %{buildroot} %{_datadir} "$name" build/bundles "$dir/pom.xml"
done

%check
bash %{SOURCE12} %{buildroot} %{SOURCE13} %{SOURCE14}

%files
%license LICENSE NOTICE.txt
%{_datadir}/maven-metadata/jetty-*.xml
%{_datadir}/maven-repository/org/eclipse/jetty/jetty-*/
%{_datadir}/maven-repository/org/eclipse/jetty/ee10/jetty-*/

%changelog
%autochangelog
