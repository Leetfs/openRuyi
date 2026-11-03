# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# The SDK uses the default lifecycle and its own verification and repository profiles.
%global sdk_projects !:tycho-baseline-plugin,!:tycho-sbom,!:tycho-gpg-plugin,!:tycho-version-bump-plugin,!:tycho-cleancode-plugin
%global enforcer_version 3.6.2
%global jetty_version 12.1.14
%global revision 14bb695163b412b2a18258983e535b831db4bf21
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
%global repo_dir %{_datadir}/maven-repository

Name:           tycho
Version:        5.0.3
Release:        %autorelease
Summary:        Maven plugins for building Eclipse components
License:        EPL-2.0 AND EPL-1.0
URL:            https://eclipse.dev/tycho/
VCS:            git:https://github.com/eclipse-tycho/tycho
#!RemoteAsset:  sha256:2649bcbd262c0442421086fdf828936381feffed83de703024df40d928bc17a2
Source0:        https://github.com/eclipse-tycho/tycho/archive/refs/tags/tycho-%{version}.tar.gz
Source1:        install-reactor.py
# Bind the optional UI test entry point to the workbench supplied by the target application.
Patch2000:      2000-Resolve-the-target-workbench-when-UI-tests-start.patch
Patch2001:      2001-filter-tycho-test-properties-with-resources.patch
Patch2002:      2002-resolve-tools-in-their-runtime-context.patch
BuildArch:      noarch

BuildRequires:  mvn(org.apache.commons:commons-compress:jar:sources) == 1.28.0
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven:apache-maven:tar.gz:bin) == 3.9.16
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin) == 3.5.0
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin) == 7.2.3
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bnd.embedded-repo) == 7.2.3
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.repository) == 7.2.3
BuildRequires:  mvn(ch.digitalfondue.jfiveparse:jfiveparse) == 2.0.0
BuildRequires:  mvn(io.github.java-diff-utils:java-diff-utils) == 4.17
BuildRequires:  mvn(io.takari.polyglot:polyglot-common) == 0.8.1
BuildRequires:  mvn(org.apache.commons:commons-exec) == 1.6.0
BuildRequires:  mvn(commons-net:commons-net) == 3.13.0
BuildRequires:  mvn(de.pdark:decentxml) == 1.4
BuildRequires:  mvn(org.apache.maven.indexer:search-backend-smo) == 7.1.6
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin) == %{enforcer_version}
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin) == 3.1.4
BuildRequires:  mvn(org.apache.maven.surefire:surefire-grouper) == 3.5.5
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin) == 3.5.5
BuildRequires:  mvn(org.apache.maven.surefire:surefire-api) == 3.5.5
BuildRequires:  mvn(org.apache.servicemix.tooling:depends-maven-plugin) == 1.5.0
BuildRequires:  mvn(org.codehaus.mojo:animal-sniffer-annotations) == 1.27
BuildRequires:  mvn(io.takari.maven:takari-smart-builder) == 1.1.0
BuildRequires:  mvn(org.eclipse.jdt:org.eclipse.jdt.core) == 3.45.0
BuildRequires:  mvn(org.eclipse.jetty:jetty-http) == %{jetty_version}
BuildRequires:  mvn(org.eclipse.jetty:jetty-server) == %{jetty_version}
BuildRequires:  mvn(org.eclipse.jetty.ee10:jetty-ee10-servlet) == %{jetty_version}
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit) == 7.6.0.202603022253-r
BuildRequires:  mvn(org.apache.bcel:bcel) == 6.12.0
BuildRequires:  mvn(org.eclipse.jdt:org.eclipse.jdt.launching.macosx) == 3.6.400
BuildRequires:  mvn(org.eclipse.pde:org.eclipse.pde.api.tools) == 1.3.1100
BuildRequires:  mvn(org.eclipse.pde:org.eclipse.pde.core) == 3.21.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.e4.ui.workbench3) == 0.18.0
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.p2.director.app) == 1.3.900
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.p2.metadata) == 2.9.600
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.p2.publisher) == 1.9.600
BuildRequires:  mvn(org.osgi:org.osgi.namespace.extender) == 1.0.1
BuildRequires:  mvn(org.osgi:org.osgi.namespace.implementation) == 1.0.0
BuildRequires:  mvn(org.osgi:org.osgi.service.component.annotations) == 1.5.1
BuildRequires:  mvn(org.osgi:org.osgi.service.repository) == 1.1.0
BuildRequires:  mvn(org.tukaani:xz) == 1.12
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-named-locks) == 1.9.27
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  xmlstarlet
Provides:       mvn(org.eclipse.tycho:tycho-build) == %{version}
Requires:       mvn(commons-net:commons-net) == 3.13.0
Requires:       eclipse-p2-director >= 4.39
Requires:       mvn(org.tukaani:xz) == 1.12
Requires:       mvn(org.apache.maven.resolver:maven-resolver-named-locks) == 1.9.27
Requires:       maven >= 3.9.9
Requires:       mvn(org.apache.commons:commons-compress:jar:sources) == 1.28.0
Requires:       mvn(biz.aQute.bnd:biz.aQute.bnd.embedded-repo) == 7.2.3
Requires:       mvn(org.apache.maven.indexer:search-backend-smo) == 7.1.6
Requires:       mvn(org.eclipse.jdt:org.eclipse.jdt.launching.macosx) == 3.6.400
Requires:       mvn(org.eclipse.pde:org.eclipse.pde.api.tools) == 1.3.1100
Requires:       mvn(org.apache.maven.plugins:maven-failsafe-plugin) == 3.5.5
Requires:       mvn(org.apache.maven.surefire:surefire-api) == 3.5.5
Requires:       mvn(io.takari.maven:takari-smart-builder) == 1.1.0
Requires:       mvn(org.osgi:org.osgi.service.repository) == 1.1.0

