# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Build JaCoCo's coverage libraries, legacy agent and Maven plugin from source."""
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import os
import shutil
import subprocess

root = Path.cwd()
version = "0.8.14"
revision = "2eb248366f0eb63fd964fc7a81804b27229a6edd"
qualified_version = "0.8.14.202510111229"
runtime_package = "org.jacoco.agent.rt.internal_" + revision[-7:]
repo = root / "build/repo"
repo.mkdir(parents=True, exist_ok=True)
jpb = Path("/usr/share/java/javapackages-bootstrap")
system = Path("/usr/share/maven-repository")
compiler = system / "org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar"
modules = ["org.jacoco.core", "org.jacoco.report", "org.jacoco.agent.rt", "org.jacoco.agent", "jacoco-maven-plugin"]
parent = "org.jacoco.build"
namespace = "http://maven.apache.org/POM/4.0.0"
def artifact_dir(name):
    directory = repo / "org/jacoco" / name / version
    directory.mkdir(parents=True, exist_ok=True)
    return directory

def plugin_version(name):
    with ZipFile(jpb/(name+".jar")) as archive:
        return ET.fromstring(archive.read("META-INF/maven/plugin.xml")).findtext("version")

def maven(name, goals):
    ext = "/usr/share/javapackages-bootstrap/maven/lib/ext"
    env = dict(os.environ)
    env["MAVEN_OPTS"] = env.get("MAVEN_OPTS","")+" -Dmaven.ext.class.path="+ext+"/xmvn.jar:"+ext+"/kojan-xml.jar"
    subprocess.run(["mvn","-B","-o","-f",root/name/"pom.xml","-Dmaven.repo.local="+str(repo),
        "-Dqualified.bundle.version="+qualified_version,"-Dbuild.commitId="+revision,
        "-Djacoco.runtime.package.name="+runtime_package,*goals],check=True,cwd=root,env=env)

for name in [parent,*modules]:
    shutil.copyfile(root/name/"pom.xml", artifact_dir(name)/(name+"-"+version+".pom"))
(root/".mvn").mkdir(exist_ok=True)
(root/".xmvn").mkdir(exist_ok=True)
(root/".xmvn/configuration.xml").write_text(
    "<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository>"
    "<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>")
bundle_plugin=plugin_version("maven-bundle-plugin")
jar_plugin=plugin_version("maven-jar-plugin")
descriptor_plugin=plugin_version("maven-plugin-plugin")
native_cp=[jpb/(n+".jar") for n in ["asm","asm-commons","asm-tree"]]
for name in modules:
    project=root/name
    classes=project/"target/classes"
    classes.mkdir(parents=True, exist_ok=True)
    if name=="org.jacoco.agent":
        agent=root/"org.jacoco.agent.rt/target"/("org.jacoco.agent.rt-"+version+"-all.jar")
        shutil.copyfile(agent,classes/"jacocoagent.jar")
        shutil.copyfile(agent,artifact_dir(name)/(name+"-"+version+"-runtime.jar"))
    source=project/"src"
    files=sorted(source.rglob("*.java"))
    listing=project/"target/java"; listing.write_text("\n".join(map(str,files))+"\n")
    cp=os.pathsep.join(map(str,native_cp))
    if name=="jacoco-maven-plugin":
        deps=[
            system/"org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.jar",
            system/"org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.jar",
            jpb/"file-management.jar",jpb/"maven-plugin-annotations.jar"
        ]
        cp+=":"+os.pathsep.join(map(str,deps))+":/usr/share/maven/lib/*:/usr/share/maven/boot/*"
        cmd=["javac","--release","8","-Xpkginfo:always","-proc:none"]
    else:
        cmd=["java","-jar",str(compiler),"-source","1.5","-target","1.5","-nowarn","-proc:none"]
    subprocess.run([*cmd,"-encoding","UTF-8","-cp",cp,"-d",classes,"@"+str(listing)],check=True)
    for resource in sorted(source.rglob("*")):
        if not resource.is_file() or resource.suffix in (".java",".class"):continue
        target=classes/resource.relative_to(source);target.parent.mkdir(parents=True,exist_ok=True)
        if resource.name=="jacoco.properties":
            values={"qualified.bundle.version":qualified_version,"jacoco.home.url":"http://www.jacoco.org/jacoco","jacoco.runtime.package.name":runtime_package}
            data=resource.read_text().replace("@build.commitId@",revision)
            for key,value in values.items():data=data.replace("$"+"{"+key+"}",value)
            target.write_text(data)
        else:shutil.copyfile(resource,target)
    native_cp.append(classes)
    if name=="org.jacoco.agent.rt":
        maven(name,["org.apache.maven.plugins:maven-jar-plugin:"+jar_plugin+":jar","org.apache.maven.plugins:maven-shade-plugin:3.6.1:shade@default"])
        continue
    if name=="jacoco-maven-plugin":
        maven(name,["org.apache.maven.plugins:maven-plugin-plugin:"+descriptor_plugin+":descriptor"])
    else:
        maven(name,["org.apache.felix:maven-bundle-plugin:"+bundle_plugin+":manifest"])
    meta=classes/"META-INF/maven/org.jacoco"/name;meta.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(project/"pom.xml",meta/"pom.xml")
    target=artifact_dir(name)/(name+"-"+version+".jar")
    manifest=classes/"META-INF/MANIFEST.MF"
    if manifest.exists():subprocess.run(["jar","cfm",target,manifest,"-C",classes,"."],check=True)
    else:subprocess.run(["jar","cf",target,"-C",classes,"."],check=True)
