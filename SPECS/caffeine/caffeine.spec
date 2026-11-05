# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           caffeine
Version:        3.3.1
Release:        %autorelease
Summary:        High-performance in-memory cache for Java
License:        Apache-2.0
URL:            https://github.com/ben-manes/caffeine
VCS:            git:https://github.com/ben-manes/caffeine.git
#!RemoteAsset:  sha256:b27bdcb637056eb5a1def448eb470edbaa5e1d78335b9e08fa85d7a933846397
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  jspecify
BuildRequires:  error-prone-annotations
BuildRequires:  guava
BuildRequires:  commons-lang3
BuildRequires:  javapoet-palantir
BuildRequires:  spotbugs-annotations

%description
Caffeine supplies synchronous and asynchronous caches with bounded size,
expiration, automatic loading and cache statistics.

%prep
%autosetup

%build
mkdir generator-classes classes generated
lang3jar=$(find %{_datadir}/maven-repository/org/apache/commons/commons-lang3 -name '*.jar' -print -quit)
test -n "$lang3jar"
deps=%{_datadir}/java/guava.jar:%{_datadir}/java/javapoet-palantir.jar:$lang3jar:%{_datadir}/java/jspecify.jar:%{_datadir}/java/error-prone-annotations.jar:%{_datadir}/java/spotbugs-annotations.jar
find caffeine/src/javaPoet/java -name '*.java' | sort > generator.list
javac --release 25 -encoding UTF-8 -cp "$deps" -d generator-classes @generator.list
cp -a caffeine/src/javaPoet/resources/. generator-classes/
# Generate all cache and node variants from the upstream JavaPoet templates.
java -cp "generator-classes:$deps" com.github.benmanes.caffeine.cache.NodeFactoryGenerator generated/nodes
java -cp "generator-classes:$deps" com.github.benmanes.caffeine.cache.LocalCacheFactoryGenerator generated/caches
find caffeine/src/main/java generated -name '*.java' | sort > sources.list
javac --release 25 -encoding UTF-8 -cp "$deps" -d classes @sources.list
cat > caffeine.mf <<MANIFEST
Manifest-Version: 1.0
Automatic-Module-Name: com.github.benmanes.caffeine

MANIFEST
jar --create --file caffeine.jar --manifest caffeine.mf -C classes .

%install
install -Dpm644 caffeine.jar %{buildroot}%{_datadir}/java/caffeine.jar

%check
# Exercise bounded eviction, deterministic expiration, loading and asynchronous access.
# The upstream suites additionally require Truth, Mockito, Lincheck and test adapters.
cat > CacheCheck.java <<'JAVA'
import com.github.benmanes.caffeine.cache.*;
import java.time.Duration;
import java.util.concurrent.atomic.AtomicLong;
class CacheCheck {
    public static void main(String[] args) {
        AtomicLong clock=new AtomicLong();
        LoadingCache<Integer,Integer> cache=Caffeine.newBuilder()
            .maximumSize(3).expireAfterWrite(Duration.ofSeconds(1))
            .ticker(clock::get).executor(Runnable::run).recordStats().build(k -> k*2);
        if (cache.get(21)!=42 || cache.get(21)!=42 || cache.stats().hitCount()!=1)
            throw new AssertionError("loading or statistics");
        for (int i=0;i<100;i++) cache.get(i);
        cache.cleanUp();
        if (cache.estimatedSize()>3) throw new AssertionError("bounded eviction");
        clock.set(2_000_000_000L); cache.cleanUp();
        if (cache.estimatedSize()!=0) throw new AssertionError("expiration");
        AsyncLoadingCache<Integer,Integer> async=Caffeine.newBuilder()
            .executor(Runnable::run).buildAsync(k -> k+1);
        if (async.get(41).join()!=42) throw new AssertionError("async loading");
    }
}
JAVA
javac -cp caffeine.jar CacheCheck.java
java -cp .:caffeine.jar CacheCheck

%files
%license LICENSE
%doc README.md
%{_datadir}/java/caffeine.jar

%changelog
%autochangelog
