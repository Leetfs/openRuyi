# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aopalliance
Version:        1.0
Release:        %autorelease
Summary:        Java API for method and constructor interception
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://aopalliance.sourceforge.net/
VCS:            cvs:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance
# The public release ZIP contains bytecode and Javadoc. The release sources carry the interception_1_0 CVS tag.
#!RemoteAsset:  sha256:fb31304f733f6eaa46053b4189654f6b05072fb0f7d101637b88c283c5ff5a01
Source0:        https://sourceforge.net/code-snapshots/cvs/a/ao/aopalliance.zip#/%{name}-cvs.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  python3

%description
The AOP Alliance API lets Java frameworks implement and share method and
constructor interceptors. It describes interception points and the
invocation chain passed to each interceptor.

%prep
%setup -q -T -c
python3 - %{SOURCE0} <<'PYTHON'
import re
import sys
from pathlib import Path
from zipfile import ZipFile

def head_text(rcs):
    match = re.search(rb'\ntext\n@((?:[^@]|@@)*)@', rcs)
    return match[1].replace(b'@@', b'@')

prefix = 'aopalliance/aopalliance/src/main/'
with ZipFile(sys.argv[1]) as archive:
    for name in archive.namelist():
        if not name.startswith(prefix) or not name.endswith('.java,v'):
            continue
        source = archive.read(name)
        tag = re.search(rb'\binterception_1_0:([\d.]+)', source)
        if tag is None:
            continue
        assert tag[1] == re.match(rb'head\s+([\d.]+);', source)[1]
        path = Path('src') / name[len(prefix):-2]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(head_text(source))
    terms = head_text(archive.read('aopalliance/www/index.html,v'))
    assert b'all the source code provided by AOP Alliance is <b>Public Domain</b>' in terms
    Path('licensing.html').write_bytes(terms)
PYTHON

%build
mkdir classes
find src -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
jar --create --file aopalliance.jar -C classes .

%install
install -Dpm644 aopalliance.jar %{buildroot}%{_datadir}/java/aopalliance.jar

%check
cat > Intercept.java <<'JAVA'
import java.lang.reflect.*;
import org.aopalliance.intercept.*;
class Intercept {
    public int value() { return 41; }
    public static void main(String[] args) throws Throwable {
        Intercept target = new Intercept();
        Method method = Intercept.class.getMethod("value");
        MethodInvocation call = new MethodInvocation() {
            public Method getMethod() { return method; }
            public Object[] getArguments() { return new Object[0]; }
            public Object proceed() throws Throwable { return method.invoke(target); }
            public Object getThis() { return target; }
            public AccessibleObject getStaticPart() { return method; }
        };
        MethodInterceptor intercept = invocation -> (Integer) invocation.proceed() + 1;
        if (!intercept.invoke(call).equals(42)) throw new AssertionError("Interception");
    }
}
JAVA
javac --release 8 -cp aopalliance.jar Intercept.java
java -cp .:aopalliance.jar Intercept

%files
%license licensing.html
%{_datadir}/java/aopalliance.jar

%changelog
%autochangelog
