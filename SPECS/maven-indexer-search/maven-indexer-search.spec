# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global group_dir %{repo}/org/apache/maven/indexer
Name:           maven-indexer-search
Version:        7.1.6
Release:        %autorelease
Summary:        Maven repository search API and Solr search backend
License:        Apache-2.0
URL:            https://maven.apache.org/maven-indexer/
VCS:            git:https://github.com/apache/maven-indexer
#!RemoteAsset:  sha256:c84bbf2df17c01c43b1009378d7d28d60f8df4a07b0eab1b1425bf8428eb7297
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/indexer/maven-indexer/%{version}/maven-indexer-%{version}-source-release.zip
Source1:        SearchCoordinates.java
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 44
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.indexer:maven-indexer:pom:) == %{version}
Provides:       mvn(org.apache.maven.indexer:search-api) == %{version}
Provides:       mvn(org.apache.maven.indexer:search-backend-smo) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 44

%description
Maven Search API describes repository queries and artifact coordinates.
The SMO backend searches Solr-compatible Maven repositories by checksum,
group, artifact and version.

%prep
%autosetup -n maven-indexer-%{version}

%build
mkdir -p build/bundles
cp=%{_datadir}/java/javapackages-bootstrap/gson.jar
for n in search-api search-backend-smo; do
    out="$PWD/build/$n"; mkdir -p "$out/META-INF/maven/org.apache.maven.indexer/$n"
    find "$n/src/main/java" -name '*.java' | sort > "build/$n.sources"
    javac --release 11 -g -encoding UTF-8 -proc:none -cp "$cp" -d "$out" @"build/$n.sources"
    if test "$n" = search-backend-smo; then
        properties="$out/org/apache/maven/search/backend/smo/internal/smo-version.properties"
        printf 'version=%%s\n' '%{version}' > "$properties"
    fi
    cp LICENSE NOTICE "$out/META-INF/"
    meta="$out/META-INF/maven/org.apache.maven.indexer/$n"; cp "$n/pom.xml" "$meta/"
    printf 'artifactId=%%s\ngroupId=org.apache.maven.indexer\nversion=%%s\n' "$n" '%{version}' > "$meta/pom.properties"
    title=$(sed -n 's/.*<name>\(Maven :: Search API[^<]*\)<\/name>.*/\1/p' "$n/pom.xml" | head -1)
    test -n "$title"
    printf 'Specification-Title: %%s\nSpecification-Version: 7.1\nSpecification-Vendor: The Apache Software Foundation\nImplementation-Title: %%s\nImplementation-Version: %%s\nImplementation-Vendor: The Apache Software Foundation\n' "$title" "$title" '%{version}' > build/module.mf
    jar cfm "build/bundles/$n.jar" build/module.mf -C "$out" .
    cp="$PWD/build/bundles/$n.jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-parent pom.xml
index=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
echo '<metadata><artifacts>' > "$index"
for n in search-api search-backend-smo; do
    path=%{group_dir}/$n/%{version}/$n-%{version}; mkdir -p "%{buildroot}$(dirname "$path")"
    install -m644 "build/bundles/$n.jar" "%{buildroot}$path.jar"
    install -m644 "$n/pom.xml" "%{buildroot}$path.pom"
    for ext in jar pom; do
        printf '<artifact><groupId>org.apache.maven.indexer</groupId><artifactId>%%s</artifactId><version>%%s</version><extension>%%s</extension><path>%%s.%%s</path>' "$n" '%{version}' "$ext" "$path" "$ext" >> "$index"
        echo '<compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions>' >> "$index"
        if test "$ext" = pom; then echo '<properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties>' >> "$index"; fi
        echo '</artifact>' >> "$index"
    done
done
echo '</artifacts></metadata>' >> "$index"

%check
# The upstream SMO showcase is explicitly ignored and contacts the public Maven Central service.
# Test the SHA-1 lookup through the production HTTP transport against a local Solr endpoint.
cp=$(cat build/classpath)
java -cp "$cp" %{SOURCE1}

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-indexer-search*.xml
%{group_dir}/maven-indexer/
%{group_dir}/search-api/
%{group_dir}/search-backend-smo/

%changelog
%autochangelog
