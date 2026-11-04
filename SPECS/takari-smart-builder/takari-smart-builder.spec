# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global artifact_dir %{repo_dir}/io/takari/maven/%{name}/%{version}

Name:           takari-smart-builder
Version:        1.1.0
Release:        %autorelease
Summary:        Dependency-aware parallel builder for Maven reactors
License:        Apache-2.0 AND EPL-1.0
URL:            https://github.com/takari/takari-smart-builder
VCS:            git:https://github.com/takari/takari-smart-builder
#!RemoteAsset:  sha256:4d7ea84fb9e76934ba242c35251b806657672804cd3f0b9dc1c3d82fddc46b4a
Source0:        https://github.com/takari/takari-smart-builder/archive/refs/tags/takari-smart-builder-%{version}.tar.gz?/takari-smart-builder-%{version}.tar.gz
#!RemoteAsset:  sha256:1e761f874dc3370a92677a80f1ad1ec4d01c53c70595a899cceb36363301a726
Source1:        https://maven-central.storage-download.googleapis.com/maven2/io/takari/takari/64/takari-64.pom
#!RemoteAsset:  sha256:1528e4d4ad4ee3dcdcf20a46571ae607b1eefaec4918fc94d5f05e9ac17331e5
Source2:        https://raw.githubusercontent.com/eclipse-ecf/ecf/85965b70101a8022ea1ee3f1bf1dc65bd99220b8/incubation/projects/org.eclipse.ecf.ipc/bundles/org.eclipse.ecf.ipc.library/misc/epl-v10.html
Source3:        check-reactor.sh
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin) == 3.2.0
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(io.takari.maven:takari-smart-builder) == %{version}
Provides:       mvn(io.takari:takari:pom:) == 64
Requires:       maven >= 3.9.9

%description
The Takari smart builder schedules Maven reactor projects on parallel worker
threads after their upstream dependencies complete. It also reports the
critical path through the reactor.

%prep
%autosetup -n takari-smart-builder-takari-smart-builder-%{version}
cp %{SOURCE2} EPL-1.0.html

%build
mkdir -p target/classes target/test-classes
cp='/usr/share/maven/lib/*:/usr/share/java/javapackages-bootstrap/*'
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -processor org.eclipse.sisu.space.SisuIndexAPT6 -cp "$cp" -d target/classes @target/sources
if test -d src/main/resources; then cp -r src/main/resources/. target/classes/; fi
grep -F io.takari.maven.builder.smart.SmartBuilder target/classes/META-INF/sisu/javax.inject.Named
jar cf target/smart.jar -C target/classes .

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-parent %{SOURCE1}
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/smart.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>io.takari.maven</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path></artifact>
 <artifact><groupId>io.takari.maven</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Exercise the released queue, topology, parallel executor and project-comparison suites.
cp='target/smart.jar:/usr/share/maven/lib/*:/usr/share/java/javapackages-bootstrap/*'
find src/test/java -name '*.java' ! -path '*/its/*' | sort > target/test-sources
javac --release 8 -encoding UTF-8 -proc:none -cp "$cp" -d target/test-classes @target/test-sources
if test -d src/test/resources; then cp -r src/test/resources/. target/test-classes/; fi
java -cp "target/test-classes:$cp" org.junit.runner.JUnitCore io.takari.maven.builder.smart.ReactorBuildQueueTest io.takari.maven.builder.smart.ProjectComparatorTest io.takari.maven.builder.smart.DagWidthTest io.takari.maven.builder.smart.ProjectExecutorServiceTest
# Run the upstream three-module fixtures with the distribution Maven and check aggregation occurs only at the reactor root.
bash %{SOURCE3}

%files
%license LICENSE EPL-1.0.html
%doc README.md
%{_datadir}/maven-metadata/takari-smart-builder.xml
%{_datadir}/maven-metadata/takari-smart-builder-parent.xml
%{repo_dir}/io/takari/maven/takari-smart-builder/
%{repo_dir}/io/takari/takari/64/

%changelog
%autochangelog
