# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global qualifier v20221108-1853
%global maven_repo %{_datadir}/maven-repository
Name:           ecj-legacy
Version:        3.32.0
Release:        %autorelease
Summary:        Eclipse Java compiler for legacy class file targets
License:        EPL-2.0
URL:            https://eclipse.dev/jdt/core/
VCS:            git:https://github.com/eclipse-jdt/eclipse.jdt.core
#!RemoteAsset:  sha256:e0ec85b14bdae7ba62053dc09e763c683e0723a290f680de0b3c9a27c1828c0d
Source0:        https://github.com/eclipse-jdt/eclipse.jdt.core/archive/refs/tags/R4_26.tar.gz?/eclipse-jdt-core-R4_26.tar.gz
#!RemoteAsset:  sha256:9c7801d10bf7678a9123064208e705892b1df7d0936da2d4a0edd3c88a97b475
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/ecj/%{version}/ecj-%{version}.pom
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.jdt:org.eclipse.jdt.core) == 3.45.0
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.common) == 3.20.300
BuildRequires:  python3
Provides:       mvn(org.eclipse.jdt:ecj) == %{version}
Requires:       java-25-openjdk

%description
The Eclipse JDT batch compiler supports Java source and class file levels
needed by older virtual machines. It also implements the javax.tools
JavaCompiler service and supports annotation processing.

%prep
%autosetup -n eclipse.jdt.core-R4_26

%build
mkdir -p build/{bootstrap,classes,bundles}
core=org.eclipse.jdt.core
roots=("$core/compiler" "$core/batch" "$core/antadapter" org.eclipse.jdt.compiler.apt/src org.eclipse.jdt.compiler.tool/src)
find "${roots[@]}" -name '*.java' | sort > build/sources
# The ECJ batch distribution also includes these three JDT model classes.
for name in ExtraFlags SourceElementNotifier parser/TypeConverter; do echo "$core/model/org/eclipse/jdt/internal/compiler/$name.java" >> build/sources; done
cp="%{maven_repo}/org/eclipse/jdt/org.eclipse.jdt.core/3.45.0/org.eclipse.jdt.core-3.45.0.jar:%{_datadir}/java/javapackages-bootstrap/ant.jar:%{maven_repo}/org/eclipse/platform/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar"
# The annotation processing bridge uses newer JDK model interfaces while targeting Java 11 bytecode.
javac -source 11 -target 11 -encoding UTF-8 -proc:none -cp "$cp" -d build/bootstrap @build/sources
for src in "${roots[@]}"; do
    (cd "$src"; find . \( -name '*.properties' -o -name '*.rsc' -o -name '*.props' -o -path './META-INF/services/*' \) -type f -exec cp --parents '{}' "$OLDPWD/build/bootstrap/" \;)
done
java -cp "build/bootstrap:$cp" org.eclipse.jdt.internal.compiler.batch.Main -proc:none -nowarn \
    -source 11 -target 11 -encoding UTF-8 -cp "$cp" -d build/classes @build/sources
(cd build/bootstrap; find . -type f ! -name '*.class' -exec cp --parents '{}' ../classes/ \;)
sed -i 's/compiler.version = bundle_qualifier, bundle_version/compiler.version = %{qualifier}, %{version}/' \
    build/classes/org/eclipse/jdt/internal/compiler/batch/messages.properties
sed 's/^Bundle-Version: .*/Bundle-Version: %{version}.%{qualifier}/' \
    "$core/scripts/binary/META-INF/MANIFEST.MF" > build/MANIFEST.MF
install -m644 "$core/about.html" build/classes/about.html
install -m644 "$core/META-INF/eclipse.inf" build/classes/META-INF/eclipse.inf
jar cfm build/bundles/ecj.jar build/MANIFEST.MF -C build/classes .

%install
%{_libexecdir}/eclipse-equinox/install-bundles --qualifier %{qualifier} --symbolic-name org.eclipse.jdt.core.compiler.batch \
    %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1}

%check
java -jar build/bundles/ecj.jar -version | grep -F '%{qualifier}, %{version}'
# Exercise both legacy targets with a real compiled class and verify their JVM headers.
mkdir -p check/{java11,java5,service}
cat > check/Legacy.java <<'EOF'
public class Legacy { public static void main(String[] args) { System.out.print("legacy"); } }
EOF
for level in '1.3 1.1 java11' '1.5 1.5 java5'; do
    read -r source target dir <<< "$level"
    java -jar build/bundles/ecj.jar -proc:none -source "$source" -target "$target" -d "check/$dir" check/Legacy.java
    test "$(java -cp "check/$dir" Legacy)" = legacy
done
python3 - <<'PY'
from pathlib import Path
import struct
for name, version in (("java11", (3, 45)), ("java5", (0, 49))):
    output = Path("check") / name / "Legacy.class"
    assert struct.unpack(">HH", output.read_bytes()[4:8]) == version
PY
# Load ECJ through the standard Java compiler service and compile an annotation-processing client.
cat > check/MarkerProcessor.java <<'EOF'
import java.util.Set;
import javax.annotation.processing.*;
import javax.lang.model.SourceVersion;
import javax.lang.model.element.TypeElement;
import javax.tools.StandardLocation;
@SupportedAnnotationTypes("*")
@SupportedSourceVersion(SourceVersion.RELEASE_11)
public class MarkerProcessor extends AbstractProcessor {
    public boolean process(Set<? extends TypeElement> types, RoundEnvironment round) {
        if (round.processingOver()) try (var out=processingEnv.getFiler().createResource(
                StandardLocation.CLASS_OUTPUT, "", "processor-ran").openWriter()) {
            out.write("annotation processing");
        } catch (java.io.IOException ex) { throw new AssertionError(ex); }
        return false;
    }
}
EOF
cat > check/UseCompiler.java <<'EOF'
import java.util.ServiceLoader;
import javax.tools.JavaCompiler;
class UseCompiler {
    public static void main(String[] args) {
        JavaCompiler compiler = ServiceLoader.load(JavaCompiler.class).stream().map(ServiceLoader.Provider::get)
            .filter(c -> c.getClass().getName().equals("org.eclipse.jdt.internal.compiler.tool.EclipseCompiler"))
            .findFirst().orElseThrow();
        if (compiler.run(null, null, null, "-source", "11", "-target", "11", "-processorpath", "check", "-processor", "MarkerProcessor", "-d", "check/service", "check/Legacy.java") != 0)
            throw new AssertionError();
    }
}
EOF
javac --release 17 -d check check/{MarkerProcessor,UseCompiler}.java
java -cp check:build/bundles/ecj.jar UseCompiler
test "$(java -cp check/service Legacy)" = legacy
grep -Fx "annotation processing" check/service/processor-ran

%files
%license LICENSE
%{_datadir}/maven-metadata/ecj-legacy.xml
%{maven_repo}/org/eclipse/jdt/ecj/%{version}/

%changelog
%autochangelog
