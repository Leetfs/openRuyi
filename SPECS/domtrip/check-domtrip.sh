#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
root=$PWD
fixture=$root/build/xml-comparison
mkdir -p "$fixture"/{src,classes}
unzip -oq "$1" -d "$fixture/src"
unzip -oq "$2" -d "$fixture/src"
# Dom4jRoundTripTest uses dom4j SAX I/O and Jaxen. Their optional adapters for
# other document models, schema languages, and pull parsers are outside this fixture.
find "$fixture/src" -name '*.java' ! -name module-info.java ! -name XPP3Reader.java ! -name XPPReader.java \
    ! -path '*/org/dom4j/datatype/*' ! -path '*/org/dom4j/jaxb/*' ! -path '*/org/dom4j/xpp/*' \
    ! -path '*/org/jaxen/jdom/*' ! -path '*/org/jaxen/xom/*' ! -path '*/org/jaxen/javabean/*' | sort > "$fixture/sources"
jb=/usr/share/java/javapackages-bootstrap
javac --release 8 -proc:none -nowarn -encoding UTF-8 -cp "$jb/jdom2.jar" -d "$fixture/classes" @"$fixture/sources"
cp="$root/build/core/domtrip-core.jar:$root/build/maven/domtrip-maven.jar:$fixture/classes:$jb/jdom2.jar"
for jar in /usr/share/maven-repository/org/junit/platform/*/1.12.2/*.jar /usr/share/maven-repository/org/junit/jupiter/*/5.12.2/*.jar; do cp="$cp:$jar"; done
for n in junit-jupiter-params apiguardian-api opentest4j univocity-parsers; do cp="$cp:$jb/$n.jar"; done
for mod in core maven; do
    cd "$root/$mod"
    out=$root/build/$mod/tests
    mkdir -p "$out"
    # The upstream JMH performance driver is separate from the test suite.
    find src/test/java -name '*.java' ! -name ParserBenchmark.java | sort > "$out/sources"
    javac --release 21 -g -proc:none -encoding UTF-8 -cp "$cp" -d "$out" @"$out/sources" /usr/libexec/eclipse-equinox/RunJupiter.java
    tests=$(find src/test/java -name '*Test.java' | sed 's|^src/test/java/||;s|/|.|g;s|[.]java$||')
    java -cp "$out:$cp" RunJupiter $tests
done
