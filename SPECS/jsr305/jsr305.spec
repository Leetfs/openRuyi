# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jsr305
Version:        0.1~svn51
Release:        %autorelease
Summary:        Java annotations for static analysis
License:        BSD-3-Clause
URL:            https://code.google.com/archive/p/jsr-305/
# VCS: No VCS link available
# The expert group's final SVN snapshot contains the reference implementation and its license.
#!RemoteAsset:  sha256:4f29730ba2229df8af699ee139486bf5593052d2fcc2bd0fc3cfe121fd76025b
Source0:        https://storage.googleapis.com/google-code-archive-source/v2/code.google.com/jsr-305/source-archive.zip#/%{name}-r51.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip

%description
JSR 305 defines Java annotations for nullness, concurrency and other
properties used by static analysis tools. It also provides meta-annotations
for declaring type qualifiers and their defaults.

%prep
%setup -q -T -c
unzip -q %{SOURCE0} 'jsr-305/trunk/ri/src/main/java/*.java' jsr-305/trunk/ri/LICENSE

%build
mkdir classes
find jsr-305/trunk/ri/src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
jar --create --file jsr305.jar -C classes .

%install
install -Dpm644 jsr305.jar %{buildroot}%{_datadir}/java/jsr305.jar

%check
cat > Qualifiers.java <<'JAVA'
import javax.annotation.Nonnull;
import javax.annotation.ParametersAreNonnullByDefault;
import javax.annotation.concurrent.GuardedBy;
import javax.annotation.meta.TypeQualifier;
import javax.annotation.meta.When;

@ParametersAreNonnullByDefault
class Qualifiers {
    @GuardedBy("this") Object value;
    @Nonnull public String name() { return "valid"; }
    public static void main(String[] args) throws Exception {
        Nonnull n = Qualifiers.class.getMethod("name").getAnnotation(Nonnull.class);
        if (n.when() != When.ALWAYS || !Nonnull.class.isAnnotationPresent(TypeQualifier.class))
            throw new AssertionError("Runtime qualifier metadata");
        if (!Qualifiers.class.isAnnotationPresent(ParametersAreNonnullByDefault.class))
            throw new AssertionError("Default qualification");
        Nonnull.Checker checker = new Nonnull.Checker();
        if (checker.forConstantValue(n, null) != When.NEVER ||
            checker.forConstantValue(n, "valid") != When.ALWAYS)
            throw new AssertionError("Constant qualification");
    }
}
JAVA
javac --release 8 -cp jsr305.jar Qualifiers.java
java -cp .:jsr305.jar Qualifiers

%files
%license jsr-305/trunk/ri/LICENSE
%{_datadir}/java/jsr305.jar

%changelog
%autochangelog
