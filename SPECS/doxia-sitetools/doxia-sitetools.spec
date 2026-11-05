# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global doxia_repo %{repo}/org/apache/maven/doxia

Name:           doxia-sitetools
Version:        2.0.0
Release:        %autorelease
Summary:        Maven site models and report rendering tools
License:        Apache-2.0
URL:            https://maven.apache.org/doxia/doxia-sitetools/
VCS:            git:https://github.com/apache/maven-doxia-sitetools
#!RemoteAsset:  sha256:97e7d88575b0918ed257c4e25be274d430e8573d3b92b38a1f4378bc19bbc085
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-sitetools-%{version}-source-release.zip
Source1:        IndexNative.java
Source2:        build-sitetools.py
Source3:        check-sitetools.py
Source4:        generate-model.py
Source5:        build-htmlunit-fixtures.py
#!RemoteAsset:  sha256:baec79d3e7c2c38709e0354fca6d7ad4b1db92b20e52aaf434af75cee2a79a74
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/htmlunit/htmlunit/4.4.0/htmlunit-4.4.0-sources.jar
#!RemoteAsset:  sha256:396abdec68dae0c18362e059bbc31fdd01f19d4865ca561d603ed13b84279e73
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/htmlunit/htmlunit-core-js/4.4.0/htmlunit-core-js-4.4.0-sources.jar
#!RemoteAsset:  sha256:0781755f7a520e65a6e93b4ed01130262046b46441f46f39a95910608efbf44c
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/htmlunit/neko-htmlunit/4.4.0/neko-htmlunit-4.4.0-sources.jar
#!RemoteAsset:  sha256:fed57542f78cafdc32855055305389d4906128da16869e3ab2c7a4f4dd230a9d
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/htmlunit/htmlunit-cssparser/4.4.0/htmlunit-cssparser-4.4.0-sources.jar
#!RemoteAsset:  sha256:ea7623c3fc7484597c757096cc70cd92d41b790796abf3142d2be78738ce0321
Source10:       https://maven-central.storage-download.googleapis.com/maven2/org/htmlunit/htmlunit-xpath/4.4.0/htmlunit-xpath-4.4.0-sources.jar
#!RemoteAsset:  sha256:59df612ef9a003e3fa46acfd69632956f871efdf1101beaf8f076d4c5fc534b8
Source11:       https://maven-central.storage-download.googleapis.com/maven2/org/htmlunit/htmlunit-csp/4.4.0/htmlunit-csp-4.4.0-sources.jar
#!RemoteAsset:  sha256:064ac1e41f475c1fd0479b6505f44b6e3bb044b948bddc75d56a496ebb85fbc3
Source12:       https://maven-central.storage-download.googleapis.com/maven2/org/brotli/dec/0.1.2/dec-0.1.2-sources.jar
#!RemoteAsset:  sha256:9b8c59ecd259d16a026945abb5c2a82f403b6c3dcc1588dbc2532f2cd5d4e83d
Source13:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/httpcomponents/httpmime/4.5.14/httpmime-4.5.14-sources.jar
#!RemoteAsset:  sha256:3c531edfc074e3e0885e5d4a777a9e7317e108028be50ef6e893a5a9cf3e12c2
Source14:       https://maven-central.storage-download.googleapis.com/maven2/xerces/xercesImpl/2.12.2/xercesImpl-2.12.2-sources.jar
#!RemoteAsset:  sha256:2017bf4995644d73ff62f75109d9f9932609ae20e9a33ae1efb78e8af8b744cd
Source15:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/jetty-util/9.4.55.v20240627/jetty-util-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:92609e874be17a90eb4a4fcdc69cd76910a80236920cec44da6eaa9f6b101538
Source16:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/jetty-io/9.4.55.v20240627/jetty-io-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:7ca2d82c5c6c20bd8f2ef57d770384be37fe325696f8a26e4fefb8f329eacfb6
Source17:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/jetty-http/9.4.55.v20240627/jetty-http-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:59542512e200fa093e8e3d4152a59317ffb153d0e94b2e45105117199efe2303
Source18:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/jetty-xml/9.4.55.v20240627/jetty-xml-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:217aee7b6bb49cb13159229fa6072b87642813fbcee4e0eeae08fcf91e753273
Source19:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/jetty-client/9.4.55.v20240627/jetty-client-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:3f23ae663646b6950f12c2733147e3a2e6962232794c445fb3227494fc914ac9
Source20:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/websocket/websocket-api/9.4.55.v20240627/websocket-api-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:d83249d0bc3da53f18b5a67442b270d3dff7e7755d76b7f3bf2fb7b588a00895
Source21:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/websocket/websocket-common/9.4.55.v20240627/websocket-common-9.4.55.v20240627-sources.jar
#!RemoteAsset:  sha256:02a85c31b5efb05aa84dbdc55d78dcccdf562594e068ced9e965fbf9afc29fae
Source22:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jetty/websocket/websocket-client/9.4.55.v20240627/websocket-client-9.4.55.v20240627-sources.jar
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  maven >= 3.9.16
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core) == 2.0.0
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core:jar:tests) == 2.0.0
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api) == 4.0.0
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 43
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n) == 1.1.0
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity) == 2.2.0
BuildRequires:  mvn(org.apache.velocity.tools:velocity-tools-generic) == 3.1
BuildRequires:  mvn(org.apache.commons:commons-lang3) == 3.20.0
BuildRequires:  mvn(org.apache.commons:commons-text) == 1.12.0
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  mvn(commons-net:commons-net) == 3.13.0
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  mvn(org.ow2.asm:asm) == 9.10.1
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.doxia:doxia-sitetools:pom:) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-site-model) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-skin-model) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-integration-tools) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-site-renderer) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.16
Requires:       mvn(org.apache.maven.doxia:doxia-core) == 2.0.0
Requires:       mvn(org.apache.maven.reporting:maven-reporting-api) == 4.0.0
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 43
Requires:       mvn(org.codehaus.plexus:plexus-i18n) == 1.1.0
Requires:       mvn(org.codehaus.plexus:plexus-velocity) == 2.2.0
Requires:       mvn(org.apache.velocity.tools:velocity-tools-generic) == 3.1
Requires:       mvn(org.apache.commons:commons-lang3) == 3.20.0
Requires:       mvn(org.apache.commons:commons-text) == 1.12.0
Requires:       mvn(commons-io:commons-io) == 2.21.0

