# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Run the Apache Invoker fixtures against the staged plugin in an isolated Maven repository."""
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tarfile
from xml.etree import ElementTree as ET

buildroot, antlr_source, ant_task, verifier = map(Path, sys.argv[1:])
root = Path("target/invoker").resolve()
repo = root / "local-repo"
root.mkdir(parents=True)
repo.mkdir()
bootstrap = Path("/usr/share/java/javapackages-bootstrap")
system_repo = Path("/usr/share/maven-repository")
staged = root / "plugin.xml"
staged.write_text((buildroot / "usr/share/maven-metadata/maven-antrun-plugin.xml").read_text()
                  .replace("<path>/usr/", f"<path>{buildroot}/usr/"))
junit_version = "5.12.2"

# The plugin-classpath fixture runs ANTLR 2.7.4 using the Ant 1.6.5 task.
fixture = root / "antlr"
fixture.mkdir()
with tarfile.open(antlr_source) as archive:
    for member in archive.getmembers():
        relative = Path(*Path(member.name).parts[1:])
        if member.isfile() and relative.parts[:1] == ("antlr",) and relative.suffix == ".java":
            target = fixture / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.extractfile(member).read())
task_src = fixture / "ANTLR.java"
shutil.copyfile(ant_task, task_src)
for group, name, version, sources in [
    ("antlr", "antlrall", "2.7.4", sorted((fixture / "antlr").rglob("*.java"))),
    ("ant", "ant-antlr", "1.6.5", [task_src]),
]:
    classes = fixture / name
    classes.mkdir()
    subprocess.run(["javac", "--release", "8", "-proc:none", "-nowarn", "-encoding", "ISO-8859-1",
                    "-cp", f"{bootstrap}/ant.jar:{bootstrap}/ant-launcher.jar", "-d", classes, *sources], check=True)
    dest = repo / group / name / version
    dest.mkdir(parents=True)
    subprocess.run(["jar", "cf", dest / f"{name}-{version}.jar", "-C", classes, "."], check=True)
    (dest / f"{name}-{version}.pom").write_text(f"<project><modelVersion>4.0.0</modelVersion><groupId>{group}</groupId>"
                                                f"<artifactId>{name}</artifactId><version>{version}</version></project>")

# Aggregate Ant FileSets are relative to the Maven repository. XMvn resolves individual files by RPM path.
paths = [
    ("org/apache/ant", "ant", "1.10.14"), ("org/apache/ant", "ant-launcher", "SYSTEM"),
    ("jakarta/activation", "jakarta.activation-api", "SYSTEM"), ("jakarta/mail", "jakarta.mail-api", "SYSTEM"),
    ("org/junit/jupiter", "junit-jupiter-engine", junit_version), ("org/junit/jupiter", "junit-jupiter-api", junit_version),
    ("org/junit/platform", "junit-platform-engine", "1.12.2"), ("org/junit/platform", "junit-platform-commons", "1.12.2"),
    ("org/opentest4j", "opentest4j", "1.3.0"), ("org/apiguardian", "apiguardian-api", "1.1.2"),
]
for group, name, version in paths:
    rel = Path(group, name, version, f"{name}-{version}.jar")
    source = system_repo / rel
    if not source.is_file():
        source = bootstrap / (name + ".jar")
    if not source.is_file():
        raise FileNotFoundError(source)
    dest = repo / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.symlink_to(source)

bsh = system_repo / "org/apache-extras/beanshell/bsh/2.1.1/bsh-2.1.1.jar"
subprocess.run(["javac", "-cp", bsh, "-d", root, verifier], check=True)
jcp = f"{root}:{bsh}:/usr/share/maven/lib/*:{bootstrap}/plexus-utils.jar"
tools = {"maven-clean-plugin": "3.5.0", "maven-resources-plugin": "3.5.0", "maven-compiler-plugin": "3.12.1.MBI",
         "maven-surefire-plugin": "3.5.5", "maven-jar-plugin": "3.3.0.MBI", "maven-install-plugin": "3.1.4"}

def plugin_version(match):
    block = match.group()
    plugins = re.search(r"<artifactId>([^<]+)</artifactId>", block)
    if plugins and plugins[1] in tools:
        return re.sub(r"<version>[^<]+</version>", f"<version>{tools[plugins[1]]}</version>", block, count=1)
    return block

