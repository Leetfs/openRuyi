# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           javapoet-palantir
Version:        0.22.0
Release:        %autorelease
Summary:        Palantir Java source generation library
License:        Apache-2.0
URL:            https://github.com/palantir/javapoet
VCS:            git:https://github.com/palantir/javapoet.git
#!RemoteAsset:  sha256:ce4f59ec52517bf247c420062897bf0013eeac558fbed67e7c713773ca799612
Source0:        https://github.com/palantir/javapoet/archive/refs/tags/%{version}.tar.gz#/javapoet-palantir-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
JavaPoet builds Java source files from models of classes, methods,
statements and types. This package provides the Palantir namespace
used by Java source generators such as Caffeine.

%prep
%autosetup -n javapoet-%{version}

%build
mkdir classes
find javapoet/src/main/java -name '*.java' | sort > sources.list
javac --release 17 -encoding UTF-8 -d classes @sources.list
cat > javapoet.mf <<MANIFEST
Manifest-Version: 1.0
Automatic-Module-Name: com.palantir.javapoet

MANIFEST
jar --create --file javapoet-palantir.jar --manifest javapoet.mf -C classes .

%install
install -Dpm644 javapoet-palantir.jar %{buildroot}%{_datadir}/java/javapoet-palantir.jar

%check
# Generate, compile and execute a class through the public source-generation API.
# The upstream suite also requires Compile Testing, Jimfs, Mockito and AssertJ.
cat > GeneratorCheck.java <<'JAVA'
import com.palantir.javapoet.*;
import java.nio.file.Path;
import javax.lang.model.element.Modifier;
class GeneratorCheck {
    public static void main(String[] args) throws Exception {
        MethodSpec main = MethodSpec.methodBuilder("main")
            .addModifiers(Modifier.PUBLIC, Modifier.STATIC)
            .returns(void.class).addParameter(String[].class, "args")
            .addStatement("$T.out.println($L)", System.class, 42).build();
        TypeSpec type = TypeSpec.classBuilder("GeneratedAnswer")
            .addModifiers(Modifier.PUBLIC).addMethod(main).build();
        JavaFile.builder("generated", type).build().writeTo(Path.of("output"));
    }
}
JAVA
javac -cp javapoet-palantir.jar GeneratorCheck.java
java -cp .:javapoet-palantir.jar GeneratorCheck
javac output/generated/GeneratedAnswer.java
test "$(java -cp output generated.GeneratedAnswer)" = 42

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/java/javapoet-palantir.jar

%changelog
%autochangelog
