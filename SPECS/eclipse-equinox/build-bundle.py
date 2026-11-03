#!/usr/bin/python3
"""Build a binary Eclipse bundle from its PDE source and resource lists."""
import argparse
from email import message_from_string
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("bundle", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--release", required=True)
parser.add_argument("--classpath", required=True)
parser.add_argument("--nested-classpath", help="Build the nested JARs in the PDE source lists with this extra class path")
args = parser.parse_args()

props = re.sub(r"\\\r?\n[ \t]*", "", (args.bundle / "build.properties").read_text())
properties = {}
for line in props.splitlines():
    key, sep, value = line.partition("=")
    if sep and not key.lstrip().startswith(("#", "!")):
        properties[key.strip()] = [part.strip() for part in value.split(",") if part.strip()]

original = (args.bundle / "META-INF/MANIFEST.MF").read_text()
version_header = re.compile(r"(?m)^Bundle-Version: ([0-9]+[.][0-9]+[.][0-9]+(?:[.][A-Za-z0-9_-]+)?)$")
manifest, count = version_header.subn(lambda match: "Bundle-Version: " + match[1].removesuffix(".qualifier"), original)
if count != 1:
    raise ValueError(f"Invalid Bundle-Version for {args.bundle.name}")

args.output.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(dir=args.output.parent) as temporary:
    work = Path(temporary)
    classes = work / "classes"
    classes.mkdir()

    def copy_resource(file, base, destination):
        if file.suffix in (".java", ".class") or file.name in ("package.html", ".gitignore"):
            return
        target = destination / file.relative_to(base)
        if target.relative_to(destination).as_posix() == "META-INF/MANIFEST.MF":
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, target)

    def compile_sources(directories, destination, classpath):
        java = []
        for directory in directories:
            source = args.bundle / directory
            if not source.is_dir():
                raise ValueError(f"Missing source directory {source}")
            for file in sorted(source.rglob("*")):
                if file.suffix == ".java":
                    java.append(file)
                elif file.is_file():
                    copy_resource(file, source, destination)
        sources = work / "java-sources"
        sources.write_text("".join(f'"{file.resolve()}"\n' for file in java))
        subprocess.run(["javac", "--release", args.release, "-encoding", "UTF-8", "-proc:none",
                        "-classpath", classpath, "-d", str(destination), "@" + str(sources)], check=True)

    date_option = []
    if "SOURCE_DATE_EPOCH" in os.environ:
        timestamp = datetime.fromtimestamp(int(os.environ["SOURCE_DATE_EPOCH"]), timezone.utc)
        date_option = ["--date", timestamp.isoformat(timespec="seconds")]
    if "source.." in properties:
        compile_sources(properties["source.."], classes, args.classpath)
    elif args.nested_classpath is None or not any(key.startswith("source.") and key.endswith(".jar") for key in properties):
        raise ValueError(f"No bundle sources declared by {args.bundle.name}")

    for pattern in properties["bin.includes"]:
        if pattern == ".":
            continue
        for path in sorted(args.bundle.glob(pattern.rstrip("/"))):
            if path.is_dir():
                for file in sorted(path.rglob("*")):
                    if file.is_file():
                        copy_resource(file, args.bundle, classes)
            else:
                copy_resource(path, args.bundle, classes)

    if args.nested_classpath is not None:
        nested = {key.removeprefix("source."): values for key, values in properties.items()
                  if key.startswith("source.") and key.endswith(".jar")}
        order = dict.fromkeys(properties.get("jars.compile.order", []) + list(nested))
        nested_cp = [str(classes), args.classpath, args.nested_classpath]
        for name in order:
            if name not in nested:
                continue
            relative = Path(name)
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError(f"Invalid nested JAR path {name}")
            output = classes / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(dir=work) as compiled:
                compile_sources(nested[name], Path(compiled), os.pathsep.join(nested_cp))
                subprocess.run(["jar", "--create", "--file", str(output), *date_option, "-C", compiled, "."], check=True)
            nested_cp.append(str(output))

    components = message_from_string(manifest.replace("\n ", "")).get("Service-Component", "")
    required = [name.strip() for name in components.split(",") if name.strip()]
    if any(not list(classes.glob(name)) for name in required):
        system = Path("/usr/share/java/javapackages-bootstrap")
        bnd = os.pathsep.join(str(system / (name + ".jar")) for name in
                              ("biz.aQute.bndlib", "aQute.libg", "slf4j-api", "osgi.core", "osgi.cmpn"))
        generator = Path(__file__).resolve().with_name("GenerateComponents.java")
        subprocess.run(["java", "-cp", bnd, str(generator), str(classes), args.classpath], check=True)
        for name in required:
            if not list(classes.glob(name)):
                raise ValueError(f"Missing service component {name} for {args.bundle.name}")

    mf = work / "MANIFEST.MF"
    mf.write_text(manifest)
    command = ["jar", "--create", "--file", str(args.output), "--manifest", str(mf)]
    subprocess.run(command + date_option + ["-C", str(classes), "."], check=True)
