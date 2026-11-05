# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jetbrains-annotations
Version:        26.1.0
Release:        %autorelease
Summary:        JetBrains annotations for Java code analysis
License:        Apache-2.0
URL:            https://github.com/JetBrains/java-annotations
VCS:            git:https://github.com/JetBrains/java-annotations.git
#!RemoteAsset:  sha256:07b7d2490ee5fbdcb8c153b58cb0adfd9d72fbc5f94f43d71c67b52e35d9f07c
Source0:        https://github.com/JetBrains/java-annotations/archive/refs/tags/%{version}.tar.gz#/jetbrains-annotations-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
JetBrains annotations describe nullability, contracts, mutability and API
usage for Java IDEs, compilers and static analysis tools.

%prep
%autosetup -n java-annotations-%{version}

%build
mkdir classes
find src/jvmMain/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
cat > annotations.mf <<MANIFEST
Manifest-Version: 1.0
Automatic-Module-Name: org.jetbrains.annotations

MANIFEST
jar --create --file jetbrains-annotations.jar --manifest annotations.mf -C classes .

%install
install -Dpm644 jetbrains-annotations.jar %{buildroot}%{_datadir}/java/jetbrains-annotations.jar

%check
# Verify the nullability and contract metadata consumed by Java libraries.
cat > AnnotationCheck.java <<'JAVA'
import java.lang.annotation.*;
import org.jetbrains.annotations.*;
class AnnotationCheck {
    public static void main(String[] args) {
        for (Class<?> type : new Class<?>[]{NotNull.class, Nullable.class, Contract.class}) {
            if (type.getAnnotation(Retention.class).value() != RetentionPolicy.CLASS)
                throw new AssertionError(type);
        }
        boolean typeUse = false;
        for (ElementType value : NotNull.class.getAnnotation(Target.class).value())
            typeUse |= value == ElementType.TYPE_USE;
        if (!typeUse) throw new AssertionError("type-use annotation");
    }
}
JAVA
javac -cp jetbrains-annotations.jar AnnotationCheck.java
java -cp .:jetbrains-annotations.jar AnnotationCheck

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/java/jetbrains-annotations.jar

%changelog
%autochangelog
