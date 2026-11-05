# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           j2objc-annotations
Version:        3.1
Release:        %autorelease
Summary:        Java annotations consumed by J2ObjC
License:        Apache-2.0
URL:            https://developers.google.com/j2objc/
VCS:            git:https://github.com/google/j2objc.git
#!RemoteAsset:  sha256:f19e77e8a83113323f1701139701978ceb579e6f997bcb5638d15faee3e192b4
Source0:        https://github.com/google/j2objc/archive/refs/tags/3.1.tar.gz#/j2objc-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
These Java annotations control ownership, naming and reflection when
Java libraries are translated with J2ObjC. Java applications can compile
libraries that use the annotations independently of the translator.

%prep
%autosetup -n j2objc-%{version}
find . -type f -name '*.jar' -delete

%build
mkdir classes module
find annotations/src/main/java -name '*.java' ! -name module-info.java | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
printf 'Automatic-Module-Name: com.google.j2objc.annotations\n' > manifest.mf
jar --create --file j2objc-annotations.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 j2objc-annotations.jar %{buildroot}%{_datadir}/java/j2objc-annotations.jar

%check
cat > CheckAnnotations.java <<'JAVA'
import com.google.j2objc.annotations.Weak;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;
class CheckAnnotations {
    public static void main(String[] args) {
        Class<?> annotation = Weak.class;
        if (!annotation.isAnnotation() || !annotation.isAnnotationPresent(Retention.class) ||
            !annotation.isAnnotationPresent(Target.class))
            throw new AssertionError("Annotation metadata");
    }
}
JAVA
javac --release 8 -cp j2objc-annotations.jar CheckAnnotations.java
java -cp .:j2objc-annotations.jar CheckAnnotations
jar --describe-module --file j2objc-annotations.jar | grep -F com.google.j2objc.annotations

%files
%license LICENSE
%{_datadir}/java/j2objc-annotations.jar

%changelog
%autochangelog
