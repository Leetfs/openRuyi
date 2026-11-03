#!/usr/bin/python3
"""Compile the Bnd Maven and repository artifacts from their released source sets."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

root = Path.cwd()
sources = Path(sys.argv[1])
version = sys.argv[2]
work = root / "build/openruyi"
work.mkdir(parents=True, exist_ok=True)
system = Path("/usr/share/java/javapackages-bootstrap")
maven_home = Path("/usr/share/maven")
repo = Path("/usr/share/maven-repository")
staged_repo = work / "repository"
modules = ("biz.aQute.bnd.util", "biz.aQute.bndlib", "biz.aQute.repository",
           "biz.aQute.resolve", "biz.aQute.bnd.maven", "bnd-maven-plugin")


def installed(group, artifact, release):
    file = repo / group.replace(".", "/") / artifact / release / f"{artifact}-{release}.jar"
    if not file.is_file():
        raise FileNotFoundError(file)
    return file


native = [
    installed("org.osgi", "org.osgi.service.log", "1.3.0"),
    installed("org.osgi", "org.osgi.util.function", "1.2.0"),
    installed("org.osgi", "org.osgi.util.promise", "1.3.0"),
    installed("org.eclipse.platform", "org.eclipse.osgi", "3.24.100"),
    installed("org.eclipse.jdt", "org.eclipse.jdt.annotation", "2.4.100"),
    installed("org.apache.maven.shared", "maven-mapping", "3.0.0"),
    system / "slf4j-api-2.0.17.jar",
    *sorted((maven_home / "lib").glob("*.jar")),
    *sorted(system.glob("*.jar")),
]
raw = {}


def classpath(paths):
    return os.pathsep.join(map(str, paths))


def write_resource(directory, name, data):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Invalid archive path {name}")
    target = directory / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def archive(classes, target):
    subprocess.run(["jar", "--create", "--file", str(target), "-C", str(classes), "."], check=True)


resolver_source = next(sources.glob("org.apache.felix.resolver-2.0.4-source-release.zip"))
with ZipFile(resolver_source) as resolver:
    for name in ("NOTICE", "LICENSE"):
        (work / ("felix-resolver-" + name)).write_bytes(resolver.read("org.apache.felix.resolver-2.0.4/" + name))

for name in modules:
    module = work / name
    java_dir = module / "src"
    classes = module / "classes"
    classes.mkdir(parents=True)
    with ZipFile(sources / f"{name}-{version}-sources.jar") as jar:
        for member in jar.namelist():
            if member.endswith("/") or member.startswith("META-INF/"):
                continue
            if member.endswith((".class", ".jar")):
                raise ValueError(f"Unexpected binary in source archive: {member}")
            write_resource(java_dir if member.endswith(".java") else classes, member, jar.read(member))

    paths = sorted(java_dir.rglob("*.java"))
    argfile = module / "javac-sources"
    argfile.write_text("".join(f'"{path}"\n' for path in paths))
    subprocess.run(["javac", "--release", "17", "-proc:none", "-encoding", "UTF-8",
                    "-cp", classpath([*reversed(raw.values()), *native]), "-d", str(classes),
                    "@" + str(argfile)], check=True)

    if name == "biz.aQute.bndlib":
        src = root / name / "src"
        for file in sorted(src.rglob("*")):
            if file.is_file() and file.suffix != ".java":
                write_resource(classes, str(file.relative_to(src)), file.read_bytes())
        shutil.copytree(root / name / "img", classes / "img", dirs_exist_ok=True)
        shutil.copyfile(root / "LICENSE", classes / "LICENSE")
        for file, target in ((root / name / "readme.md", classes / "readme.md"),
                             (src / "aQute/bnd/osgi/bnd.info", classes / "aQute/bnd/osgi/bnd.info")):
            target.write_text(file.read_text().replace("${Bundle-Version}", version))
    elif name == "biz.aQute.resolve":
        reason = "org/apache/felix/resolver/reason/packageinfo"
        with ZipFile(resolver_source) as resolver:
            write_resource(classes, reason, resolver.read("org.apache.felix.resolver-2.0.4/src/main/resources/" + reason))
    elif name == "biz.aQute.repository":
        # The upstream conditional package includes XZ from the build class path.
        with ZipFile(system / "xz.jar") as xz:
            for item in xz.namelist():
                if item.startswith("org/tukaani/xz/") and item.endswith(".class"):
                    write_resource(classes, item, xz.read(item))
    elif name == "bnd-maven-plugin":
        resources = root / "maven-plugins" / name / "src/main/resources"
        shutil.copytree(resources, classes, dirs_exist_ok=True)

    if name != "bnd-maven-plugin":
        shutil.copytree(java_dir, classes / "OSGI-OPT/src", dirs_exist_ok=True)

    raw[name] = module / "raw.jar"
    archive(classes, raw[name])

# The distribution provides these OSGi API packages in the standard Core and
# Compendium artifacts. Keep the separately versioned Promise and Log APIs.
model_dir = work / "poms"
model_dir.mkdir()
uri = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", uri)
aggregates = {
    "org.osgi.dto": ("osgi.core", "8.0.0"),
    "org.osgi.framework": ("osgi.core", "8.0.0"),
    "org.osgi.resource": ("osgi.core", "8.0.0"),
    "org.osgi.service.resolver": ("osgi.core", "8.0.0"),
    "org.osgi.util.tracker": ("osgi.core", "8.0.0"),
    "org.osgi.service.serviceloader": ("osgi.cmpn", "7.0.0"),
    "org.osgi.service.coordinator": ("osgi.cmpn", "7.0.0"),
    "org.osgi.service.repository": ("osgi.cmpn", "7.0.0"),
}
for name in modules:
    file = f"{name}-{version}.pom"
    model = ET.parse(sources / file)
    deps = model.find("{*}dependencies")
    replacements = {}
    for dep in list(deps):
        artifact = dep.findtext("{*}artifactId")
        if dep.findtext("{*}groupId") != "org.osgi" or artifact not in aggregates:
            continue
        if dep.findtext("{*}scope", "compile") != "compile" or dep.findtext("{*}optional", "false") != "false":
            raise ValueError(f"Unexpected scope for {artifact}")
        replacement, release = aggregates[artifact]
        deps.remove(dep)
        if replacement not in replacements:
            dep.find("{*}artifactId").text = replacement
            dep.find("{*}version").text = release
            replacements[replacement] = dep
    if replacements:
        deps.extend(replacements.values())
        model.write(model_dir / file, encoding="utf-8", xml_declaration=True)
    else:
        shutil.copyfile(sources / file, model_dir / file)

# Analyze the release classes with the Bnd library built in the first pass.
analyzer_cp = classpath([*raw.values(), *native])
ready = []
for name in modules[:-1]:
    module = work / name
    cpfile = module / "manifest-classpath"
    cpfile.write_text("".join(str(f) + "\n" for f in [*reversed(ready), *raw.values(), *native]))
    output = work / f"{name}-{version}.jar"
    subprocess.run(["java", "-cp", analyzer_cp, str(sources / "BndManifest.java"), str(root / name),
                    str(raw[name]), str(output), version, str(cpfile), str(sources / "osgi-imports.properties")], check=True)
    ready.append(output)
    dest = staged_repo / "biz/aQute/bnd" / name / version
    dest.mkdir(parents=True)
    shutil.copyfile(output, dest / output.name)
    pom = f"{name}-{version}.pom"
    shutil.copyfile(model_dir / pom, dest / pom)

# Generate the Plexus lifecycle mapping and Maven goal descriptions from the compiled plugin.
name = modules[-1]
module = work / name
(module / ".mvn").mkdir()
(module / ".xmvn").mkdir()
(module / ".xmvn/configuration.xml").write_text(
    "<configuration><resolverSettings><metadataRepositories>"
    "<repository>/usr/share/maven-metadata</repository>"
    "<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>"
    "</metadataRepositories></resolverSettings></configuration>\n")
model = ET.parse(model_dir / f"{name}-{version}.pom")


def element(parent, key, value=None):
    node = ET.SubElement(parent, "{" + uri + "}" + key)
    node.text = value
    return node


build = element(model.getroot(), "build")
element(build, "directory", str(module / "target"))
element(build, "sourceDirectory", str(module / "src"))
element(build, "outputDirectory", str(module / "classes"))
plugins = element(build, "plugins")
plugin = element(plugins, "plugin")
element(plugin, "groupId", "org.apache.maven.plugins")
element(plugin, "artifactId", "maven-plugin-plugin")
element(plugin, "version", "3.9.0.MBI")
element(element(plugin, "configuration"), "goalPrefix", "bnd")
model.write(module / "pom.xml", encoding="utf-8", xml_declaration=True)
subprocess.run(["mvn", "--offline", "--batch-mode", "-Dmaven.repo.local=" + str(staged_repo),
                "org.codehaus.plexus:plexus-component-metadata:2.2.0.MBI:generate-metadata",
                "org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor"], cwd=module, check=True)
descriptor = ET.parse(module / "classes/META-INF/maven/plugin.xml")
goals = {m.findtext("{*}goal") for m in descriptor.findall("{*}mojos/{*}mojo")}
if goals != {"bnd-process", "bnd-process-tests", "help", "jar", "test-jar"}:
    raise ValueError(f"Incomplete Bnd Maven goal descriptors: {sorted(goals)}")
components = ET.parse(module / "classes/META-INF/plexus/components.xml")
if not any(n.text == "aQute.bnd.maven.plugin.BndPackagingLifecycleParticipant"
           for n in components.iter() if n.tag.endswith("implementation")):
    raise ValueError("Missing Bnd Maven lifecycle participant")
archive(module / "classes", work / f"{name}-{version}.jar")
