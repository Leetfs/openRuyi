"""Run the original model, integration and HTML renderer suites."""
from pathlib import Path
import shutil
import subprocess
import sys

fixture_builder, source_directory = sys.argv[1:]
root = Path.cwd()
repo = Path("/usr/share/maven-repository")
classpath = (root / "target/production-classpath").read_text().strip().split(":")
tests = repo / "org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0-tests.jar"
classpath.insert(0, str(tests))
for group, version in (("org/junit/jupiter", "5.12.2"), ("org/junit/platform", "1.12.2"),
                        ("org/mockito/mockito-core", "4.11.0"),
                        ("org/ow2/asm", "9.10.1"),
                        ("org/codehaus/plexus/plexus-testing", "2.1.0"),
                        ("commons-net/commons-net", "3.13.0")):
    jars = sorted((repo / group).rglob("*-" + version + ".jar"))
    if not jars:
        raise SystemExit(f"Required test dependency is missing: {group} {version}")
    classpath[0:0] = [str(jar) for jar in jars]
(root / "target/test-classpath").write_text(":".join(classpath) + "\n")
subprocess.run([sys.executable, fixture_builder, source_directory], check=True)
classpath[0:0] = (root / "target/htmlunit-classpath").read_text().strip().split(":")
launcher = root / "target/launcher"
subprocess.run(["javac", "-cp", ":".join(classpath), "-d", str(launcher),
                "/usr/libexec/eclipse-equinox/RunJupiter.java"], check=True)
classpath.insert(0, str(launcher))
for name in ("doxia-site-model", "doxia-integration-tools", "doxia-site-renderer"):
    module = root / name
    classes = module / "target/test-classes"
    classes.mkdir(parents=True, exist_ok=True)
    sources = sorted((module / "src/test/java").rglob("*.java"))
    source_list = module / "target/test-sources"
    source_list.write_text("".join(str(p) + "\n" for p in sources))
    subprocess.run(["javac", "--release", "11", "-proc:none", "-encoding", "UTF-8", "-g",
                    "-cp", ":".join(classpath), "-d", str(classes), "@" + str(source_list)],
                   check=True)
    resources = module / "src/test/resources"
    if resources.exists():
        shutil.copytree(resources, classes, dirs_exist_ok=True)
    tests = [".".join(p.relative_to(module / "src/test/java").with_suffix("").parts)
             for p in sources if p.name.endswith("Test.java")]
    subprocess.run(["java", "--add-exports",
                    "java.xml/com.sun.org.apache.xerces.internal.dom=ALL-UNNAMED",
                    "-Dbasedir=" + str(module),
                    "-cp", ":".join([str(classes)] + classpath), "RunJupiter", *tests],
                   cwd=module, check=True)
