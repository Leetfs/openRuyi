# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/codehaus/plexus/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           plexus-i18n
Version:        1.1.0
Release:        %autorelease
Summary:        Internationalization service for Plexus components
License:        Apache-2.0
URL:            https://codehaus-plexus.github.io/%{name}/
VCS:            git:https://github.com/codehaus-plexus/%{name}
#!RemoteAsset:  sha256:e0d570ca4ed179f1d0d09da0da2ad344e2d5538ff305006bfb7e1bb88783c757
Source0:        https://github.com/codehaus-plexus/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:4915a0a3683e9afad03db155ee85050396bbcdc240a83bf04aba58701b36d8ba
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/plexus/%{name}/%{version}/%{name}-%{version}.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source3:        IndexNative.java
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:) == 24
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
Provides:       mvn(org.codehaus.plexus:%{name}) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.codehaus.plexus:plexus:pom:) == 24

%description
Plexus I18N selects localized resource bundles and expands translated messages.

%prep
%autosetup -n %{name}-%{name}-%{version}
cp %{SOURCE2} LICENSE

%build
mkdir -p target/classes/META-INF/maven/org.codehaus.plexus/%{name} target/tools
cp=
for artifact in javax.inject org.eclipse.sisu.inject slf4j-api; do
    cp="$cp%{bootstrap_java}/$artifact.jar:"
done
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -g -proc:none -cp "$cp" -d target/classes @target/sources
index_cp="%{bootstrap_java}/org.eclipse.sisu.inject.jar:%{bootstrap_java}/javax.inject.jar:%{bootstrap_java}/guice.jar:%{bootstrap_java}/asm.jar"
javac -cp "$index_cp" -d target/tools %{SOURCE3}
java -cp "target/tools:target/classes:$index_cp:$cp" IndexNative target/classes
test -s target/classes/META-INF/sisu/javax.inject.Named
meta=target/classes/META-INF/maven/org.codehaus.plexus/%{name}
cp %{SOURCE1} "$meta/pom.xml"
printf 'groupId=org.codehaus.plexus\nartifactId=%%s\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE target/classes/META-INF/
jar cf target/%{name}.jar -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 %{SOURCE1} %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.codehaus.plexus</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.codehaus.plexus</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Run the original component tests with Sisu injection and their resource bundles.
mkdir -p target/test-classes
cp=$(find %{repo}/org/junit/jupiter %{repo}/org/junit/platform -name '*-5.12.2.jar' -o -name '*-1.12.2.jar' | paste -sd:)
cp="$PWD/target/%{name}.jar:$cp:%{repo}/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.jar:"
for artifact in org.eclipse.sisu.inject org.eclipse.sisu.plexus javax.inject guice guava aopalliance javax.annotation-api slf4j-api slf4j-simple plexus-utils plexus-xml plexus-classworlds plexus-container-default plexus-component-annotations apiguardian-api opentest4j failureaccess velocity-engine-core commons-lang3 commons-io asm asm-commons; do
    cp="$cp%{bootstrap_java}/$artifact.jar:"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -encoding UTF-8 -g -proc:none -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -cp "target/test-classes:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java $tests

%files
%license LICENSE
%doc README.md
%{_datadir}/maven-metadata/plexus-i18n.xml
%{artifact_dir}/

%changelog
%autochangelog
