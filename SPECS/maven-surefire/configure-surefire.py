# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Bind the offline Maven reactor to the distribution plugins and test engines."""
from pathlib import Path
from xml.etree import ElementTree as ET

namespace = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", namespace)


def tag(name):
    return f"{{{namespace}}}{name}"


def child(node, name):
    element = node.find(tag(name))
    return ET.SubElement(node, tag(name)) if element is None else element


def plugin(plugins, name, group="org.apache.maven.plugins"):
    for item in plugins.findall(tag("plugin")):
        if item.findtext(tag("artifactId")) == name and item.findtext(tag("groupId"), "org.apache.maven.plugins") == group:
            return item
    item = ET.SubElement(plugins, tag("plugin"))
    child(item, "groupId").text = group
    child(item, "artifactId").text = name
    return item


def execution(plugin_node, name):
    executions = child(plugin_node, "executions")
    for item in executions.findall(tag("execution")):
        if item.findtext(tag("id")) == name:
            return item
    item = ET.SubElement(executions, tag("execution"))
    child(item, "id").text = name
    return item


model = ET.parse("pom.xml")
build = child(model.getroot(), "build")
managed = child(child(build, "pluginManagement"), "plugins")
versions = {
    "maven-antrun-plugin": "3.1.0.MBI",
    "maven-assembly-plugin": "3.7.1.MBI",
    "maven-compiler-plugin": "3.12.1.MBI",
    "maven-dependency-plugin": "3.6.1.MBI",
    "maven-jar-plugin": "3.3.0.MBI",
    "maven-plugin-plugin": "3.9.0.MBI",
    "maven-remote-resources-plugin": "3.1.0.MBI",
    "maven-resources-plugin": "3.5.0",
    "maven-surefire-plugin": "3.2.2.MBI",
}
for artifact, version in versions.items():
    child(plugin(managed, artifact), "version").text = version
child(plugin(managed, "sisu-maven-plugin", "org.eclipse.sisu"), "version").text = "1.0.0.MBI"

# These executions check the release source formatting and license headers.
plugins = child(build, "plugins")
child(execution(plugin(plugins, "maven-checkstyle-plugin"), "checkstyle-check"), "phase").text = "none"
child(execution(plugin(plugins, "apache-rat-plugin", "org.apache.rat"), "rat-check"), "phase").text = "none"

dependencies = child(model.getroot(), "dependencies")
for group, name, version in [
    ("org.junit.platform", "junit-platform-launcher", "1.12.2"),
    ("org.junit.vintage", "junit-vintage-engine", "5.12.2"),
    ("org.junit.jupiter", "junit-jupiter-engine", "5.12.2"),
]:
    dep = ET.SubElement(dependencies, tag("dependency"))
    for key, value in [("groupId", group), ("artifactId", name), ("version", version), ("scope", "test")]:
        child(dep, key).text = value
model.write("pom.xml", encoding="utf-8", xml_declaration=True)

# Only the three host modules load the distribution's Java 17 Maven XML API.
for name in ("maven-surefire-common", "maven-surefire-plugin", "maven-failsafe-plugin"):
    path = Path(name) / "pom.xml"
    model = ET.parse(path)
    plugins = child(child(model.getroot(), "build"), "plugins")
    target = execution(plugin(plugins, "maven-enforcer-plugin"), "enforce-bytecode-version")
    rules = child(child(target, "configuration"), "rules")
    child(child(rules, "enforceBytecodeVersion"), "maxJdkVersion").text = "17"
    model.write(path, encoding="utf-8", xml_declaration=True)
