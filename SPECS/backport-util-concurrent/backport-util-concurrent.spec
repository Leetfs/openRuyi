# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           backport-util-concurrent
Version:        3.1
Release:        %autorelease
Summary:        Concurrency primitives for the Emory Java backport
License:        CC-PDDC
URL:            https://backport-jsr166.sourceforge.net/
# VCS: No VCS link available
#!RemoteAsset:  sha256:2e6ea2678e1efb8f0b3b149f35d10ae7454c46527a4dc1c84f6f3ababa38e4cd
Source0:        https://downloads.sourceforge.net/project/backport-jsr166/backport-jsr166/%{version}/%{name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
The Emory backport provides the JSR-166 concurrency API in the namespace
used by older Java applications.

%prep
%autosetup -n %{name}-%{version}-src

%build
mkdir classes
find src/edu src/sun -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
# The sun.misc sources are compile-time stubs. Use the JDK's own classes at runtime.
jar --create --file backport-util-concurrent.jar -C classes edu

%install
install -Dpm644 backport-util-concurrent.jar %{buildroot}%{_datadir}/java/backport-util-concurrent.jar

%check
# Exercise the concurrency namespace used by Ehcache and verify the queue handoff.
cat > QueueTest.java <<'JAVA'
import edu.emory.mathcs.backport.java.util.concurrent.ArrayBlockingQueue;
class QueueTest {
    public static void main(String[] args) throws Exception {
        ArrayBlockingQueue queue = new ArrayBlockingQueue(1);
        Thread producer = new Thread(() -> { try { queue.put("report"); }
            catch (InterruptedException e) { throw new AssertionError(e); } });
        producer.start();
        if (!"report".equals(queue.take())) throw new AssertionError("Queue handoff");
        producer.join();
    }
}
JAVA
javac -cp backport-util-concurrent.jar QueueTest.java
java -cp .:backport-util-concurrent.jar QueueTest

%files
%license license.html
%{_datadir}/java/backport-util-concurrent.jar

%changelog
%autochangelog
