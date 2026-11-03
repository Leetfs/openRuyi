# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           powermock-reflect
Version:        2.0.9
Release:        %autorelease
Summary:        Reflection helpers for testing Java classes
License:        Apache-2.0
URL:            https://powermock.github.io/
VCS:            git:https://github.com/powermock/powermock
#!RemoteAsset:  sha256:ff238dab46748a8f4532e95f069dd8cd0a6e7e117189c58cccc4d704c4b92c87
Source0:        https://github.com/powermock/powermock/archive/refs/tags/powermock-%{version}.tar.gz
#!RemoteAsset:  sha256:316ff63f5b09e3e240a4d4e1cafeb7fcfb27208ccabaaf17fee8a455e8654a24
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/powermock/powermock-reflect/%{version}/powermock-reflect-%{version}.pom
#!RemoteAsset:  sha256:20d83b13de814869f466e1d7e6e88c584105a8a443ecfed629309dd4d85d2eb0
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/powermock/powermock-core/%{version}/powermock-core-%{version}.pom
#!RemoteAsset:  sha256:ebe922b22c17fd0316a21eb4129e3840a63dcaaf884220a65a548b3323a26077
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/powermock/powermock-module-junit4-common/%{version}/powermock-module-junit4-common-%{version}.pom
#!RemoteAsset:  sha256:06414813c5ebcf91ee0795db9c3e3b53b522b53ce51b54348f78e5a9522a66e1
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/powermock/powermock-module-junit4/%{version}/powermock-module-junit4-%{version}.pom
#!RemoteAsset:  sha256:10f31a52304afca4c861191779a2baa003ae6e6fd80bfde3bee3e69273723b71
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/powermock/powermock-api-support/%{version}/powermock-api-support-%{version}.pom
#!RemoteAsset:  sha256:bc04807316ac745bbb48c7356e1407637bcac4bbd2a25f3720c2f08e57fa5e07
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/powermock/powermock-api-mockito2/%{version}/powermock-api-mockito2-%{version}.pom
#!RemoteAsset:  sha256:8c2a172bf8cbf08b29dfee7f958d8c1211c648a3a162f090775ba36102609a03
Source7:        https://github.com/stefanbirkner/system-rules/archive/refs/tags/system-rules-1.18.0.tar.gz?/system-rules-1.18.0.tar.gz
Source8:        check-powermock.sh
Source9:        StaticServiceTest.java
Source10:       install-powermock.py
BuildArch:      noarch

# https://github.com/raphw/byte-buddy/blob/byte-buddy-1.17.7/byte-buddy-dep/pom.xml
Patch2000:      2000-use-system-asm-for-proxy-test.patch
# https://github.com/powermock/powermock/tree/powermock-2.0.9/powermock-reflect/src/test/java
Patch2001:      2001-select-junit-object-comparison.patch

Patch2002:      2002-adapt-runner-to-system-frameworks.patch
Patch2003:      2003-update-framework-test-fixtures.patch

BuildRequires:  mvn(org.javassist:javassist) == 3.27.0-GA
BuildRequires:  python3
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(cglib:cglib) == 3.2.9
Provides:       mvn(org.powermock:powermock-reflect) == %{version}
Requires:       javapackages-bootstrap

%description
PowerMock Reflect provides the Whitebox API for looking up constructors,
methods and fields and for inspecting the internal state of Java objects
in tests.

%package     -n powermock
Summary:        PowerMock class transformers and JUnit 4 integration
Requires:       %{name} = %{version}-%{release}
Requires:       javapackages-bootstrap
Requires:       mvn(org.javassist:javassist) == 3.27.0-GA
Provides:       mvn(org.powermock:powermock-core) == %{version}
Provides:       mvn(org.powermock:powermock-module-junit4-common) == %{version}
Provides:       mvn(org.powermock:powermock-module-junit4) == %{version}
Provides:       mvn(org.powermock:powermock-api-support) == %{version}
Provides:       mvn(org.powermock:powermock-api-mockito2) == %{version}

%description -n powermock
PowerMock integrates JUnit and Mockito with class-loader based mocking
of static methods, constructors and final classes.

