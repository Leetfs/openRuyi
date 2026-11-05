# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           guava
Version:        33.8.0
Release:        %autorelease
Summary:        Core Java collections, caches and concurrency utilities
License:        Apache-2.0 AND CC0-1.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://guava.dev/
VCS:            git:https://github.com/google/guava.git
#!RemoteAsset:  sha256:051b81386baa644dab1a88555f74c301f271f8f496a5f6ff9530ca6bb7fe181f
Source0:        https://github.com/google/guava/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499
Source1:        https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt#/CC0-1.0.txt
BuildArch:      noarch

BuildRequires:  error-prone-annotations
BuildRequires:  j2objc-annotations
BuildRequires:  java-25-openjdk-devel
BuildRequires:  jspecify

Requires:       error-prone-annotations
Requires:       j2objc-annotations
Requires:       jspecify

%description
Guava supplies immutable collections, local caches, reflection helpers,
string utilities and listenable futures for Java applications. The package
includes its failureaccess module for sharing Future failure information.

%prep
%autosetup
find . -type f -name '*.jar' -delete
cp %{SOURCE1} CC0-1.0.txt
# Preserve the original public-domain and CC0 dedications in the shipped sources.
{
    echo 'Original notices from Guava source files:'
    for path in base/SmallCharMatcher.java collect/Hashing.java; do
        echo "$path"
        sed -n '/MurmurHash3 was written/,+1p' "guava/src/com/google/common/$path"
    done
    echo 'util/concurrent/Striped.java'
    sed -n '/This method was written by Doug Lea/,+2p' guava/src/com/google/common/util/concurrent/Striped.java
    for name in AtomicDouble AtomicDoubleArray MoreExecutors; do
        echo "util/concurrent/$name.java"
        sed -n '/Written by Doug Lea/,+3p' "guava/src/com/google/common/util/concurrent/$name.java"
    done
} > THIRD-PARTY-NOTICES.txt
grep -F 'Austin Appleby' THIRD-PARTY-NOTICES.txt
grep -F 'creativecommons.org/publicdomain/zero/1.0/' THIRD-PARTY-NOTICES.txt

%build
mkdir failure-classes failure-module guava-classes guava-module
find futures/failureaccess/src -name '*.java' ! -name module-info.java | sort > failure.sources
javac --release 8 -encoding UTF-8 -d failure-classes @failure.sources
javac --release 9 --patch-module com.google.common.util.concurrent.internal=failure-classes \
    -d failure-module futures/failureaccess/src/module-info.java
jar --create --file failureaccess.jar -C failure-classes . --release 9 -C failure-module module-info.class
deps=%{_datadir}/java/error-prone-annotations.jar:%{_datadir}/java/jspecify.jar:%{_datadir}/java/j2objc-annotations.jar:failureaccess.jar
find guava/src -name '*.java' ! -name module-info.java | sort > guava.sources
# The upstream Java 8 implementation uses sun.misc.Unsafe with a portable fallback.
javac -source 8 -target 8 -encoding UTF-8 -cp "$deps" -d guava-classes @guava.sources
javac --release 9 --module-path "$deps" --patch-module com.google.common=guava-classes \
    -d guava-module guava/src/module-info.java
printf 'Class-Path: failureaccess.jar\nImplementation-Version: %{version}\n' > guava.mf
jar --create --file guava.jar --manifest guava.mf -C guava-classes . --release 9 -C guava-module module-info.class

%install
install -Dpm644 guava.jar %{buildroot}%{_datadir}/java/guava.jar
install -Dpm644 failureaccess.jar %{buildroot}%{_datadir}/java/failureaccess.jar

%check
# Exercise immutable collections, cache loading and listenable futures.
cat > CheckGuava.java <<'JAVA'
import com.google.common.base.Joiner;
import com.google.common.cache.*;
import com.google.common.collect.ImmutableList;
import com.google.common.util.concurrent.*;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.atomic.AtomicInteger;

class CheckGuava {
    public static void main(String[] args) throws Exception {
        ImmutableList<String> names = ImmutableList.of("left", "right");
        if (!Joiner.on("/").join(names).equals("left/right")) throw new AssertionError("Join");
        try {
            names.add("unexpected");
            throw new AssertionError("Mutable immutable list");
        } catch (UnsupportedOperationException expected) {}
        AtomicInteger loads = new AtomicInteger();
        LoadingCache<String, Integer> cache = CacheBuilder.newBuilder().build(
            new CacheLoader<String, Integer>() {
                public Integer load(String key) { loads.incrementAndGet(); return 42; }
            });
        if (cache.get("answer") != 42 || cache.get("answer") != 42 || loads.get() != 1)
            throw new AssertionError("Cache loader");
        SettableFuture<Integer> result = SettableFuture.create();
        ListenableFuture<Integer> doubled = Futures.transform(result, n -> n * 2, MoreExecutors.directExecutor());
        result.set(21);
        if (doubled.get() != 42) throw new AssertionError("Future transformation");
        SettableFuture<Integer> failure = SettableFuture.create();
        failure.setException(new IllegalStateException("expected"));
        try {
            failure.get();
            throw new AssertionError("Lost future failure");
        } catch (ExecutionException expected) {
            if (!(expected.getCause() instanceof IllegalStateException)) throw expected;
        }
    }
}
JAVA
deps=guava.jar:failureaccess.jar:%{_datadir}/java/error-prone-annotations.jar:%{_datadir}/java/jspecify.jar:%{_datadir}/java/j2objc-annotations.jar
javac --release 8 -cp "$deps" CheckGuava.java
java -cp ".:$deps" CheckGuava
jar --describe-module --file guava.jar --release 9 | grep -F com.google.common
jar --describe-module --file failureaccess.jar --release 9 | grep -F com.google.common.util.concurrent.internal

%files
%license LICENSE CC0-1.0.txt THIRD-PARTY-NOTICES.txt
%doc README.md
%{_datadir}/java/guava.jar
%{_datadir}/java/failureaccess.jar

%changelog
%autochangelog
