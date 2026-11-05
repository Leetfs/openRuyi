# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Install the Surefire modules and register their exact Maven coordinates."""
from pathlib import Path
from shutil import copyfile
from sys import argv
from xml.etree import ElementTree as ET
from zipfile import ZipFile

source, buildroot, datadir = map(Path, argv[1:4])
version = argv[4]
metadata = ET.Element("metadata")
artifacts = ET.SubElement(metadata, "artifacts")
modules = [
    "surefire-shared-utils", "surefire-logger-api", "surefire-api", "surefire-booter",
    "surefire-extensions-api", "surefire-extensions-spi", "surefire-providers",
    "surefire-providers/common-java5", "surefire-providers/surefire-junit-platform",
    "maven-surefire-common", "maven-surefire-plugin", "maven-failsafe-plugin",
]

with ZipFile(source) as archive:
    for module in map(Path, modules):
        name = module.name
        group = "org.apache.maven.plugins" if name in ("maven-failsafe-plugin", "maven-surefire-plugin") else "org.apache.maven.surefire"
        directory = datadir / "maven-repository" / group.replace(".", "/") / name / version
        target = buildroot / directory.relative_to("/")
        target.mkdir(parents=True, exist_ok=True)
        stem = f"{name}-{version}"
        pom = target / f"{stem}.pom"
        if name == "surefire-shared-utils":
            # Shade removes dependencies incorporated into this JAR from its consumer model.
            reduced = ET.parse(module / "dependency-reduced-pom.xml")
            namespace = "http://maven.apache.org/POM/4.0.0"
            ET.register_namespace("", namespace)
            deps = reduced.getroot().find(f"{{{namespace}}}dependencies")
            if deps is not None:
                for dep in list(deps):
                    if dep.findtext(f"{{{namespace}}}scope") == "test" and dep.findtext(f"{{{namespace}}}artifactId") in (
                        "junit-platform-launcher", "junit-vintage-engine", "junit-jupiter-engine"
                    ):
                        deps.remove(dep)
                if not len(deps):
                    reduced.getroot().remove(deps)
            reduced.write(pom, encoding="utf-8", xml_declaration=True)
        else:
            pom.write_bytes(archive.read(f"surefire-{version}/{module}/pom.xml"))
        extensions = ["pom"]
        if name != "surefire-providers":
            copyfile(module / "target" / f"{stem}.jar", target / f"{stem}.jar")
            extensions.append("jar")
        for extension in extensions:
            item = ET.SubElement(artifacts, "artifact")
            for key, value in [("groupId", group), ("artifactId", name), ("version", version),
                               ("extension", extension), ("path", str(directory / f"{stem}.{extension}"))]:
                ET.SubElement(item, key).text = value
            ET.SubElement(ET.SubElement(item, "compatVersions"), "version").text = version
            if extension == "pom":
                props = ET.SubElement(item, "properties")
                ET.SubElement(props, "xmvn.resolver.disableEffectivePom").text = "true"
# The older reactor parent is supplied by surefire-grouper.
if version == "3.5.6":
    directory = datadir / "maven-repository/org/apache/maven/surefire/surefire" / version
    dest = buildroot / directory.relative_to("/") / f"surefire-{version}.pom"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(source) as archive:
        dest.write_bytes(archive.read(f"surefire-{version}/pom.xml"))
    item = ET.SubElement(artifacts, "artifact")
    for key, value in [("groupId", "org.apache.maven.surefire"), ("artifactId", "surefire"),
                       ("version", version), ("extension", "pom"), ("path", str(directory / dest.name))]:
        ET.SubElement(item, key).text = value
    ET.SubElement(ET.SubElement(item, "compatVersions"), "version").text = version
    ET.SubElement(ET.SubElement(item, "properties"), "xmvn.resolver.disableEffectivePom").text = "true"
out = buildroot / datadir.relative_to("/") / "maven-metadata"
out.mkdir(parents=True, exist_ok=True)
ET.indent(metadata)
filename = "maven-surefire-3.5.6.xml" if version == "3.5.6" else "maven-surefire.xml"
ET.ElementTree(metadata).write(out / filename, encoding="utf-8", xml_declaration=True)
