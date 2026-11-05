# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           javax-inject
Version:        1
Release:        %autorelease
Summary:        Dependency injection annotations for Java
License:        Apache-2.0
URL:            https://javax-inject.github.io/javax-inject/
VCS:            git:https://github.com/javax-inject/javax-inject.git
#!RemoteAsset:  sha256:aa437908aa6b50f2a6fe30bade6495ab1195c3ec4d7708a66afc97f2edeee766
Source0:        https://github.com/javax-inject/javax-inject/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4

%description
JSR 330 provides the javax.inject annotations and the Provider interface
used to describe constructors, bindings, qualifiers and scopes to a
dependency injection container.

%prep
%autosetup
find . -name '*.jar' -type f -delete
cp -p %{SOURCE1} LICENSE.txt

%build
mkdir classes
javac --release 8 -encoding UTF-8 -d classes src/javax/inject/*.java
jar --create --file javax.inject.jar -C classes .

%install
install -Dpm644 javax.inject.jar %{buildroot}%{_datadir}/java/javax.inject.jar

%check
# Compile the upstream technology compatibility kit against the packaged API.
mkdir tck-classes
find tck -name '*.java' | sort > tck.list
javac --release 8 -encoding UTF-8 -cp javax.inject.jar:%{_datadir}/java/junit4.jar -d tck-classes @tck.list
cat > Injection.java <<'JAVA'
import javax.inject.*;
class Injection {
    @Inject Injection(@Named("answer") Provider<Integer> answer) {
        if (answer.get() != 42) throw new AssertionError();
    }
    public static void main(String[] args) throws Exception {
        java.lang.reflect.Constructor<?> constructor = Injection.class.getDeclaredConstructor(Provider.class);
        if (!constructor.isAnnotationPresent(Inject.class)) throw new AssertionError("@Inject");
        Named key = constructor.getParameters()[0].getAnnotation(Named.class);
        if (!key.value().equals("answer") || !Named.class.isAnnotationPresent(Qualifier.class))
            throw new AssertionError("Qualified parameter");
        new Injection(() -> 42);
    }
}
JAVA
javac --release 8 -cp javax.inject.jar Injection.java
java -cp .:javax.inject.jar Injection

%files
%license LICENSE.txt
%{_datadir}/java/javax.inject.jar

%changelog
%autochangelog
