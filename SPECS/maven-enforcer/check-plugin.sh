#!/bin/sh
set -eu
buildroot=$1
mvn=$2
version=$3
metadata=$4
staging=$PWD/plugin-test
mkdir -p "$staging/.xmvn"
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" \
    "$buildroot/usr/share/maven-metadata/$metadata.xml" > "$staging/.xmvn/enforcer.xml"
# The default alias belongs to the current release. Register both versions for the consumer.
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" \
    "$buildroot/usr/share/maven-metadata/maven-enforcer.xml" > "$staging/.xmvn/default.xml"
cat > "$staging/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$staging/.xmvn/enforcer.xml</repository>
  <repository>$staging/.xmvn/default.xml</repository>
  <repository>/usr/share/maven-metadata</repository>
  <repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > "$staging/pom.xml" <<EOF
<project>
  <modelVersion>4.0.0</modelVersion><groupId>org.openruyi.test</groupId>
  <artifactId>enforcer-expression</artifactId><version>1</version>
  <build><plugins><plugin>
    <groupId>org.apache.maven.plugins</groupId><artifactId>maven-enforcer-plugin</artifactId><version>$version</version>
    <configuration><rules><evaluateBeanshell>
      <condition>6 * 7 == \${expected}</condition><message>arithmetic condition failed</message>
    </evaluateBeanshell></rules></configuration>
  </plugin></plugins></build>
</project>
EOF
cd "$staging"
goal="org.apache.maven.plugins:maven-enforcer-plugin:$version:enforce"
"$mvn" --batch-mode --offline "-Dmaven.repo.local=$staging/repository" -Dexpected=42 "$goal"
"$mvn" --batch-mode --offline "-Dmaven.repo.local=$staging/repository" -Dexpected=42 org.apache.maven.plugins:maven-enforcer-plugin:SYSTEM:enforce
if "$mvn" --batch-mode --offline "-Dmaven.repo.local=$staging/repository" -Dexpected=41 "$goal" > rejected.log 2>&1; then
    exit 1
fi
grep -F 'arithmetic condition failed' rejected.log
