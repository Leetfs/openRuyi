# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-collections3
Version:        3.2.2
Release:        %autorelease
Summary:        Apache Commons Collections 3.x for Java
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-collections/
VCS:            git:https://github.com/apache/commons-collections.git
#!RemoteAsset:  sha256:070d94fe77969d8949bd129a618e6a7bee6b83b5b5db3ef3f983395a5428b914
Source0:        https://archive.apache.org/dist/commons/collections/source/commons-collections-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  java-17-openjdk-devel
BuildRequires:  junit4

%description
The 3.x library supplies maps, collections, iterators and decorators in the
org.apache.commons.collections namespace.

%package        testlib
Summary:        Reusable collection test contracts for dependent Java libraries
Requires:       %{name} = %{version}-%{release}
Requires:       junit4

%description    testlib
The Commons Collections test support classes provide reusable JUnit
contracts for map, set and collection implementations. BeanUtils uses
BulkTest and AbstractTestMap to verify its BeanMap implementation.

%prep
%autosetup -n commons-collections-%{version}-src

%build
mkdir classes
find src/java -name '*.java' | sort > sources.list
# Java 8 added Map.remove(Object,Object) with a different return type.
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding UTF-8 -d classes @sources.list
jar --create --file commons-collections3.jar -C classes .
# Compile the test-support entry points and their actual source dependencies.
mkdir testlib-classes
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding UTF-8 \
    -cp commons-collections3.jar:%{_datadir}/java/junit4.jar -sourcepath src/test \
    -d testlib-classes src/test/org/apache/commons/collections/BulkTest.java \
    src/test/org/apache/commons/collections/map/AbstractTestMap.java
cat > testlib.mf <<MANIFEST
Manifest-Version: 1.0
Class-Path: commons-collections3.jar junit4.jar
  hamcrest1.3/hamcrest-core.jar

MANIFEST
jar --create --file commons-collections3-testlib.jar --manifest testlib.mf -C testlib-classes .

%install
install -Dpm644 commons-collections3.jar %{buildroot}%{_datadir}/java/commons-collections3.jar
install -Dpm644 commons-collections3-testlib.jar %{buildroot}%{_datadir}/java/commons-collections3-testlib.jar

%check
# Verify the bounded map from which Ehcache derives its spooling memory store.
cat > LruCheck.java <<'JAVA'
import org.apache.commons.collections.LRUMap;
class LruCheck {
    public static void main(String[] args) {
        LRUMap map = new LRUMap(2);
        map.put("a",1); map.put("b",2); map.get("a"); map.put("c",3);
        if (map.containsKey("b") || !map.containsKey("a") || map.size()!=2)
            throw new AssertionError("LRU eviction");
    }
}
JAVA
javac -cp commons-collections3.jar LruCheck.java
java -cp .:commons-collections3.jar LruCheck
# Exercise the shared test contracts with the upstream concrete HashedMap suite.
mkdir map-tests
deps=commons-collections3.jar:commons-collections3-testlib.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding UTF-8 \
    -cp "$deps" -sourcepath src/test -d map-tests \
    src/test/org/apache/commons/collections/map/TestHashedMap.java
java -cp "map-tests:$deps" org.junit.runner.JUnitCore org.apache.commons.collections.map.TestHashedMap

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/java/commons-collections3.jar

%files testlib
%license LICENSE.txt NOTICE.txt
%{_datadir}/java/commons-collections3-testlib.jar

%changelog
%autochangelog
