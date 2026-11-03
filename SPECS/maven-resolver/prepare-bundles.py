"""Pass the source POM's Bnd configuration to the Felix manifest goal."""
import sys
from pathlib import Path
from xml.etree import ElementTree

ns = {"m": "http://maven.apache.org/POM/4.0.0"}
parent = ElementTree.parse("pom.xml")
version = parent.findtext("m:version", namespaces=ns)
path = "m:build/m:pluginManagement/m:plugins/m:plugin[m:artifactId='bnd-maven-plugin']/m:configuration/m:bnd"
template = parent.findtext(path, namespaces=ns)
if not template or not version:
    raise SystemExit("Missing Resolver version or Bnd instructions in the parent POM")

for module in sys.argv[1].split(","):
    directory = Path(module)
    pom = ElementTree.parse(directory / "pom.xml")
    additions = pom.findtext("m:properties/m:bnd.instructions.additions", "", ns)
    settings = template.replace("${bnd.instructions.additions}", additions)
    settings = settings.replace("${project.artifactId}", module).replace("${project.version}", version)
    # Felix analyzes an existing classes directory rather than building the bundle.
    settings = settings.replace("-exportcontents:", "Export-Package:")
    settings = settings.replace(";-noimport:=true", f';version="{version}";-noimport:=true')
    # Bootstrap JARs omit the upstream package versions used by Bnd to compute imports.
    external = ('com.google.inject*;resolution:=optional;version="[1.4,2)",'
                'org.eclipse.sisu*;resolution:=optional;version="[1.0,2)",')
    slf4j = pom.find("m:dependencies/m:dependency[m:groupId='org.slf4j'][m:artifactId='slf4j-api']", ns)
    if slf4j is not None and slf4j.findtext("m:scope", "compile", ns) in ("compile", "provided"):
        external += 'org.slf4j;version="[1.7,2)",'
    settings = settings.replace("Import-Package:", "Import-Package: " + external)
    (directory / "bootstrap.bnd").write_text(settings)
