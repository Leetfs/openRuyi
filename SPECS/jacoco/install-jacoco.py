# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Install the coverage libraries, plugin and standalone runtime agent."""
from pathlib import Path
import shutil
import sys
from xml.etree import ElementTree as ET

buildroot=Path(sys.argv[1])
share=Path(sys.argv[2])
version="0.8.14"
artifacts=ET.Element("artifacts")
for name in ["org.jacoco.build","org.jacoco.core","org.jacoco.report","org.jacoco.agent","jacoco-maven-plugin"]:
    local=Path("build/repo/org/jacoco")/name/version
    directory=share/"maven-repository/org/jacoco"/name/version
    target=buildroot/directory.relative_to("/")
    target.mkdir(parents=True,exist_ok=True)
    entries=[("pom",None)]
    if name!="org.jacoco.build":entries.append(("jar",None))
    if name=="org.jacoco.agent":entries.append(("jar","runtime"))
    for extension,classifier in entries:
        filename=name+"-"+version+("-"+classifier if classifier else "")+"."+extension
        shutil.copyfile(local/filename,target/filename)
        item=ET.SubElement(artifacts,"artifact")
        for key,value in [("groupId","org.jacoco"),("artifactId",name),("version",version),("extension",extension)]:
            ET.SubElement(item,key).text=value
        if classifier:ET.SubElement(item,"classifier").text=classifier
        ET.SubElement(item,"path").text=str(directory/filename)
        if extension=="pom":
            props=ET.SubElement(item,"properties")
            ET.SubElement(props,"xmvn.resolver.disableEffectivePom").text="true"
        else:
            compat=ET.SubElement(item,"compatVersions")
            for value in [version,"SYSTEM"]:ET.SubElement(compat,"version").text=value
metadata=ET.Element("metadata")
metadata.append(artifacts)
ET.indent(metadata)
path=buildroot/share.relative_to("/")/"maven-metadata/jacoco.xml"
path.parent.mkdir(parents=True,exist_ok=True)
ET.ElementTree(metadata).write(path,encoding="utf-8",xml_declaration=True)