%description
This package provides the Tycho plugins used to build the Eclipse SDK.
Tycho builds Eclipse plugins, features and installable products with Maven.
It resolves OSGi bundles, assembles p2 repositories and runs Eclipse
plug-in tests.

%prep
%autosetup -p1 -n tycho-tycho-%{version}
# Njord stages artifacts for publication to the Sonatype Central Portal.
rm .mvn/extensions.xml
# Maven validates each plugin version against its embedded descriptor.
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -u '/m:project/m:build/m:pluginManagement/m:plugins/m:plugin[m:artifactId="maven-enforcer-plugin"]/m:version' \
    -v '%{enforcer_version}' pom.xml
for plugin in maven-resources-plugin maven-compiler-plugin maven-surefire-plugin maven-jar-plugin maven-source-plugin maven-plugin-plugin plexus-component-metadata sisu-maven-plugin maven-dependency-plugin; do
    jar=%{_datadir}/java/javapackages-bootstrap/$plugin.jar
    version=$(unzip -p "$jar" META-INF/maven/plugin.xml | xmlstarlet sel -t -v '/plugin/version')
    test -n "$version"
    xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
        -u "/m:project/m:build/m:pluginManagement/m:plugins/m:plugin[m:artifactId='$plugin']/m:version" \
        -v "$version" pom.xml
    if test "$plugin" = maven-source-plugin; then
        xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
            -u "/m:project/m:dependencyManagement/m:dependencies/m:dependency[m:artifactId='$plugin']/m:version" \
            -v "$version" pom.xml
    fi
done
# The source archive has no Git checkout. Use the revision recorded in the release.
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -d '/m:project/m:build/m:plugins/m:plugin[m:artifactId="buildnumber-maven-plugin"]' tycho-spi/pom.xml
# Tycho's HTTP test server uses the maintained Jetty 12.1 branch.
jetty='/m:project/m:properties/m:jetty.version'
test "$(xmlstarlet sel -N m=http://maven.apache.org/POM/4.0.0 -t -v "$jetty" tycho-core/pom.xml)" = 12.1.9
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 -u "$jetty" -v '%{jetty_version}' tycho-core/pom.xml
# AntRun copies the generated system-packages companion into the core module.
antrun=%{_datadir}/java/javapackages-bootstrap/maven-antrun-plugin.jar
version=$(unzip -p "$antrun" META-INF/maven/plugin.xml | xmlstarlet sel -t -v '/plugin/version')
test -n "$version"
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -u '/m:project/m:build/m:plugins/m:plugin[m:artifactId="maven-antrun-plugin"]/m:version' -v "$version" tycho-core/pom.xml
# The library detector runs on Java 8 and uses only the Java SE API.
detector=tycho-lib-detector/pom.xml
compiler='/m:project/m:build/m:pluginManagement/m:plugins/m:plugin[m:artifactId="maven-compiler-plugin"]'
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -d "$compiler/m:dependencies" -d "$compiler/m:configuration/*" \
    -s "$compiler/m:configuration" -t elem -n 'release' -v '8' "$detector"
# The metadata model already depends on Equinox, which exports the same OSGi Resource API.
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -d '/m:project/m:dependencies/m:dependency[m:groupId="org.osgi" and m:artifactId="org.osgi.resource"]' tycho-metadata-model/pom.xml
# The current IgnoreJRERequirement preserves the 1.9 annotation's retention and target uses.
managed='/m:project/m:dependencyManagement/m:dependencies'
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -s "$managed" -t elem -n dependency -v '' pom.xml
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -s "$managed/m:dependency[last()]" -t elem -n groupId -v org.codehaus.mojo \
    -s "$managed/m:dependency[last()]" -t elem -n artifactId -v animal-sniffer-annotations \
    -s "$managed/m:dependency[last()]" -t elem -n version -v 1.27 pom.xml
mkdir -p local-repository .xmvn
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn --batch-mode --offline -DbuildNumber=%{revision} -Dmaven.repo.local="$PWD/local-repository" --fail-at-end --projects '%{sdk_projects}' -DskipTests install

%install
python3 %{SOURCE1} local-repository %{buildroot} %{_datadir} %{version}

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
# Check the recorded release revision and the Java 8 detector consumed by Tycho.
unzip -p tycho-spi/target/tycho-spi-%{version}.jar org/eclipse/tycho/version/version.properties | grep -Fx 'buildNumber=%{revision}'
detector=tycho-lib-detector/target/tycho-lib-detector-%{version}.jar
detector_class=org.eclipse.tycho.libdetector.LibraryDetector
javap -verbose -classpath "$detector" "$detector_class" | grep -F 'major version: 52'
case "$(java -Dopenruyi.boot.class.path=/rt.jar -cp "$detector" "$detector_class")" in
    '####'*'|/rt.jar|null|null####') ;;
    *) exit 1 ;;
esac
mvn --batch-mode --offline -DbuildNumber=%{revision} -Dmaven.repo.local="$PWD/local-repository" --projects '%{sdk_projects}' verify
mvn --batch-mode --offline -DbuildNumber=%{revision} -Dmaven.repo.local="$PWD/local-repository" -f tycho-its/pom.xml verify

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/tycho.xml
%{repo_dir}/org/eclipse/tycho/

%changelog
%autochangelog
