"""Build the four upstream Site Tools modules with the installed Maven libraries."""
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

version, index_source, generator = sys.argv[1:]
root = Path.cwd()
repo = Path("/usr/share/maven-repository")
bootstrap = Path("/usr/share/java/javapackages-bootstrap")
target = root / "target"
target.mkdir(exist_ok=True)

coordinates = [
    ("org.apache.maven.doxia", "doxia-sink-api", "2.0.0"),
    ("org.apache.maven.doxia", "doxia-core", "2.0.0"),
    ("org.apache.maven.doxia", "doxia-module-apt", "2.0.0"),
    ("org.apache.maven.doxia", "doxia-module-fml", "2.0.0"),
    ("org.apache.maven.doxia", "doxia-module-xdoc", "2.0.0"),
    ("org.apache.maven.doxia", "doxia-module-xhtml5", "2.0.0"),
    ("org.apache.maven.reporting", "maven-reporting-api", "4.0.0"),
    ("org.codehaus.plexus", "plexus-i18n", "1.1.0"),
    ("org.codehaus.plexus", "plexus-velocity", "2.2.0"),
    ("org.apache.velocity.tools", "velocity-tools-generic", "3.1"),
    ("org.apache.commons", "commons-lang3", "3.20.0"),
    ("org.apache.commons", "commons-text", "1.12.0"),
    ("org.apache.commons", "commons-digester3", "3.2"),
    ("commons-io", "commons-io", "2.21.0"),
    ("cglib", "cglib", "3.2.9"),
    ("com.github.cliftonlabs", "json-simple", "3.0.2"),
]
classpath = []
for group, artifact, release in coordinates:
    jar = repo / group.replace(".", "/") / artifact / release / f"{artifact}-{release}.jar"
    if not jar.is_file():
        raise SystemExit(f"Required installed artifact is missing: {jar}")
    classpath.append(str(jar))

# Maven 3 and Resolver 1 precede bootstrap libraries. Bootstrap aggregate JARs
# containing Maven 4 or Resolver 2 service providers cannot share this container.
classpath.extend(str(p) for p in sorted(Path("/usr/share/maven/lib").glob("*.jar")))
classpath.extend(str(p) for p in sorted(Path("/usr/share/maven/boot").glob("*.jar")))
incompatible = {
    "org/apache/maven/ReactorReaderSpy.class",
    "org/apache/maven/model/profile/activation/PackagingProfileActivator.class",
    "org/eclipse/aether/transport/jdk/JdkTransporter.class",
}
for jar in sorted(bootstrap.glob("*.jar")):
    with zipfile.ZipFile(jar) as archive:
        if incompatible.intersection(archive.namelist()):
            continue
    classpath.append(str(jar))
index_classes = target / "tools"
subprocess.run(["javac", "-cp", ":".join(classpath), "-d", str(index_classes),
                index_source], check=True)
for name in ("doxia-site-model", "doxia-skin-model", "doxia-integration-tools", "doxia-site-renderer"):
    module = root / name
    if (module / "src/main/mdo").is_dir():
        subprocess.run([sys.executable, generator, str(module), str(target / "model-repository")],
                       check=True)
    classes = module / "target/classes"
    classes.mkdir(parents=True, exist_ok=True)
    sources = sorted((module / "src/main/java").rglob("*.java"))
    sources.extend(sorted((module / "target/generated-sources/modello").rglob("*.java")))
    source_list = module / "target/sources"
    source_list.write_text("".join(str(source) + "\n" for source in sources))
    subprocess.run(["javac", "--release", "8", "-proc:none", "-encoding", "UTF-8", "-g",
                    "-cp", ":".join(classpath), "-d", str(classes), "@" + str(source_list)],
                   check=True)
    resources = module / "src/main/resources"
    if resources.exists():
        shutil.copytree(resources, classes, dirs_exist_ok=True)
    subprocess.run(["java", "-cp", ":".join([str(index_classes), str(classes)] + classpath),
                    "IndexNative", str(classes)], check=True)
    metadata = classes / "META-INF/maven/org.apache.maven.doxia" / name
    metadata.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(module / "pom.xml", metadata / "pom.xml")
    (metadata / "pom.properties").write_text(
        f"groupId=org.apache.maven.doxia\nartifactId={name}\nversion={version}\n")
    for document in ("LICENSE", "NOTICE"):
        shutil.copyfile(root / document, classes / "META-INF" / document)
    jar = module / "target" / (name + ".jar")
    subprocess.run(["jar", "cf", str(jar), "-C", str(classes), "."], check=True)
    classpath.insert(0, str(jar))
(target / "production-classpath").write_text(":".join(classpath) + "\n")
