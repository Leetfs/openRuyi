# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jspecify
Version:        1.0.1
Release:        %autorelease
Summary:        Nullness annotations for Java APIs
License:        Apache-2.0
URL:            https://jspecify.dev/
VCS:            git:https://github.com/jspecify/jspecify.git
#!RemoteAsset:  sha256:664956dec926660890ea03a7b154102e7775e791a17f50c7bfb8abbbb1089f99
Source0:        https://github.com/jspecify/jspecify/archive/refs/tags/v1.0.1.tar.gz#/jspecify-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
JSpecify defines annotations for nullable and non-null Java types and
for the default nullness of a package, class or method.

%prep
%autosetup -n jspecify-%{version}
find . -type f -name '*.jar' -delete

%build
mkdir classes module
find src/main/java -name '*.java' ! -name module-info.java | sort > sources.list
# Upstream targets Java 8 bytecode while allowing ElementType.MODULE from newer JDKs.
javac -source 8 -target 8 -encoding UTF-8 -d classes @sources.list
javac --release 9 --patch-module org.jspecify=classes -d module src/java9/java/module-info.java
jar --create --file jspecify.jar -C classes . -C module module-info.class

%install
install -Dpm644 jspecify.jar %{buildroot}%{_datadir}/java/jspecify.jar

%check
cat > CheckAnnotations.java <<'JAVA'
import org.jspecify.annotations.NullMarked;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;
class CheckAnnotations {
    public static void main(String[] args) {
        Class<?> annotation = NullMarked.class;
        if (!annotation.isAnnotation() || !annotation.isAnnotationPresent(Retention.class) ||
            !annotation.isAnnotationPresent(Target.class))
            throw new AssertionError("Annotation metadata");
    }
}
JAVA
javac --release 8 -cp jspecify.jar CheckAnnotations.java
java -cp .:jspecify.jar CheckAnnotations
jar --describe-module --file jspecify.jar | grep -F org.jspecify

%files
%license LICENSE
%{_datadir}/java/jspecify.jar

%changelog
%autochangelog
