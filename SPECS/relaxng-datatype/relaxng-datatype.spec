# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           relaxng-datatype
Version:        1.0
Release:        %autorelease
Summary:        Java datatype library interfaces for RELAX NG
License:        BSD-3-Clause
URL:            https://relaxng.org/
VCS:            https://sourceforge.net/p/relaxng/code/
#!RemoteAsset:  sha256:7be15d1beb7faf895d5a7abff793ba324c4753d319236f40941ee63949f65eb2
Source0:        https://downloads.sourceforge.net/project/relaxng/datatype%20%28java%29/Ver.%{version}/relaxngDatatype-%{version}.zip
# Preserve service discovery for class loaders that expose one resource at a time.
# https://github.com/relaxng/jing-trang/commit/cc0bb93b09682bbec32f42d6a436adf6849cf12b
Patch1000:      1000-load-providers-with-single-resource-class-loaders.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip

%description
These interfaces connect Java XML validators to RELAX NG datatype
libraries. They define datatype builders, lexical validation, streaming
validation and service-provider discovery.

%prep
%setup -q -n relaxngDatatype-%{version}
rm -f relaxngDatatype.jar
# Normalize the original ZIP's CRLF source before applying the upstream change.
sed -i 's/\r$//' src/org/relaxng/datatype/helpers/DatatypeLibraryLoader.java
%patch -P 1000 -p1

%build
mkdir classes
find src -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
jar --create --file relaxngDatatype.jar -C classes .

%install
install -Dpm644 relaxngDatatype.jar %{buildroot}%{_datadir}/java/relaxngDatatype.jar

%check
mkdir -p tests/META-INF/services
cat > tests/CheckLoader.java <<'JAVA'
import java.net.URL;
import java.util.Collections;
import java.util.Enumeration;
import org.relaxng.datatype.*;
import org.relaxng.datatype.helpers.DatatypeLibraryLoader;
public class CheckLoader implements DatatypeLibraryFactory, DatatypeLibrary {
    public DatatypeLibrary createDatatypeLibrary(String uri) {
        return "urn:test".equals(uri) ? this : null;
    }
    public Datatype createDatatype(String name) { return null; }
    public DatatypeBuilder createDatatypeBuilder(String name) { return null; }
    public static void main(String[] args) {
        ClassLoader parent = CheckLoader.class.getClassLoader();
        Thread.currentThread().setContextClassLoader(new ClassLoader(parent) {
            @Override public Enumeration<URL> getResources(String name) {
                return Collections.emptyEnumeration();
            }
        });
        DatatypeLibraryLoader loader = new DatatypeLibraryLoader();
        if (!(loader.createDatatypeLibrary("urn:test") instanceof CheckLoader))
            throw new AssertionError("Service resource was not loaded");
        if (loader.createDatatypeLibrary("urn:unknown") != null)
            throw new AssertionError("Unknown library was accepted");
    }
}
JAVA
echo CheckLoader > tests/META-INF/services/org.relaxng.datatype.DatatypeLibraryFactory
javac --release 8 -cp relaxngDatatype.jar tests/CheckLoader.java
java -cp tests:relaxngDatatype.jar CheckLoader

%files
%license copying.txt
%doc README.txt
%{_datadir}/java/relaxngDatatype.jar

%changelog
%autochangelog
