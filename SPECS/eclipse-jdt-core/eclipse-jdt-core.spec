# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           eclipse-jdt-core
Version:        3.45.0
Release:        %autorelease
Summary:        Eclipse Java compiler and Java language model
License:        EPL-2.0
URL:            https://eclipse.dev/jdt/
VCS:            git:https://github.com/eclipse-jdt/eclipse.jdt.core
#!RemoteAsset:  sha256:0e63a0efd614be76836baf3629c9098eb1ae33fdd799f444e021be261587b867
Source0:        https://github.com/eclipse-jdt/eclipse.jdt.core/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:9dcd87523be648d90f706032f26ea7e0e26bfa6c55f111e6845fa89af7d01abe
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/ecj/%{version}/ecj-%{version}.pom
#!RemoteAsset:  sha256:049d18532ed78e2728e6d618cb5da42a6fe9f7b6eaedefa7b4ab8227ad2237dc
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/org.eclipse.jdt.core/%{version}/org.eclipse.jdt.core-%{version}.pom
Source3:        ModelCheck.java
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  mvn(org.eclipse.jdt:org.eclipse.jdt.annotation) == 2.4.100
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.resources) == 3.23.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.text) == 3.14.600
BuildRequires:  python3
Provides:       mvn(org.eclipse.jdt:ecj) == %{version}
Provides:       mvn(org.eclipse.jdt:org.eclipse.jdt.core) == %{version}
Requires:       eclipse-core-resources >= 4.39
Requires:       eclipse-text >= 4.39
Requires:       java-25-openjdk

%description
Eclipse JDT Core provides the Java syntax tree, language model, search
and code-formatting APIs. Its batch compiler implements the Java compiler
tool interface and can also run directly from the command line.

%prep
%autosetup -n eclipse.jdt.core-R4_39

%build
mkdir -p build/batch/META-INF build/bundles build/adapter
batch=org.eclipse.jdt.core.compiler.batch
model=org.eclipse.jdt.core
cp="%{bootstrap_java}/ant.jar:%{bootstrap_java}/ant-launcher.jar"
for coordinate in org.eclipse.osgi/3.24.100 org.eclipse.equinox.common/3.20.300 org.eclipse.core.jobs/3.15.700 org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 org.eclipse.core.contenttype/3.9.800 org.eclipse.core.runtime/3.34.200 org.eclipse.core.filesystem/1.11.400 org.eclipse.core.resources/3.23.200 org.eclipse.text/3.14.600 org.eclipse.core.commands/3.12.500; do
    name=${coordinate%%/*}; version=${coordinate##*/}
    cp="$cp:%{_datadir}/maven-repository/org/eclipse/platform/$coordinate/$name-$version.jar"
done
cp="$cp:%{_datadir}/maven-repository/org/osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar"
cp="$cp:%{_datadir}/maven-repository/org/eclipse/jdt/org.eclipse.jdt.annotation/2.4.100/org.eclipse.jdt.annotation-2.4.100.jar"
# The compiler runs on Java 17 and implements newer javax.lang.model methods.
# The distribution JDK supplies those signatures during compilation.
find "$batch/src" -name '*.java' | sort > build/batch-sources
javac -source 17 -target 17 -encoding UTF-8 -proc:none -cp "$cp" -d build/batch @build/batch-sources
classes="$PWD/build/batch"
(cd "$batch/src" && find . -type f ! -name '*.java' -exec cp --parents -t "$classes" '{}' +)
cp -a "$batch/META-INF/." build/batch/META-INF/
cp "$batch/about.html" build/batch/
sed 's/^Bundle-Version: %{version}\.qualifier$/Bundle-Version: %{version}/' "$batch/META-INF/MANIFEST.MF" > build/compiler.mf
jar --create --file build/bundles/ecj.jar --manifest build/compiler.mf -C build/batch .
cp="$PWD/build/bundles/ecj.jar:$cp"
%{_libexecdir}/eclipse-equinox/build-bundle "$model" "$PWD/build/bundles/$model.jar" --release 17 --classpath "$cp"
cp="$PWD/build/bundles/$model.jar:$cp"
find "$model/antadapter" -name '*.java' | sort > build/adapter-sources
javac --release 17 -encoding UTF-8 -cp "$cp" -d build/adapter @build/adapter-sources
classes="$PWD/build/adapter"
(cd "$model/antadapter" && find . -type f ! -name '*.java' -exec cp --parents -t "$classes" '{}' +)
jar --create --file build/jdtCompilerAdapter.jar -C build/adapter .
jar --update --file "build/bundles/$model.jar" -C build jdtCompilerAdapter.jar
printf '%%s\n' "$cp" > build/classpath

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/maven-repository/org/eclipse/jdt/ecj/%{version}/ecj-%{version}.pom
install -m644 build/bundles/ecj.jar %{buildroot}%{_datadir}/maven-repository/org/eclipse/jdt/ecj/%{version}/ecj-%{version}.jar
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/maven-repository/org/eclipse/jdt/org.eclipse.jdt.core/%{version}/org.eclipse.jdt.core-%{version}.pom
install -m644 build/bundles/org.eclipse.jdt.core.jar %{buildroot}%{_datadir}/maven-repository/org/eclipse/jdt/org.eclipse.jdt.core/%{version}/org.eclipse.jdt.core-%{version}.jar
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.eclipse.jdt</groupId><artifactId>ecj</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jdt/ecj/%{version}/ecj-%{version}.jar</path></artifact>
  <artifact><groupId>org.eclipse.jdt</groupId><artifactId>ecj</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jdt/ecj/%{version}/ecj-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>org.eclipse.jdt</groupId><artifactId>org.eclipse.jdt.core</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jdt/org.eclipse.jdt.core/%{version}/org.eclipse.jdt.core-%{version}.jar</path></artifact>
  <artifact><groupId>org.eclipse.jdt</groupId><artifactId>org.eclipse.jdt.core</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jdt/org.eclipse.jdt.core/%{version}/org.eclipse.jdt.core-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
