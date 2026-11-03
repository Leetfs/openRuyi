# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Resolve the upstream core extension and index installed ECJ releases for offline Maven."""
import os
from pathlib import Path
import subprocess
from xml.etree import ElementTree as ET

root = Path.cwd()
repo = root / "maven-repository"
work = root / ".mvn/openruyi-extension"
work.mkdir(parents=True, exist_ok=True)
extensions = root / ".mvn/extensions.xml"
model = ET.Element("project")
ET.SubElement(model, "modelVersion").text = "4.0.0"
ET.SubElement(model, "groupId").text = "org.openruyi.eclipse"
ET.SubElement(model, "artifactId").text = "sdk-build-extensions"
ET.SubElement(model, "version").text = "1"
dependencies = ET.SubElement(model, "dependencies")
for extension in ET.parse(extensions).findall("extension"):
    dependency = ET.SubElement(dependencies, "dependency")
    for field in ("groupId", "artifactId", "version"):
        value = extension.findtext(field)
        if not value:
            raise ValueError(f"Missing {field} in {extensions}")
        ET.SubElement(dependency, field).text = value
if not len(dependencies):
    raise ValueError(f"No extensions in {extensions}")
ET.ElementTree(model).write(work / "pom.xml")
# The CLI resolves .mvn/extensions.xml before the XMvn extension can map RPM artifacts.
extensions.rename(work / "extensions.xml")
try:
    ext = Path("/usr/share/javapackages-bootstrap/maven/lib/ext")
    bootstrap = os.pathsep.join(str(ext / name) for name in ("xmvn.jar", "kojan-xml.jar"))
    env = os.environ.copy()
    env["MAVEN_OPTS"] = env.get("MAVEN_OPTS", "") + " -Dmaven.ext.class.path=" + bootstrap
    config = work / ".xmvn"
    config.mkdir(exist_ok=True)
    (config / "configuration.xml").write_bytes((root / ".xmvn/configuration.xml").read_bytes())
    output = work / "classpath"
    subprocess.run(["mvn", "-B", "-o", f"-Dmaven.repo.local={repo}",
                    "org.apache.maven.plugins:maven-dependency-plugin:3.6.1.MBI:build-classpath",
                    "-DincludeScope=runtime", f"-Dmdep.outputFile={output}"],
                   cwd=work, env=env, check=True)
    # Maven supplies Xpp3Dom in the core realm. The bootstrap Plexus jars contain a second copy.
    conflict_dir = Path("/usr/share/java/javapackages-bootstrap")
    conflicts = {conflict_dir / name for name in ("plexus-xml.jar", "plexus-utils.jar")}
    paths = [Path(p) for p in output.read_text().strip().split(os.pathsep)]
    if not all(p.is_file() for p in paths):
        raise ValueError("The Maven extension classpath contains a missing artifact")
    classpath = [bootstrap, *(str(p) for p in paths if p.resolve() not in conflicts)]
    (work / "sdk-classpath").write_text(os.pathsep.join(classpath) + "\n")

    # Tycho selects its Java compiler by a Maven version range. Installed RPMs provide both files.
    artifact = repo / "org/eclipse/jdt/ecj"
    versions = sorted((p.name for p in artifact.iterdir()
                       if (p / f"ecj-{p.name}.pom").is_file() and (p / f"ecj-{p.name}.jar").is_file()),
                      key=lambda v: tuple(map(int, v.split("."))))
    if not versions:
        raise ValueError("No installed ECJ model and JAR")
    metadata = ET.Element("metadata")
    ET.SubElement(metadata, "groupId").text = "org.eclipse.jdt"
    ET.SubElement(metadata, "artifactId").text = "ecj"
    versioning = ET.SubElement(metadata, "versioning")
    ET.SubElement(versioning, "release").text = versions[-1]
    items = ET.SubElement(versioning, "versions")
    for version in versions:
        ET.SubElement(items, "version").text = version
    ET.ElementTree(metadata).write(artifact / "maven-metadata-local.xml")
except BaseException:
    (work / "extensions.xml").rename(extensions)
    raise
