#!/bin/sh
set -eu
buildroot=$1
mvn=$2
version=$3
sig=$PWD/animal-sniffer/src/test/resources/java16-1.1.signature
staging=$PWD/plugin-test
mkdir -p "$staging/.xmvn" "$staging/target/classes"
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" \
    "$buildroot/usr/share/maven-metadata/animal-sniffer.xml" > "$staging/.xmvn/plugin.xml"
cat > "$staging/.xmvn/signature.xml" <<EOF
<metadata><artifacts><artifact><groupId>org.openruyi.test</groupId><artifactId>java16</artifactId>
<extension>signature</extension><version>1.1</version><path>$sig</path></artifact></artifacts></metadata>
EOF
cat > "$staging/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$staging/.xmvn/plugin.xml</repository>
  <repository>$staging/.xmvn/signature.xml</repository>
  <repository>/usr/share/maven-metadata</repository>
  <repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cd "$staging"
cat > pom.xml <<EOF
<project>
  <modelVersion>4.0.0</modelVersion><groupId>org.openruyi.test</groupId>
  <artifactId>signature-check</artifactId><version>1</version>
  <build><plugins><plugin>
    <groupId>org.codehaus.mojo</groupId><artifactId>animal-sniffer-maven-plugin</artifactId><version>$version</version>
    <configuration><signature>
      <groupId>org.openruyi.test</groupId><artifactId>java16</artifactId><version>1.1</version>
    </signature></configuration>
  </plugin></plugins></build>
</project>
EOF
cat > Fixture.java <<'EOF'
public class Fixture {
    public int length(String text) { return text.length(); }
}
EOF
javac --release 8 -d target/classes Fixture.java
goal="org.codehaus.mojo:animal-sniffer-maven-plugin:$version:check"
"$mvn" --offline --batch-mode "-Dmaven.repo.local=$staging/repository" "$goal"
"$mvn" --offline --batch-mode "-Dmaven.repo.local=$staging/repository" org.codehaus.mojo:animal-sniffer-maven-plugin:SYSTEM:check
cat > Fixture.java <<'EOF'
public class Fixture {
    public String strip(String text) { return text.strip(); }
}
EOF
javac --release 11 -d target/classes Fixture.java
if "$mvn" --offline --batch-mode "-Dmaven.repo.local=$staging/repository" "$goal" > rejected.log 2>&1; then
    exit 1
fi
grep -E 'Undefined reference:.*String\.strip\(' rejected.log
