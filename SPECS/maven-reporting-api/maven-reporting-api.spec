# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global artifact_dir %{_datadir}/maven-repository/org/apache/maven/reporting/%{name}/%{version}
Name:           maven-reporting-api
Version:        3.0
Release:        %autorelease
Summary:        Apache Maven reporting interfaces
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-reporting-api/
VCS:            git:https://github.com/apache/maven-reporting-api
#!RemoteAsset:  sha256:2129ffdeabd662569981dce0fd3f6d5856a13ec5be931d6ddea7abcf8e2589b5
Source0:        https://github.com/apache/maven-reporting-api/archive/refs/tags/maven-reporting-api-3.0.tar.gz?/maven-reporting-api-3.0.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
#!RemoteAsset:  sha256:a4fbb1f99ed82903029a5a16ad0424b687dc7eb6db13947d1ae6387d8b1912ac
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0-source-release.zip
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:) == 15
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api) == 1.0
Provides:       mvn(org.apache.maven.reporting:maven-reporting-api) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 15
Requires:       mvn(org.apache.maven.doxia:doxia-sink-api) == 1.0

BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api) == 2.0.0
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:) == 43
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.reporting:maven-reporting-api) == 4.0.0
Requires:       mvn(org.apache.maven.doxia:doxia-sink-api) == 2.0.0
Requires:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 43

%description
The Maven Reporting API defines report generation, rendering and multi-page
report contracts for Maven plugins.

%prep
%autosetup -n maven-reporting-api-maven-reporting-api-3.0
cp %{SOURCE1} LICENSE

unzip -q %{SOURCE2}

%build
mkdir -p target/classes
find src/main/java -name '*.java' | sort > target/sources
sink=%{_datadir}/maven-repository/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.jar
javac --release 8 -proc:none -encoding UTF-8 -cp "$sink" -d target/classes @target/sources
mkdir -p target/classes/META-INF/maven/org.apache.maven.reporting/%{name}
install -m644 pom.xml target/classes/META-INF/maven/org.apache.maven.reporting/%{name}/pom.xml
jar cf target/api.jar -C target/classes .

mkdir -p target/modern-classes
find maven-reporting-api-4.0.0/src/main/java -name '*.java' | sort > target/modern-sources
modern_sink=%{_datadir}/maven-repository/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.jar
javac --release 8 -g -proc:none -cp "$modern_sink" -d target/modern-classes @target/modern-sources
meta=target/modern-classes/META-INF/maven/org.apache.maven.reporting/%{name}
mkdir -p "$meta"
cp maven-reporting-api-4.0.0/pom.xml "$meta/pom.xml"
jar cf target/modern-api.jar -C target/modern-classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/api.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.apache.maven.reporting</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
 <artifact><groupId>org.apache.maven.reporting</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

modern=%{_datadir}/maven-repository/org/apache/maven/reporting/%{name}/4.0.0
install -d "%{buildroot}$modern"
install -m644 target/modern-api.jar "%{buildroot}$modern/%{name}-4.0.0.jar"
install -m644 maven-reporting-api-4.0.0/pom.xml "%{buildroot}$modern/%{name}-4.0.0.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}-4.0.0.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.reporting</groupId><artifactId>%{name}</artifactId><version>4.0.0</version><extension>jar</extension><path>$modern/%{name}-4.0.0.jar</path><compatVersions><version>4.0.0</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.reporting</groupId><artifactId>%{name}</artifactId><version>4.0.0</version><extension>pom</extension><path>$modern/%{name}-4.0.0.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>4.0.0</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
mkdir -p target/test
# JaCoCo consumes the legacy single-page and current multi-page report signatures.
cat > target/ReportCheck.java <<'EOF'
import java.util.Locale;
import org.apache.maven.reporting.*;
class ReportCheck {
    public static void main(String[] args) throws Exception {
        MavenReport.class.getMethod("generate", org.codehaus.doxia.sink.Sink.class, Locale.class);
        MavenMultiPageReport.class.getMethod("generate", org.apache.maven.doxia.sink.Sink.class,
            org.apache.maven.doxia.sink.SinkFactory.class, Locale.class);
        Exception cause = new Exception();
        if (new MavenReportException("report", cause).getCause() != cause) throw new AssertionError();
    }
}
EOF
cp="target/api.jar:%{_datadir}/maven-repository/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.jar"
javac --release 8 -cp "$cp" -d target/test target/ReportCheck.java
java -cp "target/test:$cp" ReportCheck

cat > target/ModernReportCheck.java <<'EOF'
import java.util.Locale;
import org.apache.maven.reporting.*;
class ModernReportCheck {
    public static void main(String[] args) throws Exception {
        MavenReport.class.getMethod("generate", org.apache.maven.doxia.sink.Sink.class, Locale.class);
        MavenMultiPageReport.class.getMethod("generate", org.apache.maven.doxia.sink.Sink.class,
            org.apache.maven.doxia.sink.SinkFactory.class, Locale.class);
        Exception cause = new Exception();
        if (new MavenReportException("report", cause).getCause() != cause) throw new AssertionError();
    }
}
EOF
cp="target/modern-api.jar:%{_datadir}/maven-repository/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.jar"
javac --release 8 -cp "$cp" -d target/test target/ModernReportCheck.java
java -cp "target/test:$cp" ModernReportCheck

%files
%license LICENSE
%{_datadir}/maven-metadata/maven-reporting-api.xml
%{_datadir}/maven-metadata/maven-reporting-api-4.0.0.xml
%{artifact_dir}/
%{_datadir}/maven-repository/org/apache/maven/reporting/maven-reporting-api/4.0.0/

%changelog
%autochangelog
