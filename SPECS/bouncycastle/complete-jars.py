"""Add upstream OSGi metadata and the JDK-specific classes to the Ant artifacts."""
import os
from pathlib import Path
import re
import subprocess
import sys

version, wrapper = sys.argv[1:]
system = Path("/usr/share/java/javapackages-bootstrap")
bnd = os.pathsep.join(str(system / (n + ".jar")) for n in
                      ("biz.aQute.bndlib", "aQute.libg", "slf4j-api", "osgi.core", "osgi.cmpn"))
out = Path("build/openruyi")
out.mkdir(parents=True, exist_ok=True)
baseline = Path("build/artifacts/jdk1.8/jars")
modules = {"prov": "org.bouncycastle.provider", "util": "org.bouncycastle.util", "pg": "org.bouncycastle.pg"}
base_jars = {m: next(baseline.glob(f"bc{m}-jdk18on-*.jar")).resolve() for m in modules}
archives = os.pathsep.join(map(str, base_jars.values()))
maximum = re.search(r"(?m)^maxVersion=(.+)$", Path("gradle.properties").read_text()).group(1).strip()
built = []
for module, module_name in modules.items():
    gradle = (Path(module) / "build.gradle").read_text()
    packages = re.search(r"String packages = '([^']+)'", gradle)

    def instruction(key):
        line = next(line.strip() for line in gradle.splitlines()
                    if line.strip().startswith(f"manifest.attributes('{key}':"))
        value = line.split(":", 1)[1].strip()[:-1].strip()
        value = value[1:-1].replace(r'\"', '"').replace("${v}", version).replace("${maxVersion}", maximum)
        if packages:
            value = value.replace("${packages}", packages.group(1))
        return value

    jar = out / f"bc{module}-jdk18on-{version}.jar"
    subprocess.run(["java", "-cp", bnd, wrapper, str(base_jars[module]), str(jar), "bc" + module, version,
                    instruction("Export-Package"), instruction("Import-Package"), archives], check=True)

    layers = [(9, [Path(module) / "src/main/jdk1.9"])]
    if module == "prov":
        layers[0][1].append(Path("core/src/main/jdk1.9"))
        layers.extend((v, [Path(module) / ("src/main/" + tree)]) for v, tree in
                      [(11, "jdk1.11"), (15, "jdk1.15"), (17, "jdk17"), (25, "jdk25")])
    previous = []
    tree = out / module / "META-INF/versions"
    for level, roots in layers:
        sources = sorted(source for root in roots for source in root.rglob("*.java"))
        if not sources:
            raise ValueError(f"Missing {module} Java {level} overlay")
        dest = tree / str(level)
        dest.mkdir(parents=True, exist_ok=True)
        args = ["javac", "-encoding", "UTF-8", "-proc:none", "-implicit:none", "-d", str(dest)]
        # The upstream Java 17 provider layer also provides the JDK 21 KEM SPI.
        args += ["-source", "17", "-target", "17"] if level == 17 else ["--release", str(level)]
        local = [*previous, base_jars[module]]
        if any(s.name == "module-info.java" for s in sources):
            args += ["--patch-module", module_name + "=" + os.pathsep.join(map(str, [*roots, *local]))]
            if built:
                args += ["--module-path", os.pathsep.join(map(str, built))]
        else:
            args += ["-classpath", os.pathsep.join(map(str, [*local, *built]))]
        listing = out / module / f"sources-{level}"
        listing.write_text("".join(f'"{source.as_posix()}"\n' for source in sources))
        subprocess.run([*args, "@" + str(listing)], check=True)
        previous.insert(0, dest)
    subprocess.run(["jar", "--update", "--file", str(jar), "-C", str(out / module), "META-INF"], check=True)
    built.append(jar.resolve())
