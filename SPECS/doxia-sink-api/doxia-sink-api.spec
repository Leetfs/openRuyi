# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global artifact_dir %{_datadir}/maven-repository/org/apache/maven/doxia/%{name}/%{version}
Name:           doxia-sink-api
Version:        1.0
Release:        %autorelease
Summary:        Apache Maven Doxia document sink interfaces
License:        Apache-2.0
URL:            https://maven.apache.org/doxia/
VCS:            git:https://github.com/apache/maven-doxia
#!RemoteAsset:  sha256:a8ab1bee18c31cb3aba982e989f88ce7f9d9b5361df9e9f2e7f89c5d03d931f3
Source0:        https://github.com/apache/maven-doxia/archive/refs/tags/doxia-1.0.tar.gz?/doxia-1.0.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
#!RemoteAsset:  sha256:46932b1aea6ee980aee484e96e4e9eedc0d2a7b192b9ed42b16a9903556fe96c
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/doxia/doxia/2.0.0/doxia-2.0.0-source-release.zip
#!RemoteAsset:  sha256:92605d9a075cc6d2cf38a65464b39aba5079018c54bd7d9d25b935d5f009d4e9
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/doxia/doxia/2.1.0/doxia-2.1.0-source-release.zip
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 10
Provides:       mvn(org.apache.maven.doxia:doxia-sink-api) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia:pom:) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 10

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 43
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 43

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 47
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 47

Provides:       mvn(org.apache.maven.doxia:doxia-sink-api) == 2.0.0

Provides:       mvn(org.apache.maven.doxia:doxia-sink-api) == 2.1.0

%description
Doxia defines a document sink and factory for Maven report generators.
The API supports the original Codehaus sink interface.

%prep
%autosetup -n maven-doxia-doxia-1.0
cp %{SOURCE1} LICENSE
unzip -q %{SOURCE2}
unzip -q %{SOURCE3}

%build
mkdir -p target/classes
find doxia-sink-api/src/main/java -name '*.java' | sort > target/sources
javac --release 8 -proc:none -encoding UTF-8 -d target/classes @target/sources
mkdir -p target/classes/META-INF/maven/org.apache.maven.doxia/%{name}
install -m644 doxia-sink-api/pom.xml target/classes/META-INF/maven/org.apache.maven.doxia/%{name}/pom.xml
jar cf target/api.jar -C target/classes .

for version in 2.0.0 2.1.0; do
    source=doxia-$version/doxia-sink-api
    out=target/$version
    mkdir -p "$out/classes/META-INF/maven/org.apache.maven.doxia/%{name}"
    find "$source/src/main/java" -name '*.java' | sort > "$out/sources"
    javac --release 8 -g -Xpkginfo:always -proc:none -encoding UTF-8 -d "$out/classes" @"$out/sources"
    cp "$source/pom.xml" "$out/classes/META-INF/maven/org.apache.maven.doxia/%{name}/pom.xml"
    jar cf "$out/api.jar" -C "$out/classes" .
done

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/api.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 doxia-sink-api/pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models pom.xml doxia-2.0.0/pom.xml doxia-2.1.0/pom.xml
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.apache.maven.doxia</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
 <artifact><groupId>org.apache.maven.doxia</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

for version in 2.0.0 2.1.0; do
    dir=%{_datadir}/maven-repository/org/apache/maven/doxia/%{name}/$version
    install -d "%{buildroot}$dir"
    install -m644 "target/$version/api.jar" "%{buildroot}$dir/%{name}-$version.jar"
    install -m644 "doxia-$version/doxia-sink-api/pom.xml" "%{buildroot}$dir/%{name}-$version.pom"
    cat > "%{buildroot}%{_datadir}/maven-metadata/%{name}-$version.xml" <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>%{name}</artifactId><version>$version</version><extension>jar</extension><path>$dir/%{name}-$version.jar</path><compatVersions><version>$version</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>%{name}</artifactId><version>$version</version><extension>pom</extension><path>$dir/%{name}-$version.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>$version</version></compatVersions></artifact>
</artifacts></metadata>
EOF
done

%check
mkdir -p target/test
# Exercise both public sink namespaces and the factory used by report generators.
cat > target/SinkCheck.java <<'EOF'
import java.io.File;
import java.lang.reflect.Proxy;
import org.apache.maven.doxia.sink.SinkFactory;
class SinkCheck {
    public static void main(String[] args) {
        StringBuilder received = new StringBuilder();
        org.codehaus.doxia.sink.Sink sink = (org.codehaus.doxia.sink.Sink) Proxy.newProxyInstance(
            SinkCheck.class.getClassLoader(), new Class<?>[]{org.codehaus.doxia.sink.Sink.class},
            (proxy, method, values) -> {
                if (method.getName().equals("text")) received.append(values[0]);
                return null;
            });
        SinkFactory factory = (dir, name) -> sink;
        factory.createSink(new File("."), "report").text("coverage");
        if (!received.toString().equals("coverage")) throw new AssertionError(received);
    }
}
EOF
javac --release 8 -cp target/api.jar -d target/test target/SinkCheck.java
java -cp target/test:target/api.jar SinkCheck

cat > target/ModernSinkCheck.java <<'EOF'
import java.lang.reflect.Proxy;
import org.apache.maven.doxia.sink.Sink;
class ModernSinkCheck {
    public static void main(String[] args) {
        StringBuilder received = new StringBuilder();
        Sink sink = (Sink) Proxy.newProxyInstance(Sink.class.getClassLoader(), new Class<?>[]{Sink.class},
            (proxy, method, values) -> { received.append(method.getName()).append(" "); return null; });
        sink.head(); sink.title(); sink.text("SDK"); sink.title_(); sink.head_(); sink.close();
        if (!received.toString().equals("head title text title_ head_ close ")) throw new AssertionError(received);
    }
}
EOF
for version in 2.0.0 2.1.0; do
    javac --release 8 -cp "target/$version/api.jar" -d target/test target/ModernSinkCheck.java
    java -cp "target/test:target/$version/api.jar" ModernSinkCheck
done

%files
%license LICENSE
%{_datadir}/maven-metadata/doxia-sink-api.xml
%{_datadir}/maven-metadata/doxia-sink-api-2.*.xml
%{artifact_dir}/
%{_datadir}/maven-repository/org/apache/maven/doxia/doxia-sink-api/2.*/
%{_datadir}/maven-metadata/doxia-sink-api-models.xml
%{_datadir}/maven-repository/org/apache/maven/doxia/doxia/%{version}/
%{_datadir}/maven-repository/org/apache/maven/doxia/doxia/2.*/

%changelog
%autochangelog
