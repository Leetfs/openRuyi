#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
buildroot=$1
work=$PWD/target/shade-integration
repo=$work/repo
fixture=$repo/org/openruyi/check/library/1
mkdir -p "$work"/{.mvn,.xmvn,src,library-classes,target/classes} "$fixture"
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" "$buildroot/usr/share/maven-metadata/maven-shade-plugin.xml" > "$work/.xmvn/staged.xml"
cat > "$work/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$work/.xmvn/staged.xml</repository><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cd "$work"
cat > src/Used.java <<'JAVA'
package org.openruyi.fixture;
public class Used { public static String value() { return "relocated"; } }
JAVA
cat > src/Unused.java <<'JAVA'
package org.openruyi.fixture;
public class Unused {}
JAVA
cat > src/Main.java <<'JAVA'
package org.openruyi.app;
public class Main { public static void main(String[] args) { System.out.println(org.openruyi.fixture.Used.value()); } }
JAVA
javac --release 8 -d library-classes src/{Used,Unused}.java
jar cf "$fixture/library-1.jar" -C library-classes .
cat > "$fixture/library-1.pom" <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>library</artifactId><version>1</version></project>
EOF
javac --release 8 -cp "$fixture/library-1.jar" -d target/classes src/Main.java
cat > pom.xml <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>consumer</artifactId><version>1</version>
<dependencies><dependency><groupId>org.openruyi.check</groupId><artifactId>library</artifactId><version>1</version></dependency></dependencies>
<build><plugins><plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-shade-plugin</artifactId><version>3.6.1</version>
<configuration><minimizeJar>true</minimizeJar><createDependencyReducedPom>false</createDependencyReducedPom>
<relocations><relocation><pattern>org.openruyi.fixture</pattern><shadedPattern>org.openruyi.shaded</shadedPattern></relocation></relocations>
</configuration></plugin></plugins></build></project>
EOF
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="${MAVEN_OPTS:-} -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
jar_plugin=$(unzip -p /usr/share/java/javapackages-bootstrap/maven-jar-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
mvn -B -o -Dmaven.repo.local="$repo" \
    "org.apache.maven.plugins:maven-jar-plugin:$jar_plugin:jar" org.apache.maven.plugins:maven-shade-plugin:3.6.1:shade
jar tf target/consumer-1.jar > target/entries
grep -Fx org/openruyi/shaded/Used.class target/entries
if grep -E '^org/openruyi/fixture/[^/]+\.class$|/Unused\.class$' target/entries; then exit 1; fi
test "$(java -cp target/consumer-1.jar org.openruyi.app.Main)" = relocated
mvn -B -o -Dmaven.repo.local="$repo" org.apache.maven.plugins:maven-shade-plugin:3.6.1:help -Ddetail -Dgoal=shade > target/goal-help
grep -F 'minimizeJar' target/goal-help
