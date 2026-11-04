# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 66a8ae7fe741d03608b7454f994269b5c4531090

Name:           ehcache
Version:        1.5.0
Release:        %autorelease
Summary:        Ehcache memory and disk cache for Java
License:        Apache-2.0
URL:            https://www.ehcache.org/
VCS:            git:https://github.com/ehcache/ehcache2.git
#!RemoteAsset:  sha256:5139515731eb0525fc36a63baab202812139c861b640dd71a319174bbb498d0b
Source0:        https://github.com/ehcache/ehcache2/archive/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  backport-util-concurrent
BuildRequires:  commons-collections3
BuildRequires:  jsr107cache
BuildRequires:  slf4j-jcl
BuildRequires:  slf4j-jdk14
Requires:       backport-util-concurrent
Requires:       commons-collections3
Requires:       jsr107cache
Requires:       slf4j-jcl
Requires:       slf4j-jdk14

%description
Ehcache caches Java objects in memory or on disk and supplies the cache
manager, loaders and stores used by reporting applications.

%prep
%autosetup -n ehcache2-%{commit}
cp -p %{SOURCE1} LICENSE-2.0.txt

%build
mkdir classes
# Hibernate, servlet and JGroups adapters require external containers or a cluster.
# The resource loader uses the standalone cache, JCache interfaces and stores.
find core/src/main/java/net -name '*.java' ! -path '*/hibernate/*' ! -path '*/constructs/web/*' ! -path '*/distribution/jgroups/*' | sort > sources.list
cp=%{_datadir}/java/backport-util-concurrent.jar:%{_datadir}/java/jsr107cache.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/jcl-over-slf4j.jar
javac --release 8 -encoding UTF-8 -cp "$cp" -d classes @sources.list
cp -a core/src/main/resources/. classes/
printf 'Class-Path: backport-util-concurrent.jar jsr107cache.jar commons-collections3.jar jcl-over-slf4j.jar slf4j-jdk14.jar\n' > manifest.mf
jar --create --file ehcache.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 ehcache.jar %{buildroot}%{_datadir}/java/ehcache.jar

%check
# Use a live cache manager to create, read, remove and shut down a named cache.
cat > CacheSmoke.java <<'JAVA'
import net.sf.ehcache.*;
class CacheSmoke {
 public static void main(String[] args) {
  CacheManager manager = CacheManager.create();
  try {
   Cache cache=new Cache("report-wmf",2,false,false,60,60);
   manager.addCache(cache);
   cache.put(new Element("sheet","chart"));
   if(!"chart".equals(cache.get("sheet").getObjectValue()))throw new AssertionError("cache read");
   cache.remove("sheet"); if(cache.get("sheet")!=null)throw new AssertionError("cache removal");
  }finally {manager.shutdown();}
 }
}
JAVA
cp=ehcache.jar:%{_datadir}/java/backport-util-concurrent.jar:%{_datadir}/java/jsr107cache.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar
javac -cp "$cp" CacheSmoke.java
java -cp ".:$cp" CacheSmoke

%files
%license core/LICENSE.txt LICENSE-2.0.txt
%{_datadir}/java/ehcache.jar

%changelog
%autochangelog
