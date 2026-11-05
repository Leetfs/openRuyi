# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Build and retrofit the five source modules using the upstream Gradle module definitions."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys

version, driver = sys.argv[1:]
root = Path.cwd()
build = root / "build"
bundles = build / "bundles"
bundles.mkdir(parents=True, exist_ok=True)
bootstrap = Path("/usr/share/java/javapackages-bootstrap")
tool = build / "retrofitter"
tool.mkdir(exist_ok=True)
external = [bootstrap / f"{n}.jar" for n in ("asm", "asm-tree", "asm-commons")]
toolcp = os.pathsep.join(map(str, [tool, *external]))
toolsrc = root / "tools/retrofitter/src/main"
subprocess.run(["javac", "--release", "17", "-proc:none", "-cp", toolcp, "-d", tool,
                toolsrc / "java/org/objectweb/asm/tools/Retrofitter.java", driver], check=True)
shutil.copytree(toolsrc / "resources", tool, dirs_exist_ok=True)

gradle = Path("build.gradle").read_text()
upper = re.search(r"ext[.]osgi_version_upper_bound = '([^']+)'", gradle)[1]
modules = ["asm", "asm-tree", "asm-analysis", "asm-commons", "asm-util"]
exports = {}
dependencies = {}
compiled = []

def closure(module):
    return list(dict.fromkeys(n for child in dependencies[module] for n in [*closure(child), child]))

for module in modules:
    declaration = gradle.split(f"project(':{module}') {{", 1)[1].split("\n}", 1)[0]
    exports[module] = re.findall(r"'([^']+)'", re.search(r"provides = \[([^]]+)\]", declaration)[1])
    requires = re.search(r"requires = \[([^]]+)\]", declaration)
    dependencies[module] = re.findall(r"':([^']+)'", requires[1]) if requires else []
    classes = build / module / "classes"
    classes.mkdir(parents=True, exist_ok=True)
    files = sorted(str(s) for s in Path(module, "src/main/java").rglob("*.java"))
    subprocess.run(["javac", "--release", "11", "-g", "-proc:none", "-encoding", "UTF-8",
                    "-cp", os.pathsep.join(map(str, compiled)), "-d", classes, *files], check=True)
    deps = closure(module)
    symbolic = exports[module][0]
    requires = [exports[n][0] for n in deps]
    args = [classes, version, ",".join(exports[module])]
    if requires:
        args.append(",".join(requires))
    subprocess.run(["java", "-cp", toolcp, "RetrofitModule", *args], check=True)
    compiled.append(classes)
    imports = list(dict.fromkeys(name for n in deps for name in exports[n]))
    export = ",".join(f'{n};version="{version}"' for n in exports[module])
    if imports:
        export += ';uses:="' + ",".join(imports) + '"'
    headers = {"Bundle-DocURL": "http://asm.ow2.org",
               "Bundle-License": "BSD-3-Clause;link=https://asm.ow2.io/LICENSE.txt",
               "Bundle-ManifestVersion": "2", "Bundle-Name": symbolic,
               "Bundle-RequiredExecutionEnvironment": "J2SE-1.5", "Bundle-SymbolicName": symbolic,
               "Bundle-Version": version, "Export-Package": export}
    if imports:
        headers["Import-Package"] = ",".join(f'{n};version="[{version},{upper})"' for n in imports)
        headers["Module-Requires"] = ",".join(n + ";transitive=true" for n in requires)
    manifest = classes.parent / "module.mf"
    manifest.write_text("".join(f"{name}: {value}\n" for name, value in headers.items()))
    meta = classes / "META-INF"
    meta.mkdir(exist_ok=True)
    shutil.copyfile("LICENSE.txt", meta / "LICENSE.txt")
    subprocess.run(["jar", "cfm", bundles / (module + ".jar"), manifest, "-C", classes, "."], check=True)
