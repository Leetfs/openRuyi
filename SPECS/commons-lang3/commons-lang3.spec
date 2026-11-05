# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/commons/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           commons-lang3
Version:        3.20.0
Release:        %autorelease
Summary:        Apache Commons utilities for Java core classes
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-lang/
VCS:            git:https://github.com/apache/commons-lang
#!RemoteAsset:  sha256:a567e0f07cd5535536851f389864dc84c11f9ea62a2eb3a24d94dee887f7b91e
Source0:        https://github.com/apache/commons-lang/archive/refs/tags/rel/commons-lang-%{version}.tar.gz
#!RemoteAsset:  sha256:e19bbe631ab9a3fa0d37827cc2bff17bb73a9135d327a68666d19232f7bf3c22
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/junit-pioneer/junit-pioneer/1.9.1/junit-pioneer-1.9.1-sources.jar
#!RemoteAsset:  sha256:5330c503e49a845407d48eccfa41bc4ba29eade6f60feb49a6212fb5f57abaa5
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-text/1.14.0/commons-text-1.14.0-sources.jar
Source3:        module-info.java
Patch0:         0001-make-time-zone-tests-deterministic.patch
Patch1:         0002-release-the-timer-after-testTryAcquire.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:) == 92
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  unzip
Provides:       mvn(org.apache.commons:%{name}) == %{version}
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 92

%description
Apache Commons Lang provides string, reflection, date, concurrency and
object utilities for Java, including the org.apache.commons.lang3 module.

%prep
%autosetup -p1 -n commons-lang-rel-commons-lang-%{version}
mkdir -p target/{pioneer,text,test-classes,classes,java9,manifest} .xmvn
unzip -q %{SOURCE1} -d target/pioneer
unzip -q %{SOURCE2} -d target/text
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF

%build
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -Xpkginfo:always -g -parameters -proc:none -encoding UTF-8 -d target/classes @target/sources
javac --release 9 --module-version %{version} --patch-module org.apache.commons.lang3=target/classes -d target/java9 %{SOURCE3}
meta=target/classes/META-INF/maven/org.apache.commons/%{name}
mkdir -p "$meta"
cp pom.xml "$meta/"
cp LICENSE.txt NOTICE.txt target/classes/META-INF/
printf 'artifactId=%%s\ngroupId=org.apache.commons\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cat > bundle.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version>
<build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>5.1.9.MBI</version><configuration><manifestLocation>$PWD/target/manifest</manifestLocation><instructions>
<Bundle-SymbolicName>org.apache.commons.lang3</Bundle-SymbolicName><Bundle-Name>Apache Commons Lang</Bundle-Name><Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor><Bundle-Version>%{version}</Bundle-Version>
<Export-Package>org.apache.commons.lang3.*;version=%{version};-noimport:=true</Export-Package><Automatic-Module-Name>org.apache.commons.lang3</Automatic-Module-Name><Multi-Release>true</Multi-Release>
</instructions></configuration></plugin></plugins></build></project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -f bundle.pom -Dmaven.repo.local="$PWD/target/repo" org.apache.felix:maven-bundle-plugin:5.1.9.MBI:manifest
jar cfm target/%{name}.jar target/manifest/MANIFEST.MF -C target/classes .
jar --update --file target/%{name}.jar --release 9 -C target/java9 module-info.class

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
cp="$PWD/target/%{name}.jar"
for dir in org/junit/platform org/junit/jupiter; do
    jars=$(find "%{repo}/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$cp:$jars"
done
for n in junit-jupiter-params univocity-parsers apiguardian-api opentest4j junit jsr305 easymock hamcrest-core byte-buddy byte-buddy-agent objenesis asm asm-commons asm-tree; do
    cp="$cp:%{bootstrap_java}/$n.jar"
done
# These two classes contain JMH microbenchmarks only.
find src/test/java -name '*.java' ! -name HashSetvBitSetTest.java ! -name StringUtilsIsMixedCaseTest.java | sort > target/test-sources
javac --release 17 -proc:none -encoding UTF-8 -g -sourcepath target/pioneer:target/text -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
tests=$(sed -n '/Test[.]java$/{s|src/test/java/||;s|[.]java$||;s|/|.|g;p;}' target/test-sources)
args=$(sed -n 's|.*<extraArgs>\(.*\)</extraArgs>.*|\1|p' pom.xml | grep -- '--add-opens' | head -1)
test -n "$args"
mkdir -p target/launcher
javac -proc:none -cp "$cp" -d target/launcher %{_libexecdir}/eclipse-equinox/RunJupiter.java
java $args -Xmx1024m -Dbasedir="$PWD" -cp "$PWD/target/launcher:$PWD/target/test-classes:$cp" RunJupiter $tests
java --module-path target/%{name}.jar --add-modules org.apache.commons.lang3 -version

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/commons-lang3.xml
%{artifact_dir}/

%changelog
%autochangelog
