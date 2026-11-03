"""Install the Tycho reactor artifacts and register their Maven coordinates."""
from pathlib import Path
import shutil
import sys
from xml.etree import ElementTree as ET

source, buildroot, datadir = map(Path, sys.argv[1:4])
version = sys.argv[4]
repository = datadir / "maven-repository"
metadata = ET.Element("metadata")
artifacts = ET.SubElement(metadata, "artifacts")
found_extension = False
for pom in sorted((source / "org/eclipse/tycho").rglob(f"{version}/*.pom")):
    directory = pom.parent
    relative = directory.relative_to(source)
    group = ".".join(relative.parts[:-2])
    name = relative.parts[-2]
    stem = f"{name}-{version}"
    if pom.name != stem + ".pom":
        continue
    for file in sorted(directory.glob(stem + "*")):
        if not file.is_file() or file.suffix in (".sha1", ".md5", ".sha256", ".sha512", ".asc", ".lastUpdated"):
            continue
        extension = next((ext for ext in ("tar.gz", "tar.xz", "tar.bz2") if file.name.endswith("." + ext)),
                         file.suffix.removeprefix("."))
        suffix = file.name[len(stem):].removesuffix("." + extension)
        if not extension or (suffix and not suffix.startswith("-")):
            continue
        destination = repository / relative / file.name
        staged = buildroot / destination.relative_to("/")
        staged.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, staged)
        node = ET.SubElement(artifacts, "artifact")
        for key, val in (("groupId", group), ("artifactId", name), ("extension", extension),
                         ("version", version), ("path", str(destination))):
            ET.SubElement(node, key).text = val
        if suffix:
            ET.SubElement(node, "classifier").text = suffix[1:]
        ET.SubElement(ET.SubElement(node, "compatVersions"), "version").text = version
        if extension == "pom":
            ET.SubElement(ET.SubElement(node, "properties"), "xmvn.resolver.disableEffectivePom").text = "true"
        if (group, name, extension, suffix) == ("org.eclipse.tycho", "tycho-build", "jar", ""):
            found_extension = True

if not found_extension:
    raise SystemExit("The reactor did not install the Tycho Maven extension")
output = buildroot / datadir.relative_to("/") / "maven-metadata/tycho.xml"
output.parent.mkdir(parents=True, exist_ok=True)
ET.indent(metadata)
ET.ElementTree(metadata).write(output, encoding="utf-8", xml_declaration=True)