cp=$(cat build/classpath)
mkdir -p build/smoke/classes build/tool-tests build/tool-harness
cat > build/smoke/Answer.java <<'EOF'
public record Answer(int n) {
    public static void main(String[] args) {
        if (new Answer(42).n() != 42) throw new AssertionError();
    }
}
EOF
java -jar build/bundles/ecj.jar -17 -proc:none -d build/smoke/classes build/smoke/Answer.java
java -cp build/smoke/classes Answer
javap -verbose -classpath build/smoke/classes Answer | grep -F 'major version: 61'
echo 'class Invalid { int n = "text"; }' > build/smoke/Invalid.java
if java -jar build/bundles/ecj.jar -17 -proc:none -d build/smoke/classes build/smoke/Invalid.java >build/smoke/invalid.log 2>&1; then exit 1; fi
grep -F 'Type mismatch: cannot convert from String to int' build/smoke/invalid.log
test ! -e build/smoke/classes/Invalid.class
java -ea -cp "$cp" %{SOURCE3}
jar tf build/jdtCompilerAdapter.jar | grep -Fx 'org/eclipse/jdt/core/BuildJarIndex.class'

# Reuse the listener and expected-output marker from the batch regression suite.
# The JSR 199 tests themselves only require JUnit and the two compiler providers.
python3 - <<'PYTOOLS'
from pathlib import Path
import re
package = "org.eclipse.jdt.compiler.tool.tests"
source = Path("org.eclipse.jdt.compiler.tool.tests/src", *package.split("."))
root = Path("build/tool-harness")
helper = (source / "AbstractCompilerToolTest.java").read_text()
first = helper.index("static class CompilerInvocationDiagnosticListener")
last = helper.index("\n\tstatic EclipseCompiler ", first)
listener = helper[first:last].replace("static class ", "class ", 1)
(root / "CompilerInvocationDiagnosticListener.java").write_text("package "+package+";\nimport javax.tools.*;\nimport java.io.PrintWriter;\n"+listener+"\n")
suite = Path("org.eclipse.jdt.core.tests.compiler/src/org/eclipse/jdt/core/tests/compiler/regression/AbstractBatchCompilerTest.java").read_text()
marker = re.search(r'public static final String OUTPUT_DIR_PLACEHOLDER = "[^"]+";', suite).group(0)
for name in ("CompilerToolTests", "CompilerToolJava9Tests"):
    text = (source / (name + ".java")).read_text().replace("import "+package+".AbstractCompilerToolTest.CompilerInvocationDiagnosticListener;", "")
    text = text.replace("import static org.eclipse.jdt.core.tests.compiler.regression.AbstractBatchCompilerTest.OUTPUT_DIR_PLACEHOLDER;", "")
    if "OUTPUT_DIR_PLACEHOLDER" in text:
        declaration = "public class "+name+" extends TestCase {"
        text = text.replace(declaration, declaration+"\n    "+marker)
    (root / (name+".java")).write_text(text)
PYTOOLS
junit="%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar"
javac -encoding UTF-8 -cp "$cp:$junit" -d build/tool-tests build/tool-harness/*.java
testcp="$PWD/build/tool-tests:$cp:$junit"
cd org.eclipse.jdt.compiler.tool.tests
java -ea -cp "$testcp" org.junit.runner.JUnitCore org.eclipse.jdt.compiler.tool.tests.CompilerToolTests org.eclipse.jdt.compiler.tool.tests.CompilerToolJava9Tests

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-jdt-core.xml
%{_datadir}/maven-repository/org/eclipse/jdt/ecj/
%{_datadir}/maven-repository/org/eclipse/jdt/org.eclipse.jdt.core/

%changelog
%autochangelog
