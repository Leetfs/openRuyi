import shutil
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

buildroot, datadir, *poms = map(Path, sys.argv[1:])
metadata = ET.Element("metadata")
artifacts = ET.SubElement(metadata, "artifacts")
ns = {"m": "http://maven.apache.org/POM/4.0.0"}
for pom in poms:
    model = ET.parse(pom).getroot()
    group, name, version = (model.findtext(f"m:{key}", namespaces=ns)
                            for key in ("groupId", "artifactId", "version"))
    directory = datadir / "maven-repository" / group.replace(".", "/") / name / version
    for extension, source in (("jar", Path(f"{name}-{version}.jar")), ("pom", pom)):
        path = directory / f"{name}-{version}.{extension}"
        target = buildroot / path.relative_to("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        artifact = ET.SubElement(artifacts, "artifact")
        for key, value in (("groupId", group), ("artifactId", name), ("version", version),
                           ("extension", extension), ("path", str(path))):
            ET.SubElement(artifact, key).text = value
        versions = ET.SubElement(artifact, "compatVersions")
        for v in (version, "SYSTEM"):
            ET.SubElement(versions, "version").text = v
        if extension == "pom":
            dependencies = ET.SubElement(artifact, "dependencies")
            for dependency in model.findall("m:dependencies/m:dependency", ns):
                if dependency.findtext("m:scope", "compile", ns) not in ("compile", "runtime"):
                    continue
                entry = ET.SubElement(dependencies, "dependency")
                for dest, src in (("groupId", "groupId"), ("artifactId", "artifactId"), ("requestedVersion", "version")):
                    ET.SubElement(entry, dest).text = dependency.findtext(f"m:{src}", namespaces=ns)

out = buildroot / datadir.relative_to("/") / "maven-metadata/mockito.xml"
out.parent.mkdir(parents=True, exist_ok=True)
ET.indent(metadata)
ET.ElementTree(metadata).write(out, encoding="UTF-8", xml_declaration=True)
