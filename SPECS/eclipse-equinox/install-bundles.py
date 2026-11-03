#!/usr/bin/python3
"""Install locally built OSGi bundles alongside their published Maven models."""
import argparse
from email import message_from_bytes
from pathlib import Path
import re
import shutil
from xml.etree import ElementTree as ET
from zipfile import ZipFile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--qualifier", help="OSGi release qualifier appended to the Maven version")
parser.add_argument("--symbolic-name", help="Bundle symbolic name when it differs from a single Maven artifact ID")
parser.add_argument("--sources", type=Path, help="Directory of corresponding OSGi source bundle JARs")
parser.add_argument("buildroot", type=Path)
parser.add_argument("datadir", type=Path)
parser.add_argument("package")
parser.add_argument("jars", type=Path)
parser.add_argument("poms", type=Path, nargs="+")
args = parser.parse_args()
if args.symbolic_name and len(args.poms) != 1:
    parser.error("--symbolic-name requires one Maven model")
artifacts = ET.Element("artifacts")
namespace = {"m": "http://maven.apache.org/POM/4.0.0"}
for pom in args.poms:
    model = ET.parse(pom)
    group = model.findtext("m:groupId", namespaces=namespace) or model.findtext("m:parent/m:groupId", namespaces=namespace)
    name = model.findtext("m:artifactId", namespaces=namespace)
    version = model.findtext("m:version", namespaces=namespace) or model.findtext("m:parent/m:version", namespaces=namespace)
    if not all(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", value or "") for value in (group, name, version)):
        raise ValueError(f"Invalid Maven coordinates in {pom}")
    symbolic_name = args.symbolic_name or name
    bundle_version = f"{version}.{args.qualifier}" if args.qualifier else version
    files = [("pom", None, pom), ("jar", None, args.jars / (name + ".jar"))]
    if args.sources:
        files.append(("jar", "sources", args.sources / (name + ".jar")))
    directory = args.datadir / "maven-repository" / Path(*group.split(".")) / name / version
    for extension, classifier, file in files:
        if extension == "jar":
            with ZipFile(file) as archive:
                manifest = message_from_bytes(archive.read("META-INF/MANIFEST.MF").replace(b"\r\n ", b""))
            expected_name = symbolic_name + (".source" if classifier else "")
            if manifest.get("Bundle-SymbolicName", "").split(";")[0] != expected_name or manifest.get("Bundle-Version") != bundle_version:
                raise ValueError(f"Bundle and Maven coordinates differ for {file}")
            if classifier:
                host = manifest.get("Eclipse-SourceBundle", "")
                if host.split(";")[0] != symbolic_name or f'version="{bundle_version}"' not in host.split(";"):
                    raise ValueError(f"Source bundle lacks its released host for {file}")
        suffix = "-" + classifier if classifier else ""
        path = directory / f"{name}-{version}{suffix}.{extension}"
        staged = args.buildroot / path.relative_to("/")
        staged.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, staged)
        entry = ET.SubElement(artifacts, "artifact")
        for key, value in (("groupId", group), ("artifactId", name), ("extension", extension),
                           ("version", version), ("path", str(path))):
            ET.SubElement(entry, key).text = value
        if classifier:
            ET.SubElement(entry, "classifier").text = classifier
        versions = ET.SubElement(entry, "compatVersions")
        for alias in (version, "SYSTEM"):
            ET.SubElement(versions, "version").text = alias
        if extension == "pom":
            props = ET.SubElement(entry, "properties")
            ET.SubElement(props, "xmvn.resolver.disableEffectivePom").text = "true"

metadata = ET.Element("metadata")
metadata.append(artifacts)
path = args.buildroot / args.datadir.relative_to("/") / "maven-metadata" / (args.package + ".xml")
path.parent.mkdir(parents=True, exist_ok=True)
ET.indent(metadata)
ET.ElementTree(metadata).write(path, encoding="utf-8", xml_declaration=True)