%prep
%autosetup -p1 -n powermock-powermock-%{version}
mkdir -p target/{system-rules,modules}
tar xf %{SOURCE7} --strip-components=1 -C target/system-rules
cp -p %{SOURCE2} target/modules/powermock-core.pom
cp -p %{SOURCE3} target/modules/powermock-module-junit4-common.pom
cp -p %{SOURCE4} target/modules/powermock-module-junit4.pom
cp -p %{SOURCE5} target/modules/powermock-api-support.pom
cp -p %{SOURCE6} target/modules/powermock-api-mockito2.pom
cd powermock-reflect
cp -p %{SOURCE1} pom.xml
mkdir -p .xmvn local-repository
if test -d %{repo_dir}; then cp -as %{repo_dir}/. local-repository/; fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <repositories><repository><id>install</id><type>maven</type>
    <properties><root>usr/share/maven-repository</root></properties>
  </repository></repositories>
  <installerSettings><metadataDir>usr/share/maven-metadata</metadataDir></installerSettings>
  <artifactManagement><rule><artifactGlob/>
    <versions><version>%{version}</version><version>SYSTEM</version></versions>
  </rule></artifactManagement>
  <resolverSettings><metadataRepositories>
    <repository>%{_datadir}/maven-metadata</repository>
    <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
  </metadataRepositories></resolverSettings>
</configuration>
EOF

%build
cd powermock-reflect
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository" \
    -Dmaven.compiler.source=8 -Dmaven.compiler.target=8 \
    org.apache.maven.plugins:maven-compiler-plugin:compile \
    org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

cd ..
cp="$PWD/powermock-reflect/target/powermock-reflect-%{version}.jar:%{repo_dir}/org/javassist/javassist/3.27.0-GA/javassist-3.27.0-GA.jar:%{bootstrap_java}/*"
for dir in powermock-core powermock-modules/{powermock-module-junit4-common,powermock-module-junit4} powermock-api/{powermock-api-support,powermock-api-mockito2}; do
    name=$(basename "$dir")
    out="$PWD/target/classes/$name"; mkdir -p "$out"
    find "$dir/src/main/java" -name '*.java' | sort > "$out/sources"
    javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d "$out" @"$out/sources"
    rm "$out/sources"
    if test -d "$dir/src/main/resources"; then cp -r "$dir/src/main/resources/." "$out/"; fi
    jar="$PWD/target/modules/$name.jar"
    printf 'Implementation-Title: %%s\nImplementation-Version: %%s\n' "$name" '%{version}' > target/module.mf
    jar cfm "$jar" target/module.mf -C "$out" .
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > target/powermock-classpath

%install
cd powermock-reflect
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}
cd ..
python3 %{SOURCE10} %{buildroot} %{_datadir} target/modules

%check
cd powermock-reflect
cp="target/%{name}-%{version}.jar:%{repo_dir}/cglib/cglib/3.2.9/cglib-3.2.9.jar:%{bootstrap_java}/*"
mkdir -p target/test-classes
find src/test/java -name '*.java' | sort > test-sources
javac -encoding UTF-8 -source 8 -target 8 -cp "$cp" -d target/test-classes @test-sources
find src/test/java -name '*Test.java' | sort | sed 's@^src/test/java/@@; s@/@.@g; s@\.java$@@' > test-classes
test -s test-classes
# CGLIB defines proxy classes through ClassLoader.defineClass on the test JVM.
java --add-opens=java.base/java.lang=ALL-UNNAMED -cp "target/test-classes:$cp" org.junit.runner.JUnitCore $(cat test-classes)

cd ..
bash %{SOURCE8} %{SOURCE9} %{buildroot}

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/maven-metadata/powermock-reflect.xml
%{repo_dir}/org/powermock/powermock-reflect/

%files -n powermock
%license LICENSE.txt
%{_datadir}/maven-metadata/powermock.xml
%{repo_dir}/org/powermock/powermock-core/
%{repo_dir}/org/powermock/powermock-module-junit4-common/
%{repo_dir}/org/powermock/powermock-module-junit4/
%{repo_dir}/org/powermock/powermock-api-support/
%{repo_dir}/org/powermock/powermock-api-mockito2/

%changelog
%autochangelog
