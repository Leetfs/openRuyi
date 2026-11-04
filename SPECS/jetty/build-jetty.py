# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Build the Jetty server modules with their original JPMS and OSGi metadata."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
from xml.etree import ElementTree as ET
from zipfile import ZipFile

parser = argparse.ArgumentParser()
parser.add_argument('source', type=Path)
parser.add_argument('output', type=Path)
args = parser.parse_args()
root = args.source.resolve()
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=True)
work = out/'work'
repo = work/'repo'
work.mkdir(exist_ok=True)
repo.mkdir(exist_ok=True)
(work/'.mvn').mkdir(exist_ok=True)
(work/'.xmvn').mkdir(exist_ok=True)
(work/'.xmvn/configuration.xml').write_text('<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository><repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>')
ns = 'http://maven.apache.org/POM/4.0.0'
ET.register_namespace('', ns)
q = lambda s: '{'+ns+'}'+s
env=dict(os.environ)
ext='/usr/share/javapackages-bootstrap/maven/lib/ext'
env['MAVEN_OPTS']=env.get('MAVEN_OPTS','')+' -Dmaven.ext.class.path='+ext+'/xmvn.jar:'+ext+'/kojan-xml.jar'
platform='/usr/share/maven-repository'
modules = ['jetty-util','jetty-jmx','jetty-io','jetty-http','jetty-server','jetty-security','jetty-session','jetty-util-ajax','jetty-ee10-servlet']
modulepath=[Path(platform+'/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.jar'),Path(platform+'/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.jar')]
version='12.1.14'
with ZipFile('/usr/share/java/javapackages-bootstrap/maven-bundle-plugin.jar') as z:
 bundle_version=ET.fromstring(z.read('META-INF/maven/plugin.xml')).findtext('version')
def install_pom(file):
 x=ET.parse(file).getroot()
 g=x.findtext(q('groupId')) or x.findtext(q('parent')+'/'+q('groupId'))
 name=x.findtext(q('artifactId'))
 dest=repo/Path(*g.split('.'))/name/version
 dest.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(file,dest/(name+'-'+version+'.pom'))
 return x,g,name,dest
parent,_,_,parent_dir=install_pom(root/'pom.xml')
# The upstream extensions publish artifacts and cache remote Maven builds.
# Keep the published parent intact for installation and omit these extensions in the isolated manifest build.
build=parent.find(q('build')); extensions=build.find(q('extensions'))
assert {e.findtext(q('artifactId')) for e in extensions}=={'extension3','maven-build-cache-extension'}
build.remove(extensions)
# Manifest analysis only needs production dependencies. Upstream tests run separately.
parent_deps=parent.find(q('dependencies'))
for dependency in list(parent_deps):
 if dependency.findtext(q('scope'),'compile')=='test':parent_deps.remove(dependency)
ET.ElementTree(parent).write(parent_dir/('jetty-project-'+version+'.pom'),encoding='utf-8',xml_declaration=True)
for path in ['jetty-core/pom.xml','jetty-ee10/pom.xml']:install_pom(root/path)
for name in modules:
 source=root/('jetty-ee10' if name=='jetty-ee10-servlet' else 'jetty-core')/name
 model,group,artifact,dest=install_pom(source/'pom.xml')
 assert artifact==name
 stage=work/name
 stage.mkdir(exist_ok=True)
 cls=stage/'target/classes'
 cls.mkdir(parents=True)
 files=sorted((source/'src/main/java').rglob('*.java'))
 listing=stage/'sources';listing.write_text('\n'.join(map(str,files))+'\n')
 subprocess.run(['javac','--release','17','--module-version',version,'--module-path',os.pathsep.join(map(str,modulepath)),'-proc:none','-encoding','UTF-8','-d',cls,'@'+str(listing)],check=True)
 resources=source/'src/main/resources'
 if resources.exists():shutil.copytree(resources,cls,dirs_exist_ok=True)
 if name=='jetty-util':
  props=cls/'org/eclipse/jetty/version/build.properties'
  values={'buildNumber':'15cecbd757a2f6b0fdc6a8944f4c6d0020b17da0','timestamp':'1790920085032','project.version':version,'project.scm.connection':'scm:git:https://github.com/jetty/jetty.project.git/jetty-core/jetty-util'}
  data=props.read_text()
  for k,v in values.items(): data=data.replace('$'+'{'+k+'}',v)
  assert '$'+'{' not in data;props.write_text(data)
 tree=ET.Element(q('project'));ET.SubElement(tree,q('modelVersion')).text='4.0.0'
 # The published root supplies the original OSGi instructions and all dependency versions.
 pr=ET.SubElement(tree,q('parent'))
 original_parent=model.find(q('parent'))
 for key,value in [(key,original_parent.findtext(q(key))) for key in ('groupId','artifactId','version')]+[('relativePath','')]:
  ET.SubElement(pr,q(key)).text=value
 for key in ['groupId','artifactId','version','name','properties']:
  value=model.find(q(key))
  if value is not None:tree.append(value)
 if tree.find(q('groupId')) is None:ET.SubElement(tree,q('groupId')).text=group
 deps=ET.SubElement(tree,q('dependencies'))
 for dep in model.findall(q('dependencies')+'/'+q('dependency')):
  if dep.findtext(q('scope'),'compile') not in ('test','provided'):deps.append(dep)
 build=ET.SubElement(tree,q('build'));plugins=ET.SubElement(build,q('plugins'));plugin=ET.SubElement(plugins,q('plugin'))
 for key,value in [('groupId','org.apache.felix'),('artifactId','maven-bundle-plugin'),('version',bundle_version)]:ET.SubElement(plugin,q(key)).text=value
 for raw in model.findall(q('build')+'/'+q('plugins')+'/'+q('plugin')):
  if raw.findtext(q('artifactId'))=='maven-bundle-plugin' and raw.find(q('configuration')) is not None: plugin.append(raw.find(q('configuration')))
 pom=stage/'pom.xml';ET.ElementTree(tree).write(pom,encoding='utf-8',xml_declaration=True)
 subprocess.run(['mvn','-B','-o','-f',pom,'-Dmaven.repo.local='+str(repo),'org.apache.felix:maven-bundle-plugin:'+bundle_version+':manifest'],check=True,cwd=work,env=env)
 jar=out/(name+'.jar')
 subprocess.run(['jar','cfm',jar,cls/'META-INF/MANIFEST.MF','-C',cls,'.'],check=True)
 shutil.copyfile(jar,dest/(name+'-'+version+'.jar'));modulepath.append(jar)
 print('Built',name,flush=True)
