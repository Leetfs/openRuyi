# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global tools %{_libexecdir}/eclipse-equinox
Name:           eclipse-jdt-debug
Version:        4.39
Release:        %autorelease
Summary:        Eclipse Java debugger and VM launching support
License:        EPL-2.0 AND BSD-3-Clause
URL:            https://eclipse.dev/jdt/
VCS:            git:https://github.com/eclipse-jdt/eclipse.jdt.debug
#!RemoteAsset:  sha256:0d69392d92abbcbaf913deb63ee07752b20b165d609e4ad502605b55316825f4
Source0:        https://github.com/eclipse-jdt/eclipse.jdt.debug/archive/refs/tags/R4_39.tar.gz?/jdt-debug-R4_39.tar.gz
#!RemoteAsset:  sha256:c80aae3d377de929f7dbb96ae806f5bcbc4987002bca6d63d4ee9404a9efaf87
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/org.eclipse.jdt.debug/3.25.100/org.eclipse.jdt.debug-3.25.100.pom
#!RemoteAsset:  sha256:6d27ff37995bebe9d0e82c7d558d7a4eea24cb5ee6d8320ba326dfd7f68b39d6
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/org.eclipse.jdt.launching/3.24.100/org.eclipse.jdt.launching-3.24.100.pom
Source3:        EclipseVmCheck.java
#!RemoteAsset:  sha256:293b6af371eee28b0ff16f0334ea19e20a3d5522143faa4b95b346855507879a
Source4:        https://gitlab.ow2.org/asm/asm/-/raw/ASM_9_9/LICENSE.txt?/ASM-LICENSE.txt
#!RemoteAsset:  sha256:3df218c27b6f2218814f0150e113c73a6385df7b111ec7eacc82544dc94f1427
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/org.eclipse.jdt.launching.macosx/3.6.400/org.eclipse.jdt.launching.macosx-3.6.400.pom
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(nested-only-bundles)
BuildRequires:  eclipse-debug-core
BuildRequires:  eclipse-jdt-core
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin) == 3.6.1
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
BuildRequires:  osgi-service-prefs
BuildRequires:  unzip
BuildRequires:  xmlstarlet
Provides:       mvn(org.eclipse.jdt:org.eclipse.jdt.debug) == 3.25.100
Provides:       mvn(org.eclipse.jdt:org.eclipse.jdt.launching) == 3.24.100
Requires:       eclipse-debug-core
Requires:       eclipse-jdt-core

%description
The Eclipse Java debugger implements the Java Debug Interface and
connects to local or remote virtual machines. The launching bundle
provides JRE configuration, a library detector and a source lookup agent.

%package     -n eclipse-jdt-launching-macosx
Version:        3.6.400
Summary:        Eclipse JDT launcher support for macOS targets
License:        EPL-2.0
Provides:       mvn(org.eclipse.jdt:org.eclipse.jdt.launching.macosx) == 3.6.400
Requires:       mvn(org.eclipse.jdt:org.eclipse.jdt.launching) == 3.24.100

%description -n eclipse-jdt-launching-macosx
Java launcher integration for macOS target platforms. The bundle declares
its macOS platform filter and supplies the Maven model used by JDT clients.

%prep
%autosetup -n eclipse.jdt.debug-R4_39
cp -p %{SOURCE4} ASM-LICENSE.txt
# The Java 1.1 helper last shipped from upstream commit 72a2dd63.
# StringBuilder was introduced in Java 5.
legacy=org.eclipse.jdt.launching/support/org/eclipse/jdt/internal/launching/support/LegacySystemProperties.java
grep -F 'StringBuilder buffer = new StringBuilder();' "$legacy"
sed -i 's/StringBuilder buffer = new StringBuilder()/StringBuffer buffer = new StringBuffer()/' "$legacy"
rm org.eclipse.jdt.launching/lib/{launchingsupport.jar,javaagent-shaded.jar}
agent=org.eclipse.jdt.launching.javaagent
for n in maven-jar-plugin maven-shade-plugin; do
    if test "$n" = maven-shade-plugin; then
        jar=%{repo}/org/apache/maven/plugins/maven-shade-plugin/3.6.1/maven-shade-plugin-3.6.1.jar
    else
        jar=%{_datadir}/java/javapackages-bootstrap/maven-jar-plugin.jar
    fi
    version=$(unzip -p "$jar" META-INF/maven/plugin.xml | xmlstarlet sel -t -v /plugin/version)
    test -n "$version"
    xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 -u "/m:project/m:build/m:plugins/m:plugin[m:artifactId='$n']/m:version" -v "$version" "$agent/pom.xml"
done
# Build the standalone agent with its own Maven project root.
mkdir -p "$agent/.mvn" "$agent/.xmvn"
cat > "$agent/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF

