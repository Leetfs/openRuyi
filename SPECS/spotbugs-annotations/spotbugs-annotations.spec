# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spotbugs-annotations
Version:        4.10.5
Release:        %autorelease
Summary:        Annotations for SpotBugs static analysis
License:        LGPL-2.1-or-later
URL:            https://github.com/spotbugs/spotbugs
VCS:            git:https://github.com/spotbugs/spotbugs.git
#!RemoteAsset:  sha256:f3295529934ed258c26cc8ab0a9af73a32ad25ddc5c9a34b54c3cad644c27be8
Source0:        https://github.com/spotbugs/spotbugs/archive/refs/tags/%{version}.tar.gz#/spotbugs-annotations-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  jsr305

Requires:       jsr305

%description
SpotBugs annotations describe nullability, resource ownership and warning
suppression. They are usable without installing the analysis engine.

%prep
%autosetup -n spotbugs-%{version}

%build
mkdir classes
find spotbugs-annotations/src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/jsr305.jar -d classes @sources.list
cat > annotations.mf <<MANIFEST
Manifest-Version: 1.0
Class-Path: jsr305.jar

MANIFEST
jar --create --file spotbugs-annotations.jar --manifest annotations.mf -C classes .

%install
install -Dpm644 spotbugs-annotations.jar %{buildroot}%{_datadir}/java/spotbugs-annotations.jar

%check
# Check warning-suppression metadata and compile its use in a consumer.
cat > AnnotationCheck.java <<'JAVA'
import java.lang.annotation.*;
import edu.umd.cs.findbugs.annotations.*;
@SuppressFBWarnings(value="EI_EXPOSE_REP", justification="Test fixture")
class AnnotationCheck {
    public static void main(String[] args) throws Exception {
        if (SuppressFBWarnings.class.getAnnotation(Retention.class).value() != RetentionPolicy.CLASS)
            throw new AssertionError("suppression retention");
        if (!SuppressFBWarnings.class.getMethod("value").getReturnType().equals(String[].class))
            throw new AssertionError("suppression values");
    }
}
JAVA
javac -cp spotbugs-annotations.jar:%{_datadir}/java/jsr305.jar AnnotationCheck.java
java -cp .:spotbugs-annotations.jar:%{_datadir}/java/jsr305.jar AnnotationCheck

%files
%license LICENSE
%doc spotbugs-annotations/README.md
%{_datadir}/java/spotbugs-annotations.jar

%changelog
%autochangelog
