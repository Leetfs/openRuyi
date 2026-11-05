# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           error-prone-annotations
Version:        2.52.0
Release:        %autorelease
Summary:        Java annotations for Error Prone static analysis
License:        Apache-2.0
URL:            https://errorprone.info/
VCS:            git:https://github.com/google/error-prone.git
#!RemoteAsset:  sha256:6c3e6900edd0cd075d0aa98e5f221a76ec4cdad726afb50e5da6f12ea081e144
Source0:        https://github.com/google/error-prone/archive/refs/tags/v2.52.0.tar.gz#/error-prone-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
Error Prone annotations describe API contracts such as return value checks,
immutable types and synchronization requirements to Java compilers and
static analysis tools.

%prep
%autosetup -n error-prone-%{version}
find . -type f -name '*.jar' -delete

%build
mkdir classes module
find annotations/src/main/java -name '*.java' ! -name module-info.java | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
javac --release 9 --patch-module com.google.errorprone.annotations=classes -d module annotations/src/main/java/module-info.java
jar --create --file error-prone-annotations.jar -C classes . --release 9 -C module module-info.class

%install
install -Dpm644 error-prone-annotations.jar %{buildroot}%{_datadir}/java/error-prone-annotations.jar

%check
cat > CheckAnnotations.java <<'JAVA'
import com.google.errorprone.annotations.CheckReturnValue;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;
class CheckAnnotations {
    public static void main(String[] args) {
        Class<?> annotation = CheckReturnValue.class;
        if (!annotation.isAnnotation() || !annotation.isAnnotationPresent(Retention.class) ||
            !annotation.isAnnotationPresent(Target.class))
            throw new AssertionError("Annotation metadata");
    }
}
JAVA
javac --release 8 -cp error-prone-annotations.jar CheckAnnotations.java
java -cp .:error-prone-annotations.jar CheckAnnotations
jar --describe-module --file error-prone-annotations.jar --release 9 | grep -F com.google.errorprone.annotations

%files
%license COPYING
%{_datadir}/java/error-prone-annotations.jar

%changelog
%autochangelog
