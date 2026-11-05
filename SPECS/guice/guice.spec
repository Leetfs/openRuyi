# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global asm_version 9.10.1

Name:           guice
Version:        5.1.0
Release:        %autorelease
Summary:        Dependency injection for Java applications
License:        Apache-2.0
URL:            https://github.com/google/guice
VCS:            git:https://github.com/google/guice.git
#!RemoteAsset:  sha256:56c5cbaa160fc9e754b8d2d93b8d8584c8468726e6b16075a6d8a0f6c61fad25
Source0:        https://github.com/google/guice/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  aopalliance
BuildRequires:  error-prone-annotations
BuildRequires:  guava
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javax-inject
BuildRequires:  jsr305
BuildRequires:  mvn(org.ow2.asm:asm) == %{asm_version}

Requires:       aopalliance
Requires:       guava
Requires:       javax-inject
Requires:       jsr305
Requires:       mvn(org.ow2.asm:asm) == %{asm_version}

%description
Guice creates and connects Java objects from declared dependency bindings.
It supports JSR 330 injection, scoped objects, providers and AOP Alliance
method interceptors.

%prep
%autosetup
find . -type f -name '*.jar' -delete

%build
mkdir classes
asm=%{_datadir}/maven-repository/org/ow2/asm/asm/%{asm_version}/asm-%{asm_version}.jar
deps=%{_datadir}/java/guava.jar:%{_datadir}/java/aopalliance.jar:%{_datadir}/java/jsr305.jar:%{_datadir}/java/javax.inject.jar:%{_datadir}/java/error-prone-annotations.jar:$asm
find core/src -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp "$deps" -d classes @sources.list
cat > guice.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}
Automatic-Module-Name: com.google.guice
Class-Path: guava.jar aopalliance.jar jsr305.jar javax.inject.jar
  ../maven-repository/org/ow2/asm/asm/%{asm_version}/asm-%{asm_version}.jar

MANIFEST
jar --create --file guice.jar --manifest guice.mf -C classes .

%install
install -Dpm644 guice.jar %{buildroot}%{_datadir}/java/guice.jar

%check
cat > CheckInject.java <<'JAVA'
import com.google.inject.*;
import com.google.inject.matcher.Matchers;
class CheckInject {
    static class Answer { @Inject Answer() {} public int value() { return 21; } }
    static class Client { @Inject Answer answer; }
    public static void main(String[] args) {
        Injector injector = Guice.createInjector(new AbstractModule() {
            protected void configure() {
                bind(Answer.class).in(Scopes.SINGLETON);
                bindInterceptor(Matchers.subclassesOf(Answer.class),
                    new com.google.inject.matcher.AbstractMatcher<java.lang.reflect.Method>() { public boolean matches(java.lang.reflect.Method method) { return method.getName().equals("value"); } }, invocation -> (Integer) invocation.proceed() * 2);
            }
        });
        Client client = injector.getInstance(Client.class);
        if (client.answer.value() != 42 || client.answer != injector.getInstance(Answer.class))
            throw new AssertionError("Injection, scope or interception");
        System.out.println("Constructor/field injection, singleton scope and bytecode interception passed");
    }
}

JAVA
asm=%{_datadir}/maven-repository/org/ow2/asm/asm/%{asm_version}/asm-%{asm_version}.jar
deps=guice.jar:%{_datadir}/java/guava.jar:%{_datadir}/java/aopalliance.jar:%{_datadir}/java/jsr305.jar:%{_datadir}/java/javax.inject.jar:$asm
javac --release 8 -cp "$deps" CheckInject.java
java -cp ".:$deps" CheckInject

%files
%license COPYING
%{_datadir}/java/guice.jar

%changelog
%autochangelog
