"""Compile the original HtmlUnit test libraries, including its shaded Jetty client."""
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

sources = Path(sys.argv[1]).resolve()
root = Path.cwd()
work = root / "target/htmlunit-fixtures"
work.mkdir(parents=True, exist_ok=True)
classpath = (root / "target/test-classpath").read_text().strip().split(":")
runtime = []

def unpack(name, version, relocate=False):
    directory = work / (name + "-" + version)
    source = directory / "sources"
    classes = directory / "classes"
    source.mkdir(parents=True, exist_ok=True)
    classes.mkdir(exist_ok=True)
    archive_path = sources / f"{name}-{version}-sources.jar"
    with zipfile.ZipFile(archive_path) as archive:
        for entry in archive.infolist():
            if entry.is_dir() or entry.filename.startswith("META-INF/"):
                continue
            if Path(entry.filename).is_absolute() or ".." in Path(entry.filename).parts:
                raise SystemExit(f"Invalid source archive entry: {entry.filename}")
            filename = entry.filename
            content = archive.read(entry)
            if relocate:
                filename = filename.replace("org/eclipse/jetty", "org/htmlunit/jetty")
                content = content.replace(b"org.eclipse.jetty", b"org.htmlunit.jetty")
                content = content.replace(b"org/eclipse/jetty", b"org/htmlunit/jetty")
            destination = source / filename
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
    return directory, source, classes

def compile_library(name, version, relocate=False, selected=None, extra=()):
    directory, source, classes = unpack(name, version, relocate)
    java_sources = sorted(source.rglob("*.java"))
    if selected:
        java_sources = [source / item for item in selected]
    java_sources = [p for p in java_sources if p.name != "module-info.java"]
    source_list = directory / "sources.list"
    source_list.write_text("".join(str(p) + "\n" for p in java_sources))
    print(f"Compiling test fixture {name} {version}, {len(java_sources)} source files", flush=True)
    subprocess.run(["javac", "-proc:none", "-encoding", "UTF-8", "-g",
                    "-sourcepath", str(source), "-cp", ":".join(classpath),
                    "-d", str(classes), *extra, "@" + str(source_list)], check=True)
    for resource in source.rglob("*"):
        if resource.is_file() and resource.suffix != ".java":
            destination = classes / resource.relative_to(source)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(resource, destination)
    classpath.insert(0, str(classes))
    runtime.append(str(classes))
    return classes

for name, version in (
    ("htmlunit-core-js", "4.4.0"),
    ("neko-htmlunit", "4.4.0"),
    ("htmlunit-cssparser", "4.4.0"),
    ("htmlunit-xpath", "4.4.0"),
    ("htmlunit-csp", "4.4.0"),
    ("dec", "0.1.2"),
    ("httpmime", "4.5.14"),
):
    compile_library(name, version)

# HtmlUnit 4.4.0's websocket-client shades Jetty 9.4.55 with this namespace.
# Build the actual upstream source modules using that relocation rule.
for name in ("jetty-util", "jetty-io", "jetty-http", "jetty-xml", "jetty-client",
             "websocket-api", "websocket-common", "websocket-client"):
    compile_library(name, "9.4.55.v20240627", relocate=True)

# The optional external Xerces adapter needs these DOM implementation classes at
# compile time. The browser tests run with the JDK XML implementation.
xerces = compile_library("xercesImpl", "2.12.2", selected=(
    "org/apache/xerces/dom/DeferredDocumentImpl.java",
    "org/apache/xerces/dom/DeferredNode.java",
))
compile_library("htmlunit", "4.4.0",
                extra=("--add-exports", "java.xml/com.sun.org.apache.xerces.internal.dom=ALL-UNNAMED"))
runtime.remove(str(xerces))
(root / "target/htmlunit-classpath").write_text(":".join(runtime) + "\n")
