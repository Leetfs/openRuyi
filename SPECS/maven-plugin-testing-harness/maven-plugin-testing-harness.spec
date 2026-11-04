# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global group_dir %{repo}/org/apache/maven/plugin-testing
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           maven-plugin-testing-harness
Version:        3.5.1
Release:        %autorelease
Summary:        Test harness for Maven plugin goals
License:        Apache-2.0
URL:            https://maven.apache.org/plugin-testing/maven-plugin-testing-harness/
VCS:            git:https://github.com/apache/maven-plugin-testing
#!RemoteAsset:  sha256:9dbcd4e71090416b5cf3d038faa2d8e830eaef34ee14a2bc6d5d69f56ab8856d
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugin-testing/maven-plugin-testing/%{version}/maven-plugin-testing-%{version}-source-release.zip
Patch0:         0001-resolve-the-test-artifact-from-a-file-repository.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  maven >= 3.9.12
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 47
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine) == 5.12.2
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.plugin-testing:maven-plugin-testing:pom:) == %{version}
Provides:       mvn(org.apache.maven.plugin-testing:%{name}) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.12
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 47
Requires:       mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
Requires:       mvn(org.mockito:mockito-core) == 4.11.0

%description
Maven Plugin Testing Harness configures plugin goals from a test POM,
injects Maven components, and runs plugin tests with JUnit.

%prep
%autosetup -p1 -n maven-plugin-testing-%{version}

%build
cd %{name}
mkdir -p target/classes/META-INF/maven/org.apache.maven.plugin-testing/%{name}
cp="%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*"
for dir in org/codehaus/plexus/plexus-testing org/mockito org/junit/platform org/junit/jupiter org/junit/vintage; do
    jars=$(find "%{repo}/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$jars$cp"
done
for n in maven-plugin-annotations plexus-archiver plexus-io plexus-build-api0 commons-io commons-compress commons-lang3 commons-codec xz apiguardian-api opentest4j junit junit-jupiter-params hamcrest-core byte-buddy byte-buddy-agent objenesis asm asm-commons asm-tree; do
    cp="$cp:%{bootstrap_java}/$n.jar"
done
printf '%%s\n' "$cp" > target/classpath
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
cp ../LICENSE ../NOTICE target/classes/META-INF/
meta=target/classes/META-INF/maven/org.apache.maven.plugin-testing/%{name}
cp pom.xml "$meta/"
printf 'artifactId=%%s\ngroupId=org.apache.maven.plugin-testing\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
printf 'Specification-Title: Maven Plugin Testing Mechanism\nSpecification-Version: 3.5\nSpecification-Vendor: The Apache Software Foundation\nImplementation-Title: Maven Plugin Testing Mechanism\nImplementation-Version: %%s\nImplementation-Vendor: The Apache Software Foundation\n' '%{version}' > target/module.mf
jar cfm target/%{name}.jar target/module.mf -C target/classes .

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-parent pom.xml
path=%{group_dir}/%{name}/%{version}/%{name}-%{version}
mkdir -p "%{buildroot}$(dirname "$path")"
install -m644 %{name}/target/%{name}.jar "%{buildroot}$path.jar"
install -m644 %{name}/pom.xml "%{buildroot}$path.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.plugin-testing</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>$path.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.plugin-testing</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>$path.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
cd %{name}
mkdir -p target/test-classes
cp="$PWD/target/%{name}.jar:$(cat target/classpath)"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -DtestRepository=%{buildroot}%{repo} -Dbasedir="$PWD" -cp "target/test-classes:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java $tests

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-plugin-testing-harness*.xml
%{group_dir}/maven-plugin-testing/
%{group_dir}/maven-plugin-testing-harness/

%changelog
%autochangelog
