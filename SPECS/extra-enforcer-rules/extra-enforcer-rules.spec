# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global artifact_dir %{repo_dir}/org/codehaus/mojo/%{name}/%{version}

Name:           extra-enforcer-rules
Version:        1.11.0
Release:        %autorelease
Summary:        Additional dependency and bytecode checks for the Maven Enforcer plugin
License:        Apache-2.0 AND BSD-2-Clause-Darwin
URL:            https://www.mojohaus.org/extra-enforcer-rules/
VCS:            git:https://github.com/mojohaus/extra-enforcer-rules
#!RemoteAsset:  sha256:26d24f71a5b6858f926e83ed0cc1b328a763239763c15c5a721d24e55919b6a0
Source0:        https://github.com/mojohaus/extra-enforcer-rules/archive/refs/tags/%{version}.tar.gz?/extra-enforcer-rules-%{version}.tar.gz
# FileEncoding is a Java port of the file project's encoding.c.
#!RemoteAsset:  sha256:0505949dcf6041661d5fd7a6fb4f910c87621c68b4fbe40a79517cda3f640158
Source1:        https://raw.githubusercontent.com/file/file/b310a0c2d3e4a1c12d579ad5c0266f1092a91340/src/encoding.c
Source2:        check-bytecode.sh
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-api) == 3.6.2
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:) == 94
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
Provides:       mvn(org.codehaus.mojo:extra-enforcer-rules) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.apache.maven.enforcer:enforcer-api) == 3.6.2
Requires:       mvn(org.codehaus.mojo:mojo-parent:pom:) == 94

%description
These Maven Enforcer rules check bytecode targets, duplicate classes,
dependency scopes, character encodings and project metadata.

%prep
%autosetup
sed -n '1,/^ [*]\//p' %{SOURCE1} > file-encoding-notice.txt
file=src/main/java/org/freebsd/file/FileEncoding.java
cat file-encoding-notice.txt "$file" > FileEncoding.java
mv FileEncoding.java "$file"

%build
mkdir -p target/classes target/test-classes
framework=/usr/share/maven-repository/org/apache/maven/enforcer/enforcer-api/3.6.2/enforcer-api-3.6.2.jar
cp="$framework:/usr/share/maven/lib/*:/usr/share/java/javapackages-bootstrap/*"
find src/main/java -name '*.java' | sort > target/main.list
javac --release 8 -encoding UTF-8 -cp "$cp" -processor org.eclipse.sisu.space.SisuIndexAPT6 -d target/classes @target/main.list
test -s target/classes/META-INF/sisu/javax.inject.Named
grep -F org.codehaus.mojo.extraenforcer.dependencies.EnforceBytecodeVersion target/classes/META-INF/sisu/javax.inject.Named
jar --create --file target/rules.jar -C target/classes .
%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/rules.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.codehaus.mojo</groupId><artifactId>%{name}</artifactId><extension>jar</extension><version>%{version}</version>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path></artifact>
 <artifact><groupId>org.codehaus.mojo</groupId><artifactId>%{name}</artifactId><extension>pom</extension><version>%{version}</version>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Run the upstream dependency, encoding and model checks against native Maven and Enforcer.
framework=/usr/share/maven-repository/org/apache/maven/enforcer/enforcer-api/3.6.2/enforcer-api-3.6.2.jar
cp="target/classes:$framework:/usr/share/maven/lib/*:/usr/share/java/javapackages-bootstrap/*"
find src/test/java -name '*.java' | sort > target/tests.list
javac --release 17 -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/tests.list
if test -d src/test/resources; then cp -r src/test/resources/. target/test-classes/; fi
classes=$(find src/test/java -name '*Test.java' ! -name 'Abstract*' | sed 's|^src/test/java/||;s|[.]java$||;s|/|.|g')
java -cp "target/test-classes:$cp" org.junit.runner.JUnitCore $classes
# Load the packaged Sisu rule in Maven and check acceptance and rejection of Java 17 bytecode.
bash %{SOURCE2} %{buildroot} %{version}

%files
%license LICENSE.txt file-encoding-notice.txt
%doc README.md
%{_datadir}/maven-metadata/extra-enforcer-rules.xml
%{repo_dir}/org/codehaus/mojo/extra-enforcer-rules/

%changelog
%autochangelog
