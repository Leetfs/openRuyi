# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Build Bnd's embedded launchers using the original bundle recipes and native libraries."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
from zipfile import ZipFile

sources = Path(sys.argv[1])
builder = Path(sys.argv[2])
version = sys.argv[3]
root = Path.cwd()
work = root / "build/embedded"
work.mkdir(parents=True, exist_ok=True)
repository = Path("/usr/share/maven-repository")
native = sorted((root / "build/openruyi").glob("*.jar"))
for group in ["org/osgi", "org/junit", "org/eclipse/platform", "org/apache/felix"]:
    native.extend(p for p in (repository / group).rglob("*.jar") if not p.name.endswith(("-sources.jar", "-javadoc.jar")))
native.extend(Path("/usr/share/java/javapackages-bootstrap").glob("*.jar"))
native_cp = os.pathsep.join(map(str, native))
modules = ["biz.aQute.tester", "biz.aQute.tester.junit-platform", "biz.aQute.launcher",
           "biz.aQute.remote.launcher", "biz.aQute.junit"]
subprocess.run(["javac", "--release", "17", "-cp", native_cp, "-d", work, builder], check=True)
bundles = work / "bundles"
bundles.mkdir(exist_ok=True)
compile_cp = native_cp
for module in modules:
    directory = work / module
    java = directory / "src"
    classes = directory / "classes"
    classes.mkdir(parents=True, exist_ok=True)
    with ZipFile(sources / f"{module}-{version}-sources.jar") as archive:
        archive.extractall(java)
    source_list = directory / "java-sources"
    source_list.write_text("".join(str(f) + "\n" for f in sorted(java.rglob("*.java"))))
    subprocess.run(["javac", "--release", "17", "-g", "-proc:none", "-encoding", "UTF-8",
                    "-cp", compile_cp, "-d", classes, "@" + str(source_list)], check=True)
    compile_cp = str(classes) + os.pathsep + compile_cp
    classpath = directory / "classpath"
    classpath.write_text(str(classes) + os.pathsep + native_cp)
    project = root / ("biz.aQute.remote" if module == "biz.aQute.remote.launcher" else module)
    recipe = project / ("launcher.bnd" if module == "biz.aQute.remote.launcher" else "bnd.bnd")
    command = ["java", "-cp", str(work) + os.pathsep + native_cp, "BuildNativeBundle"]
    if module == "biz.aQute.launcher":
        pre = bundles / "biz.aQute.launcher.pre.jar"
        subprocess.run([*command, project / "bnd/pre.bnd", root, "biz.aQute.launcher.pre", classpath, pre], check=True)
        shutil.copyfile(pre, project / "pre.jar")
    subprocess.run([*command, recipe, root, module, classpath, bundles / (module + ".jar")], check=True)

content = work / "repository"
for module in modules:
    directory = content / module
    directory.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(bundles / (module + ".jar"), directory / f"{module}-{version}.jar")
shutil.copyfile(bundles / "biz.aQute.launcher.pre.jar", content / "biz.aQute.launcher/biz.aQute.launcher.pre.jar")
container = work / "container"
container.mkdir(exist_ok=True)
subprocess.run(["jar", "cf", container / "embedded-repo.jar", "-C", content, "."], check=True)
meta = container / "META-INF/maven/biz.aQute.bnd/biz.aQute.bnd.embedded-repo"
meta.mkdir(parents=True, exist_ok=True)
shutil.copyfile(sources / f"biz.aQute.bnd.embedded-repo-{version}.pom", meta / "pom.xml")
(meta / "pom.properties").write_text(f"groupId=biz.aQute.bnd\nartifactId=biz.aQute.bnd.embedded-repo\nversion={version}\n")
subprocess.run(["jar", "cf", work / f"biz.aQute.bnd.embedded-repo-{version}.jar", "-C", container, "."], check=True)
(work / "classpath").write_text(native_cp)
