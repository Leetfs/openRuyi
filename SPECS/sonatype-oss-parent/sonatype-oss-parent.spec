# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global parent_dir %{_datadir}/maven-repository/org/sonatype/oss/oss-parent

Name:           sonatype-oss-parent
Version:        7
Release:        %autorelease
Summary:        Maven parent POM for projects using Sonatype OSS hosting
License:        Apache-2.0
URL:            https://central.sonatype.com/artifact/org.sonatype.oss/oss-parent
#!RemoteAsset:  sha256:b51f8867c92b6a722499557fc3a1fdea77bdf9ef574722fe90ce436a29559454
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/sonatype/oss/oss-parent/%{version}/oss-parent-%{version}.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
#!RemoteAsset:  sha256:1678d4120a585d8a630131aeec4c524d928398583b7eab616ee7d5a87f520d3d
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/sonatype/oss/oss-parent/5/oss-parent-5.pom
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
Provides:       mvn(org.sonatype.oss:oss-parent:pom) == %{version}
Provides:       mvn(org.sonatype.oss:oss-parent:pom) == 5

%description
This Maven parent POM defines plugin configuration, project encoding and
release profiles inherited by projects published through Sonatype OSS
repository hosting.

%prep
%setup -q -c -T
cp -p %{SOURCE1} LICENSE

%install
install -Dm644 %{SOURCE0} %{buildroot}%{parent_dir}/%{version}/oss-parent-%{version}.pom
install -Dm644 %{SOURCE2} %{buildroot}%{parent_dir}/5/oss-parent-5.pom
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
install -d "$(dirname "$metadata")"
echo '<metadata><artifacts>' > "$metadata"
for v in 5 %{version}; do
    cat >> "$metadata" <<EOF
<artifact><groupId>org.sonatype.oss</groupId><artifactId>oss-parent</artifactId>
  <extension>pom</extension><version>$v</version><path>%{parent_dir}/$v/oss-parent-$v.pom</path>
  <compatVersions><version>$v</version></compatVersions>
  <properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
EOF
done
echo '</artifacts></metadata>' >> "$metadata"

%check
mkdir -p .xmvn src/main/resources
sed 's|<path>/usr/share/|<path>%{buildroot}/usr/share/|g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > .xmvn/parent.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$PWD/.xmvn/parent.xml</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
for v in 5 %{version}; do
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><parent>
  <groupId>org.sonatype.oss</groupId><artifactId>oss-parent</artifactId><version>$v</version><relativePath/>
</parent><artifactId>inheritance-check</artifactId><version>1</version>
<build><resources><resource><directory>src/main/resources</directory><filtering>true</filtering></resource></resources></build></project>
EOF
echo '${sonatypeOssDistMgmtSnapshotsUrl}' > src/main/resources/inherited-url
%{_libexecdir}/javapackages-bootstrap/mvn --offline --batch-mode -X -Dxmvn.debug=true -Dmaven.repo.local="$PWD/local-repository-$v" \
    org.apache.maven.plugins:maven-resources-plugin:resources > "resolution-$v.log" 2>&1 || { tail -40 "resolution-$v.log"; exit 1; }
grep -F "%{buildroot}%{parent_dir}/$v/oss-parent-$v.pom" "resolution-$v.log" > /dev/null
grep -Fx 'https://oss.sonatype.org/content/repositories/snapshots/' target/classes/inherited-url
done

%files
%license LICENSE
%{_datadir}/maven-metadata/sonatype-oss-parent.xml
%{parent_dir}/

%changelog
%autochangelog
