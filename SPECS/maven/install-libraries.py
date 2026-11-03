"""Install Maven's modules and link external jars to the RPMs that supplied them."""
import hashlib
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

root, datadir, version = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
repository = datadir / "maven-repository"
maven_home = datadir / "maven"
maven_modules = repository / "org/apache/maven"
distribution = Path("distribution")

def staged(path):
    return root / path.relative_to("/")

def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").digest()

modules = {}
for pom in [Path("pom.xml"), *sorted(Path(".").glob("maven-*/pom.xml"))]:
    name = "maven" if pom.parent == Path(".") else pom.parent.name
    directory = maven_modules / name / version
    staged(directory).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(pom, staged(directory) / f"{name}-{version}.pom")
    modules[f"{name}-{version}.jar"] = directory

system_jars = defaultdict(list)
for prefix in (repository, datadir / "java"):
    for jar in sorted(prefix.rglob("*.jar")):
        if jar.is_file():
            system_jars[jar.stat().st_size].append(jar.resolve())

owners = set()
for location in ("boot", "lib"):
    jars = sorted((distribution / location).glob("*.jar"))
    if not jars:
        raise SystemExit(f"No Maven {location} jars built")
    directory = maven_home / location
    staged(directory).mkdir(parents=True, exist_ok=True)
    for jar in jars:
        if jar.name in modules:
            target = modules[jar.name] / jar.name
            shutil.copyfile(jar, staged(target))
        else:
            checksum = digest(jar)
            target = next((p for p in system_jars[jar.stat().st_size] if digest(p) == checksum), None)
            if target is None:
                raise SystemExit(f"No installed RPM supplied the built distribution's {jar.name}")
            owner = subprocess.check_output(
                ["rpm", "-qf", "--queryformat", "%{NAME}", target], text=True
            )
            owners.add(owner)
        (staged(directory) / jar.name).symlink_to(os.path.relpath(target, directory))
Path("runtime-requires").write_text("".join(f"{owner}\n" for owner in sorted(owners)))

# Expose the installed Maven modules, including the root model used as a BOM.
metadata = ET.Element("metadata")
artifacts = ET.SubElement(metadata, "artifacts")
for file in sorted(staged(maven_modules).glob(f"*/{version}/*")):
    extension = file.suffix.removeprefix(".")
    if extension not in ("jar", "pom"):
        continue
    artifact = ET.SubElement(artifacts, "artifact")
    for key, value in (
        ("groupId", "org.apache.maven"), ("artifactId", file.parent.parent.name),
        ("extension", extension), ("version", version), ("path", "/" + str(file.relative_to(root)))
    ):
        ET.SubElement(artifact, key).text = value
    ET.SubElement(ET.SubElement(artifact, "compatVersions"), "version").text = version
    if extension == "pom":
        properties = ET.SubElement(artifact, "properties")
        ET.SubElement(properties, "xmvn.resolver.disableEffectivePom").text = "true"
output = staged(datadir / "maven-metadata/maven.xml")
output.parent.mkdir(parents=True, exist_ok=True)
ET.indent(metadata)
ET.ElementTree(metadata).write(output, encoding="utf-8", xml_declaration=True)