%description
Doxia Site Tools provides site and skin descriptor models, Maven integration,
and document rendering for Maven reports.

%prep
%autosetup -n doxia-sitetools-%{version}

%build
%{python3} %{SOURCE2} %{version} %{SOURCE1} %{SOURCE4}

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models pom.xml
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
echo '<metadata><artifacts>' > "$metadata"
for artifact in doxia-site-model doxia-skin-model doxia-integration-tools doxia-site-renderer; do
    destination=%{doxia_repo}/$artifact/%{version}
    mkdir -p "%{buildroot}$destination"
    install -m644 "$artifact/target/$artifact.jar" "%{buildroot}$destination/$artifact-%{version}.jar"
    install -m644 "$artifact/pom.xml" "%{buildroot}$destination/$artifact-%{version}.pom"
    cat >> "$metadata" <<EOF
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>$artifact</artifactId><version>%{version}</version><extension>jar</extension><path>$destination/$artifact-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>$artifact</artifactId><version>%{version}</version><extension>pom</extension><path>$destination/$artifact-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
EOF
done
echo '</artifacts></metadata>' >> "$metadata"

%check
# Build HtmlUnit and its browser libraries from source, then run the original
# descriptor, Maven integration, HTML DOM and JavaScript rendering tests.
%{python3} %{SOURCE3} %{SOURCE5} %{_sourcedir}

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/doxia-sitetools.xml
%{_datadir}/maven-metadata/doxia-sitetools-models.xml
%{doxia_repo}/doxia-sitetools/%{version}/
%{doxia_repo}/doxia-site-model/%{version}/
%{doxia_repo}/doxia-skin-model/%{version}/
%{doxia_repo}/doxia-integration-tools/%{version}/
%{doxia_repo}/doxia-site-renderer/%{version}/

%changelog
%autochangelog
