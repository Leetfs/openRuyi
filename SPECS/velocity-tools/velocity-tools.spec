# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/velocity/tools/velocity-tools-generic/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           velocity-tools
Version:        3.1
Release:        %autorelease
Summary:        General-purpose tools for Velocity templates
License:        Apache-2.0
URL:            https://velocity.apache.org/tools/
VCS:            git:https://github.com/apache/velocity-tools
#!RemoteAsset:  sha256:334b4a81808a09beda5b2e6ca56aa76cb33d599ebde8cd400d684a8cf9fe1f1a
Source0:        https://github.com/apache/velocity-tools/archive/refs/tags/%{version}.tar.gz?/velocity-tools-%{version}.tar.gz
#!RemoteAsset:  sha256:7a2ac73c90dd104b5a07e6e2cd03e95ec28d29f3b8304f3dd7fffcecb049712e
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/velocity/velocity-master/4/velocity-master-4.pom
Source2:        RunJUnit.java
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache:apache:pom:) == 23
BuildRequires:  mvn(org.apache.commons:commons-digester3) == 3.2
BuildRequires:  mvn(org.apache.commons:commons-lang3) == 3.20.0
BuildRequires:  mvn(com.github.cliftonlabs:json-simple) == 3.0.2
Provides:       mvn(org.apache.velocity.tools:velocity-tools-generic) == %{version}
Provides:       mvn(org.apache.velocity.tools:velocity-tools-parent:pom:) == %{version}
Provides:       mvn(org.apache.velocity:velocity-master:pom:) == 4
Requires:       javapackages-bootstrap
Requires:       mvn(org.apache:apache:pom:) == 23
Requires:       mvn(org.apache.commons:commons-digester3) == 3.2
Requires:       mvn(org.apache.commons:commons-lang3) == 3.20.0
Requires:       mvn(com.github.cliftonlabs:json-simple) == 3.0.2

%description
Velocity Tools provides formatting, escaping, collection, XML and JSON
utilities for templates, together with configurable toolboxes.

%prep
%autosetup -n velocity-tools-%{version}

%build
cd velocity-tools-generic
mkdir -p target/classes/META-INF/maven/org.apache.velocity.tools/velocity-tools-generic
cp="%{repo}/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.jar:%{repo}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar:%{repo}/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.jar:%{repo}/cglib/cglib/3.2.9/cglib-3.2.9.jar:%{bootstrap_java}/*"
printf '%%s\n' "$cp" > target/classpath
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/classes @target/sources
cp -r src/main/resources/. target/classes/
meta=target/classes/META-INF/maven/org.apache.velocity.tools/velocity-tools-generic
cp pom.xml "$meta/"
printf 'groupId=org.apache.velocity.tools\nartifactId=velocity-tools-generic\nversion=%%s\n' '%{version}' > "$meta/pom.properties"
cp ../LICENSE ../NOTICE target/classes/META-INF/
jar cf target/velocity-tools-generic.jar -C target/classes .

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models pom.xml %{SOURCE1}
mkdir -p %{buildroot}%{artifact_dir}
install -m644 velocity-tools-generic/target/velocity-tools-generic.jar %{buildroot}%{artifact_dir}/velocity-tools-generic-%{version}.jar
install -m644 velocity-tools-generic/pom.xml %{buildroot}%{artifact_dir}/velocity-tools-generic-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.velocity.tools</groupId><artifactId>velocity-tools-generic</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/velocity-tools-generic-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.velocity.tools</groupId><artifactId>velocity-tools-generic</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/velocity-tools-generic-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Run the original generic tool, template and toolbox configuration tests.
cd velocity-tools-generic
mkdir -p target/test-classes target/launcher
cp="target/velocity-tools-generic.jar:$(cat target/classpath)"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
javac -cp "$cp" -d target/launcher %{SOURCE2}
tests=$(find src/test/java -name '*Tests.java' -o -name '*TestCase.java' -o -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -Dbasedir="$PWD" -cp "target/launcher:target/test-classes:$cp" RunJUnit $tests

%files
%license LICENSE NOTICE
%doc README.md
%{_datadir}/maven-metadata/velocity-tools.xml
%{_datadir}/maven-metadata/velocity-tools-models.xml
%{artifact_dir}/
%{repo}/org/apache/velocity/tools/velocity-tools-parent/%{version}/
%{repo}/org/apache/velocity/velocity-master/4/

%changelog
%autochangelog
