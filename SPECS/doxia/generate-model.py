# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

"""Run the upstream generate-sources Modello executions with the installed generator."""
from copy import deepcopy
from pathlib import Path
import subprocess
import sys
from xml.etree import ElementTree as ET

module, repository = (Path(argument).resolve() for argument in sys.argv[1:])
namespace = "http://maven.apache.org/POM/4.0.0"
ns = {"m": namespace}
ET.register_namespace("", namespace)
tag = lambda name: "{" + namespace + "}" + name
original = ET.parse(module / "pom.xml")
plugins = original.findall("m:build/m:plugins/m:plugin", ns)
plugin = deepcopy(next(item for item in plugins
                       if item.findtext("m:artifactId", namespaces=ns) == "modello-maven-plugin"))
version = plugin.find("m:version", ns)
if version is None:
    version = ET.SubElement(plugin, tag("version"))
version.text = "2.4.0.MBI"
configuration = plugin.find("m:configuration", ns)
if configuration is None:
    configuration = ET.SubElement(plugin, tag("configuration"))
ET.SubElement(configuration, tag("javaSource")).text = "8"
executions = plugin.find("m:executions", ns)
for execution in list(executions):
    if execution.findtext("m:phase", namespaces=ns) != "generate-sources":
        executions.remove(execution)
if not list(executions):
    raise SystemExit("No upstream generate-sources model execution")
project = ET.Element(tag("project"))
for key, value in (("modelVersion", "4.0.0"), ("groupId", "org.openruyi.build"),
                   ("artifactId", "native-model-generator"), ("version", "1"),
                   ("packaging", "pom")):
    ET.SubElement(project, tag(key)).text = value
build = ET.SubElement(project, tag("build"))
ET.SubElement(build, tag("plugins")).append(plugin)
configuration_directory = module / ".xmvn"
configuration_directory.mkdir(exist_ok=True)
(configuration_directory / "configuration.xml").write_text(
    "<configuration><resolverSettings><metadataRepositories>"
    "<repository>/usr/share/maven-metadata</repository>"
    "<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>"
    "</metadataRepositories></resolverSettings></configuration>\n"
)
output = module / "generate-model.pom"
ET.indent(project)
ET.ElementTree(project).write(output, encoding="utf-8", xml_declaration=True)
subprocess.run(["/usr/libexec/javapackages-bootstrap/mvn", "-B", "-o", "-f", str(output),
                "-Dmaven.repo.local=" + str(repository), "generate-sources"],
               cwd=module, check=True)
