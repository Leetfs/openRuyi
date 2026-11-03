#!/usr/bin/python3
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Install released Maven POM artifacts in the distribution repository and XMvn index."""
import argparse
from pathlib import Path
import re
import shutil
from xml.etree import ElementTree as ET

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("buildroot", type=Path)
parser.add_argument("datadir", type=Path)
parser.add_argument("package")
parser.add_argument("poms", type=Path, nargs="+")
args = parser.parse_args()
metadata = ET.Element("metadata")
artifacts = ET.SubElement(metadata, "artifacts")

for pom in args.poms:
    model = ET.parse(pom).getroot()
    group = model.findtext("{*}groupId") or model.findtext("{*}parent/{*}groupId")
    name = model.findtext("{*}artifactId")
    version = model.findtext("{*}version") or model.findtext("{*}parent/{*}version")
    if model.findtext("{*}packaging") != "pom":
        raise ValueError(f"Expected POM packaging in {pom}")
    if not all(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", part or "")
               for part in (group, name, version)):
        raise ValueError(f"Expected release coordinates in {pom}")
    directory = args.datadir / "maven-repository" / Path(*group.split(".")) / name / version
    destination = directory / f"{name}-{version}.pom"
    staged = args.buildroot / destination.relative_to("/")
    staged.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(pom, staged)
    entry = ET.SubElement(artifacts, "artifact")
    for tag, value in (("groupId", group), ("artifactId", name), ("extension", "pom"),
                       ("version", version), ("path", str(destination))):
        ET.SubElement(entry, tag).text = value
    ET.SubElement(ET.SubElement(entry, "compatVersions"), "version").text = version
    properties = ET.SubElement(entry, "properties")
    ET.SubElement(properties, "xmvn.resolver.disableEffectivePom").text = "true"

index = args.buildroot / args.datadir.relative_to("/") / "maven-metadata" / (args.package + ".xml")
index.parent.mkdir(parents=True, exist_ok=True)
ET.indent(metadata)
ET.ElementTree(metadata).write(index, encoding="utf-8", xml_declaration=True)
