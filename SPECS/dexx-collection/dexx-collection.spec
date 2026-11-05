# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dexx-collection
Version:        0.7
Release:        %autorelease
Summary:        Persistent immutable collections for Java
License:        MIT AND BSD-3-Clause
URL:            https://github.com/andrewoma/dexx
VCS:            git:https://github.com/andrewoma/dexx.git
#!RemoteAsset:  sha256:543572828b62c7e8ae463c0de31d19bd598620d665eaeb257ac239212d148087
Source0:        https://github.com/andrewoma/dexx/archive/refs/tags/%{version}.tar.gz#/dexx-collection-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  jetbrains-annotations

%description
Dexx provides persistent maps, sets, vectors and lists. Updates return a
new collection while preserving the previous contents for other users.

%prep
%autosetup -n dexx-%{version}

%build
mkdir classes
find collection/src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/jetbrains-annotations.jar -d classes @sources.list
jar --create --file dexx-collection.jar -C classes .

%install
install -Dpm644 dexx-collection.jar %{buildroot}%{_datadir}/java/dexx-collection.jar

%check
# Check persistent map updates, removal and iteration as used by RDF indexes.
# The upstream test suite requires Kotlin; this exercises the Java public API.
cat > PersistentMapCheck.java <<'JAVA'
import com.github.andrewoma.dexx.collection.HashMap;
import com.github.andrewoma.dexx.collection.Pair;
class PersistentMapCheck {
    public static void main(String[] args) {
        HashMap<Integer, Integer> empty = HashMap.empty();
        HashMap<Integer, Integer> map = empty;
        for (int i=0; i<10000; i++) map=map.put(i, i*2);
        HashMap<Integer, Integer> changed=map.remove(42).put(10000, 7);
        if (empty.size()!=0 || map.size()!=10000 || changed.size()!=10000)
            throw new AssertionError("persistent sizes");
        if (map.get(42)!=84 || changed.get(42)!=null || map.get(10000)!=null)
            throw new AssertionError("old map changed");
        long sum=0;
        for (Pair<Integer,Integer> entry : map) sum+=entry.component2();
        if (sum!=99990000) throw new AssertionError("iteration");
    }
}
JAVA
javac -cp dexx-collection.jar PersistentMapCheck.java
java -cp .:dexx-collection.jar PersistentMapCheck

%files
%license LICENSE.txt NOTICE.txt licenses/LICENSE_Scala.txt
%doc README.md
%{_datadir}/java/dexx-collection.jar

%changelog
%autochangelog