def properties(file):
    if not file.is_file():
        return {}
    return dict(tuple(v.strip() for v in line.split("=", 1)) for line in file.read_text().splitlines()
                if line.strip() and not line.lstrip().startswith("#") and "=" in line)

config = f"""<configuration><resolverSettings><metadataRepositories><repository>{staged}</repository>
<repository>/usr/share/maven-metadata</repository><repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>"""
fixtures = root / "it"
shutil.copytree("src/it", fixtures)
verified = 0
for pom in sorted(fixtures.glob("*/pom.xml")):
    d = pom.parent
    xml = pom.read_text().replace("@pom.version@", "3.2.0").replace("@versions.junit5@", junit_version)
    xml = re.sub(r"<plugin(?:\s[^>]*)?>.*?</plugin>", plugin_version, xml, flags=re.S)
    if d.name == "MANTRUN-221":
        # This fixture checks propagation into Ant of a property set in the same Maven session.
        plugin = """<plugin><groupId>org.codehaus.mojo</groupId><artifactId>build-helper-maven-plugin</artifactId><version>3.6.1</version>
<executions><execution><phase>validate</phase><goals><goal>bsh-property</goal></goals><configuration>
<source>String json = new String(java.nio.file.Files.readAllBytes(new File(project.getBasedir(), "package.json").toPath()), "UTF-8");
int key = json.indexOf("version"); int colon = json.indexOf(":", key);
int begin = json.indexOf(34, colon); int end = json.indexOf(34, begin + 1);
if (key == -1 || end == -1) throw new IllegalArgumentException("Missing version");
prop1 = json.substring(begin + 1, end);</source><properties><property>prop1</property></properties>
</configuration></execution></executions></plugin>"""
        xml, n = re.subn(r"<plugin>\s*<groupId>ca.szc.maven</groupId>.*?</plugin>", lambda _: plugin, xml, count=1, flags=re.S)
        assert n == 1
    pom.write_text(xml)
    (d / ".xmvn").mkdir(exist_ok=True)
    (d / ".xmvn/configuration.xml").write_text(config)
    cfg = properties(d / "invoker.properties")
    goals = cfg.get("invoker.goals", "verify").replace("$" + "{project.groupId}:$" + "{project.artifactId}:$" + "{project.version}",
                                                        "org.apache.maven.plugins:maven-antrun-plugin:3.2.0")
    cmd = ["mvn", "-B", "-o", f"-Dmaven.repo.local={repo}", *shlex.split(goals)]
    if "invoker.profiles" in cfg:
        cmd.append("-P" + cfg["invoker.profiles"])
    cmd.extend(f"-D{k}={v}" for k, v in properties(d / "test.properties").items())
    with (d / "build.log").open("w") as log:
        rc = subprocess.run(cmd, cwd=d, stdout=log, stderr=subprocess.STDOUT, timeout=120).returncode
    if (rc == 0) != (cfg.get("invoker.buildResult", "success") == "success"):
        print((d / "build.log").read_text()[-4200:])
        raise RuntimeError(d.name)
    if d.name == "filesets-test":
        check = d / "verify.bsh"
        text = check.read_text().replace("5.13.1.jar", junit_version + ".jar")
        check.write_text(text.replace('depsDir, "ant-1.10.14.jar"', 'depsDir, "ant.jar"'))
    if (d / "verify.bsh").is_file():
        subprocess.run(["java", "-cp", jcp, "CheckInvoker", d, repo], cwd=d, check=True)
    if (d / "verify.groovy").is_file():
        # The five XML assertions in custom-ant-target-attributes/verify.groovy.
        assert d.name == "custom-ant-target-attributes"
        project = ET.parse(d / "target/antrun/build-myname.xml").getroot()
        assert project.get("default") == "myname"
        targets = project.findall("target")
        assert len(targets) == 1 and targets[0].attrib == {"name": "myname", "description": "Foo"}
    if d.name == "plugin-classpath-test":
        assert all((d / "target" / (name + ".java")).is_file() for name in ("CalcLexer", "CalcParser", "CalcTreeWalker"))
    print("Verified", d.name, flush=True)
    verified += 1
assert verified == 29, verified