%build
mkdir -p build/{bundles,support}
base=$PWD
launch=org.eclipse.jdt.launching
legacy=%{repo}/org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar
java -cp "$legacy" org.eclipse.jdt.internal.compiler.batch.Main -proc:none -source 1.3 -target 1.1 -d build/support "$launch"/support/org/eclipse/jdt/internal/launching/support/*.java
jar cf "$launch/lib/launchingsupport.jar" -C build/support .
(
    cd org.eclipse.jdt.launching.javaagent
    mkdir -p target/classes
    find src/main/java -name '*.java' | sort > target/sources-list
    javac --release 8 -proc:none -cp %{_datadir}/java/javapackages-bootstrap/asm.jar -d target/classes @target/sources-list
    export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
    ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
    export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
    jar_version=$(unzip -p %{_datadir}/java/javapackages-bootstrap/maven-jar-plugin.jar META-INF/maven/plugin.xml | xmlstarlet sel -t -v /plugin/version)
    mvn -B -o -Dmaven.repo.local="$base/build/maven-repo" "org.apache.maven.plugins:maven-jar-plugin:$jar_version:jar" org.apache.maven.plugins:maven-shade-plugin:3.6.1:shade@default
    cp target/javaagent-shaded.jar "$base/$launch/lib/"
)
cp=$(find %{repo}/org/eclipse/{platform,jdt} %{repo}/org/osgi/org.osgi.service.prefs -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
%{tools}/build-bundle org.eclipse.jdt.debug build/bundles/org.eclipse.jdt.debug.jar --release 17 --classpath "$cp" --nested-classpath "$cp"
unzip -p build/bundles/org.eclipse.jdt.debug.jar jdimodel.jar > build/jdimodel.jar
%{tools}/build-bundle "$launch" "build/bundles/$launch.jar" --release 17 --classpath "$PWD/build/jdimodel.jar:$cp"
mac=org.eclipse.jdt.launching.macosx
sed -i 's/^Bundle-Version: 3.6.400.qualifier/Bundle-Version: 3.6.400.v20260211-1052/' "$mac/META-INF/MANIFEST.MF"
%{tools}/build-bundle "$mac" "build/bundles/$mac.jar" --release 17 --classpath "$PWD/build/jdimodel.jar:$PWD/build/bundles/$launch.jar:$cp"
printf '%%s\n' "$cp" > build/classpath

%install
%{tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}

%{tools}/install-bundles --qualifier v20260211-1052 %{buildroot} %{_datadir} eclipse-jdt-launching-macosx build/bundles %{SOURCE5}

%check
launch=build/bundles/org.eclipse.jdt.launching.jar
for name in javaagent-shaded launchingsupport; do unzip -p "$launch" "lib/$name.jar" > "build/$name.jar"; done
for name in LegacySystemProperties LibraryDetector; do
    class=org.eclipse.jdt.internal.launching.support.$name
    javap -v -cp build/launchingsupport.jar "$class" > build/class-info
    grep -F 'minor version: 3' build/class-info
    grep -F 'major version: 45' build/class-info
    java -Dopenruyi.jdt.check=detected -cp build/launchingsupport.jar "$class" openruyi.jdt.check > "build/$name.out"
done
grep -F 'value= "detected"' build/LegacySystemProperties.out
grep -F '|' build/LibraryDetector.out
java -javaagent:build/javaagent-shaded.jar=debuglog -version > build/agent.log 2>&1
grep -F 'Advanced source lookup enabled.' build/agent.log
mkdir build/tests
cp="build/jdimodel.jar:build/bundles/org.eclipse.jdt.launching.jar:$(cat build/classpath)"
javac --release 17 -proc:none -cp "$cp" -d build/tests %{SOURCE3}
timeout 45 java -cp "build/tests:$cp" EclipseVmCheck "$PWD/build/tests"
cat > build/CheckLaunchFilter.java <<'EOF'
import java.util.Map;
import java.util.jar.JarFile;
import org.osgi.framework.FrameworkUtil;

class CheckLaunchFilter {
    public static void main(String[] args) throws Exception {
        try (JarFile jar = new JarFile(args[0])) {
            var manifest = jar.getManifest().getMainAttributes();
            var filter = FrameworkUtil.createFilter(manifest.getValue("Eclipse-PlatformFilter"));
            if (!filter.matches(Map.of("osgi.os", "macosx")) || filter.matches(Map.of("osgi.os", "linux")))
                throw new AssertionError(filter);
            if (!"3.6.400.v20260211-1052".equals(manifest.getValue("Bundle-Version"))
                    || jar.stream().filter(e -> e.getName().endsWith(".class")).count() != 5)
                throw new AssertionError("Unexpected macOS launcher contents");
        }
    }
}
EOF
java -cp "$cp" build/CheckLaunchFilter.java build/bundles/org.eclipse.jdt.launching.macosx.jar


%files
%license LICENSE NOTICE ASM-LICENSE.txt
%{_datadir}/maven-metadata/eclipse-jdt-debug.xml
%{repo}/org/eclipse/jdt/org.eclipse.jdt.debug/
%{repo}/org/eclipse/jdt/org.eclipse.jdt.launching/

%files -n eclipse-jdt-launching-macosx
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-jdt-launching-macosx.xml
%{repo}/org/eclipse/jdt/org.eclipse.jdt.launching.macosx/

%changelog
%autochangelog
