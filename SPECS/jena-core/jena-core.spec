# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jena-core
Version:        6.2.0
Release:        %autorelease
Summary:        Apache Jena RDF model and inference libraries
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://jena.apache.org/
VCS:            git:https://github.com/apache/jena.git
#!RemoteAsset:  sha256:fdd8e9b6c9e62db3dcf33728b7586351015e67e854e82f9b6e1e09690b003351
Source0:        https://downloads.apache.org/jena/source/jena-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  caffeine
BuildRequires:  dexx-collection
BuildRequires:  roaringbitmap
BuildRequires:  commons-compress
BuildRequires:  commons-codec
BuildRequires:  commons-io
BuildRequires:  commons-lang3
BuildRequires:  jspecify
BuildRequires:  slf4j
BuildRequires:  slf4j-jdk14

Requires:       caffeine
Requires:       dexx-collection
Requires:       roaringbitmap
Requires:       commons-compress
Requires:       commons-codec
Requires:       commons-io
Requires:       commons-lang3
Requires:       slf4j

%description
Jena Core provides RDF graphs, models, ontology support and inference.
This package includes the base utilities, IRI and language-tag modules
needed by the RDF library. Logging uses the application's SLF4J provider;
the optional command-line logging configuration adapters are not included.

%prep
%autosetup -n jena-%{version}

%build
deps=%{_datadir}/java/caffeine.jar:%{_datadir}/java/dexx-collection.jar:%{_datadir}/java/roaringbitmap.jar:%{_datadir}/java/commons-compress.jar:%{_datadir}/java/commons-codec.jar:%{_datadir}/java/jspecify.jar:%{_datadir}/java/slf4j-api.jar
for artifact in commons-io/commons-io org/apache/commons/commons-lang3; do
    jar=$(find %{_datadir}/maven-repository/"$artifact" -name '*.jar' -print -quit)
    test -n "$jar"
    deps="$deps:$jar"
done
printf '%s\n' "$deps" > dependencies.classpath
for module in jena-iri3986 jena-langtag jena-base jena-core; do
    mkdir -p "build/$module"
    # LogCtl adapters configure optional logging providers for Jena command-line
    # tools. The RDF libraries log through SLF4J and do not call these adapters.
    find "$module/src/main/java" -name '*.java' ! -name module-info.java ! -name 'LogCtl*.java' | sort > "$module.list"
    javac --release 25 -encoding UTF-8 -cp "$deps" -d "build/$module" @"$module.list"
    if test -d "$module/src/main/resources"; then
        cp -a "$module/src/main/resources/." "build/$module/"
    fi
    cat > "$module.mf" <<MANIFEST
Manifest-Version: 1.0
Implementation-Title: $module
Implementation-Version: %{version}

MANIFEST
    jar --create --file "$module.jar" --manifest "$module.mf" -C "build/$module" .
    deps="$deps:$module.jar"
done
printf '%s\n' "$deps" > test.classpath

%install
for module in jena-iri3986 jena-langtag jena-base jena-core; do
    install -Dpm644 "$module.jar" %{buildroot}%{_datadir}/java/"$module.jar"
done

%check
# Exercise RDF model edits, resource renaming and the legacy RDF/XML parser and writer.
# These are the interfaces used by ODFDOM to extract package RDF metadata.
# The broader upstream suites require JUnit Jupiter and ARQ integration fixtures.
cat > RdfCheck.java <<'JAVA'
import java.io.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.rdfxml.arp1.RDFXMLReader;
import org.apache.jena.rdfxml.xmloutput.impl.RDFXML_Basic;
import org.apache.jena.util.ResourceUtils;
import org.apache.jena.vocabulary.RDF;
import org.apache.jena.vocabulary.RDFS;
class RdfCheck {
    public static void main(String[] args) {
        String xml="<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns:x='urn:test:'>"
            +"<rdf:Description rdf:about='urn:old'><x:title xml:lang='en'>Example</x:title></rdf:Description></rdf:RDF>";
        Model model=ModelFactory.createDefaultModel();
        new RDFXMLReader().read(model,new StringReader(xml),"urn:base:");
        Resource subject=ResourceUtils.renameResource(model.getResource("urn:old"),"urn:new");
        if (model.size()!=1 || !model.contains(subject,model.createProperty("urn:test:title"),"Example","en"))
            throw new AssertionError("RDF extraction or resource rename");
        StringWriter output=new StringWriter();
        new RDFXML_Basic().write(model,output,"urn:base:");
        Model restored=ModelFactory.createDefaultModel();
        new RDFXMLReader().read(restored,new StringReader(output.toString()),"urn:base:");
        if (!model.isIsomorphicWith(restored)) throw new AssertionError("RDF/XML round trip");
        Resource parent=model.createResource("urn:Parent");
        Resource child=model.createResource("urn:Child");
        model.add(child,RDFS.subClassOf,parent);
        model.add(subject,RDF.type,child);
        InfModel inferred=ModelFactory.createRDFSModel(model);
        if (!inferred.contains(subject,RDF.type,parent)) throw new AssertionError("RDFS inference");
        System.out.println("RDF/XML extraction, rename, round trip and inference passed");
    }
}
JAVA
deps="$(cat test.classpath):%{_datadir}/java/slf4j-jdk14.jar"
javac -cp "$deps" RdfCheck.java
java -cp ".:$deps" RdfCheck

%files
%license LICENSE NOTICE
%doc README.md
%{_datadir}/java/jena-base.jar
%{_datadir}/java/jena-core.jar
%{_datadir}/java/jena-iri3986.jar
%{_datadir}/java/jena-langtag.jar

%changelog
%autochangelog
