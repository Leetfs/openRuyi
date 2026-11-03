#!/usr/bin/python3
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Install PowerMock's released Maven models and corresponding source-built modules."""
from pathlib import Path
import shutil
import sys
import xml.etree.ElementTree as ET

root, share, built = map(Path, sys.argv[1:])
artifacts = ET.Element("artifacts")
for pom in sorted(built.glob("*.pom")):
    model = ET.parse(pom)
    group, name, version = [model.findtext("{*}" + key) for key in ("groupId", "artifactId", "version")]
    if group != "org.powermock" or name != pom.stem or not version:
        raise ValueError(f"Unexpected module coordinates in {pom}")
    directory = share / "maven-repository/org/powermock" / name / version
    for ext in ("jar", "pom"):
        src = built / (name + "." + ext)
        path = directory / f"{name}-{version}.{ext}"
        dest = root / path.relative_to("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        artifact = ET.SubElement(artifacts, "artifact")
        for key, value in (("groupId", group), ("artifactId", name), ("extension", ext), ("version", version), ("path", str(path))):
            ET.SubElement(artifact, key).text = value
        if ext == "pom":
            props = ET.SubElement(artifact, "properties")
            ET.SubElement(props, "xmvn.resolver.disableEffectivePom").text = "true"
        versions = ET.SubElement(artifact, "compatVersions")
        for value in (version, "SYSTEM"):
            ET.SubElement(versions, "version").text = value
metadata = ET.Element("metadata")
metadata.append(artifacts)
index = root / share.relative_to("/") / "maven-metadata/powermock.xml"
ET.indent(metadata)
ET.ElementTree(metadata).write(index, encoding="utf-8", xml_declaration=True)
