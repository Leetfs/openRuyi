#!/usr/bin/python3
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Run SAT4J's upstream test selection with the distribution's JUnit 4 provider."""
import sys
from copy import deepcopy
from pathlib import Path
from xml.etree import ElementTree as ET

namespace = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", namespace)

def tag(name):
    return f"{{{namespace}}}{name}"

def add(parent, **fields):
    for key, value in fields.items():
        ET.SubElement(parent, tag(key)).text = value

source = ET.parse("pom.xml")
plugins = source.findall("./{*}build/{*}plugins/{*}plugin")
settings = next(plugin.find("{*}configuration") for plugin in plugins
                if plugin.findtext("{*}artifactId") == "maven-surefire-plugin")
for module in ("core", "pb"):
    project = ET.Element(tag("project"))
    add(project, modelVersion="4.0.0", groupId="org.openruyi.check", artifactId=f"sat4j-{module}-tests", version="1")
    dependencies = ET.SubElement(project, tag("dependencies"))
    add(ET.SubElement(dependencies, tag("dependency")), groupId="junit", artifactId="junit", version="4.13.2", scope="test")
    add(ET.SubElement(dependencies, tag("dependency")), groupId="org.mockito", artifactId="mockito-core", version="4.11.0", scope="test")
    if module == "pb":
        add(ET.SubElement(dependencies, tag("dependency")), groupId="org.ow2.sat4j", artifactId="org.ow2.sat4j.core",
            version="2.3.6", scope="system", systemPath=str(Path("org.sat4j.core/target/core.jar").resolve()))
    build = ET.SubElement(project, tag("build"))
    plugin = ET.SubElement(ET.SubElement(build, tag("plugins")), tag("plugin"))
    add(plugin, groupId="org.apache.maven.plugins", artifactId="maven-surefire-plugin", version=sys.argv[1])
    provider = ET.SubElement(ET.SubElement(plugin, tag("dependencies")), tag("dependency"))
    add(provider, groupId="org.apache.maven.surefire", artifactId="surefire-junit4", version=sys.argv[1])
    plugin.append(deepcopy(settings))
    ET.ElementTree(project).write(Path("org.sat4j." + module) / "tests.pom", encoding="utf-8", xml_declaration=True)
