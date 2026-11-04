# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Build the prior-release JUnit provider used by the Surefire reactor."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

source,work=map(lambda value:Path(value).resolve(),sys.argv[1:3])
repo=work/'repo'
repo.mkdir(parents=True,exist_ok=True)
(work/'.mvn').mkdir(exist_ok=True);(work/'.xmvn').mkdir(exist_ok=True)
(work/'.xmvn/configuration.xml').write_text('<configuration><resolverSettings><metadataRepositories><repository>$NATIVE_METADATA</repository><repository>/usr/share/maven-metadata</repository><repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>')
jpb=Path('/usr/share/java/javapackages-bootstrap')
cfg=work/'.xmvn/configuration.xml'
cfg.write_text(cfg.read_text().replace('$NATIVE_METADATA',str(work/'.xmvn/native.xml')))
native=ET.Element('metadata');artifacts=ET.SubElement(native,'artifacts')
ET.ElementTree(native).write(work/'.xmvn/native.xml')
ns='http://maven.apache.org/POM/4.0.0';ET.register_namespace('',ns);q=lambda k:'{'+ns+'}'+k
group='org.apache.maven.surefire';v='3.5.2'
with ZipFile(jpb/'maven-jar-plugin.jar') as z:jar_plugin=ET.fromstring(z.read('META-INF/maven/plugin.xml')).findtext('version')
env=dict(os.environ);ext='/usr/share/javapackages-bootstrap/maven/lib/ext';env['MAVEN_OPTS']=env.get('MAVEN_OPTS','')+' -Dmaven.ext.class.path='+ext+'/xmvn.jar:'+ext+'/kojan-xml.jar'
versions={'maven-shared-utils':'3.3.4','commons-io':'2.17.0','commons-lang3':'3.17.0','commons-compress':'1.27.1'}
modules=['surefire-shared-utils','surefire-logger-api','surefire-api','surefire-extensions-api','surefire-extensions-spi','surefire-booter','surefire-providers/common-java5','surefire-providers/surefire-junit-platform','surefire-shadefire']
libs=[]
for path in modules:
    name=Path(path).name;original=source/path
    model=ET.parse(original/'pom.xml').getroot()
    stage=work/name;classes=stage/'target/classes';classes.mkdir(parents=True,exist_ok=True)
    java=sorted((original/'src/main/java').rglob('*.java'))
    if java:
        listing=stage/'sources';listing.write_text('\n'.join(map(str,java))+'\n')
        cp=os.pathsep.join([*map(str,libs),str(jpb/'*')])
        subprocess.run(['javac','--release','8','-Xpkginfo:always','-proc:none','-encoding','UTF-8','-cp',cp,'-d',classes,'@'+str(listing)],check=True)
    resources=original/'src/main/resources'
    if resources.exists():shutil.copytree(resources,classes,dirs_exist_ok=True)
    root=ET.Element(q('project'))
    for key,value in [('modelVersion','4.0.0'),('groupId',group),('artifactId',name),('version',v)]:ET.SubElement(root,q(key)).text=value
    deps=ET.SubElement(root,q('dependencies'))
    for dep in model.findall(q('dependencies')+'/'+q('dependency')):
        g=dep.findtext(q('groupId'));art=dep.findtext(q('artifactId'));scope=dep.findtext(q('scope'),'compile')
        if scope in ['test','provided'] or art in ['jsr305','junit-platform-engine','junit-platform-launcher']:continue
        if g in ('$'+'{project.groupId}',group):g=group;dv=v
        elif art in versions:dv=versions[art]
        else:continue
        x=ET.SubElement(deps,q('dependency'))
        for k,value in [('groupId',g),('artifactId',art),('version',dv)]:ET.SubElement(x,q(k)).text=value
    if name in ['surefire-shared-utils','surefire-shadefire']:
        # XMvn also has bootstrap versions of these artifacts. Pin every input at the
        # same resolution depth so a bootstrap transitive POM cannot override it.
        if name=='surefire-shared-utils':
            direct=[('org.apache.maven.shared','maven-shared-utils','3.3.4'),('commons-io','commons-io','2.17.0'),
                    ('org.apache.commons','commons-lang3','3.17.0'),('org.apache.commons','commons-compress','1.27.1'),
                    ('commons-codec','commons-codec','1.17.1')]
        else:
            direct=[(group,n,v) for n in ['surefire-junit-platform','common-java5','surefire-shared-utils',
                                           'surefire-api','surefire-logger-api','surefire-booter','surefire-extensions-spi']]
        deps.clear()
        for owner,artifact,version in direct:
            dependency=ET.SubElement(deps,q('dependency'))
            for key,value in [('groupId',owner),('artifactId',artifact),('version',version)]:
                ET.SubElement(dependency,q(key)).text=value
            exclusion=ET.SubElement(ET.SubElement(dependency,q('exclusions')),q('exclusion'))
            ET.SubElement(exclusion,q('groupId')).text='*'
            ET.SubElement(exclusion,q('artifactId')).text='*'
    plugin=next((x for x in model.findall('.//'+q('plugin')) if x.findtext(q('artifactId'))=='maven-shade-plugin'),None)
    if plugin is not None:
        pl=ET.SubElement(ET.SubElement(root,q('build')),q('plugins'));pl.append(plugin)
        ver=plugin.find(q('version'))
        if ver is None:ver=ET.SubElement(plugin,q('version'))
        ver.text='3.6.1'
    pom=stage/'pom.xml';ET.ElementTree(root).write(pom,encoding='utf-8',xml_declaration=True)
    target=repo/Path(*group.split('.'))/name/v;target.mkdir(parents=True,exist_ok=True)
    dest=target/(name+'-'+v+'.jar')
    if plugin is not None:
        if (original/'src').exists():
            # Original IncludeResourceTransformer paths are relative to the project.
            (stage/'src').symlink_to(original/'src',target_is_directory=True)
        cmd=['mvn','-o','-B','-f',pom,'-Dmaven.repo.local='+str(repo),'org.apache.maven.plugins:maven-jar-plugin:'+jar_plugin+':jar','org.apache.maven.plugins:maven-shade-plugin:3.6.1:shade@default']
        subprocess.run(cmd,check=True,cwd=work,env=env)
        shutil.copyfile(stage/'target'/(name+'-'+v+'.jar'),dest)
    else:
        subprocess.run(['jar','cf',dest,'-C',classes,'.'],check=True)
    shutil.copyfile(pom,target/(name+'-'+v+'.pom'))
    for ext,file in [('jar',dest),('pom',target/(name+'-'+v+'.pom'))]:
        entry=ET.SubElement(artifacts,'artifact')
        for key,value in [('groupId',group),('artifactId',name),('version',v),('extension',ext),('path',str(file))]:
            ET.SubElement(entry,key).text=value
        if ext=='jar':ET.SubElement(ET.SubElement(entry,'compatVersions'),'version').text=v
        else:ET.SubElement(ET.SubElement(entry,'properties'),'xmvn.resolver.disableEffectivePom').text='true'
    ET.ElementTree(native).write(work/'.xmvn/native.xml',encoding='utf-8',xml_declaration=True)
    libs.append(dest);print('Source-built',name,flush=True)
