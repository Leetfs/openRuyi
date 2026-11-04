# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 85965b70101a8022ea1ee3f1bf1dc65bd99220b8
%global repo_dir %{_datadir}/maven-repository
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-ecf
Version:        3.13.0
Release:        %autorelease
Summary:        Eclipse Communication Framework identities and file transfer
License:        EPL-2.0 AND EPL-1.0
URL:            https://eclipse.dev/ecf/
VCS:            git:https://github.com/eclipse-ecf/ecf
#!RemoteAsset:  sha256:dddd30a8febd5a4a5373f26a4fba2a2899171defec4ad57f633b3f8085a0f801
Source0:        https://github.com/eclipse-ecf/ecf/archive/%{commit}.tar.gz?/ecf-%{commit}.tar.gz
#!RemoteAsset:  sha256:bdcfa3e78d93428ed824696e389e2cbf624ea824b5c3a4bedcd82012d9ee28df
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ecf/org.eclipse.ecf.identity/3.10.0/org.eclipse.ecf.identity-3.10.0.pom
#!RemoteAsset:  sha256:03fdde485014d5e191ad44c997451128f65edd63cdc722309fca29b6e1a33d6c
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ecf/org.eclipse.ecf/3.13.0/org.eclipse.ecf-3.13.0.pom
#!RemoteAsset:  sha256:fafc82b1cd65b7cab7d3d556bfa6de4a94de6ba20663e92bfbb3b84f3a8e8bd0
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ecf/org.eclipse.ecf.filetransfer/5.1.103/org.eclipse.ecf.filetransfer-5.1.103.pom
#!RemoteAsset:  sha256:b57029dba6ffb72c9216170750d32b713ed250a216a65de8bdc938c0b5cc715d
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ecf/org.eclipse.ecf.provider.filetransfer/3.3.100/org.eclipse.ecf.provider.filetransfer-3.3.100.pom
#!RemoteAsset:  sha256:42a0274fc728a02dda34bf6d48abc33a5ddbf77381677f0b13acf949333117e8
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ecf/ecf-parent/1.0.0/ecf-parent-1.0.0.pom
#!RemoteAsset:  sha256:0becf16567beb77fa252b7664631dd177c8f9a1889e48995b45379c7130e5303
Source6:        https://raw.githubusercontent.com/eclipse-equinox/p2/d5bb33c77711e7b8ddffd4097bf7631228083a07/LICENSE
Source7:        check-identity.sh
Source8:        IdentityApplication.java
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(parent-models)
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.net) == 1.5.800
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.concurrent) == 1.3.400
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.launcher) == 1.7.100
Provides:       mvn(org.eclipse.ecf:org.eclipse.ecf.identity) == 3.10.0
Provides:       mvn(org.eclipse.ecf:org.eclipse.ecf) == 3.13.0
Provides:       mvn(org.eclipse.ecf:org.eclipse.ecf.filetransfer) == 5.1.103
Provides:       mvn(org.eclipse.ecf:org.eclipse.ecf.provider.filetransfer) == 3.3.100
Provides:       mvn(org.eclipse.ecf:ecf-parent:pom:) == 1.0.0
Requires:       eclipse-core-net >= 4.39
Requires:       eclipse-core-runtime >= 4.39
Requires:       eclipse-equinox-services >= 4.39

%description
ECF creates communication containers, assigns identities to remote objects,
and transfers files. Its provider supplies the file transfer services used by
Eclipse p2 to retrieve and install artifacts.

%prep
%autosetup -n ecf-%{commit}
cp %{SOURCE6} EPL-2.0.txt
cp incubation/projects/org.eclipse.ecf.ipc/bundles/org.eclipse.ecf.ipc.library/misc/epl-v10.html EPL-1.0.html

%build
mkdir -p build/bundles
cp=$(rpm -ql eclipse-equinox eclipse-equinox-services eclipse-core-jobs eclipse-core-runtime eclipse-core-net jna |
    sed -n '/^\/usr\/share\/maven-repository\/.*[.]jar$/ { /-sources[.]jar$/!p; }' | sort -u | paste -sd:)
cp="$cp:%{_datadir}/java/javapackages-bootstrap/osgi.cmpn.jar:%{_datadir}/java/javapackages-bootstrap/osgi.annotation.jar"
for name in org.eclipse.ecf.identity org.eclipse.ecf org.eclipse.ecf.filetransfer org.eclipse.ecf.provider.filetransfer; do
    dir=framework/bundles/$name
    if test "$name" = org.eclipse.ecf.provider.filetransfer; then dir=providers/bundles/$name; fi
    release=17
    if test "$name" = org.eclipse.ecf.filetransfer; then release=8; fi
    %{bundle_tools}/build-bundle "$dir" "build/bundles/$name.jar" --release "$release" --classpath "$cp"
    cp="$cp:$PWD/build/bundles/$name.jar"
done

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-parent %{SOURCE5}
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}

%check
# Run the released identity suites inside Equinox, including registration and lookup of ID namespaces.
bash %{SOURCE7} %{SOURCE8}
# The R7 logging stub is only used when compiling against older OSGi APIs.
jar tf build/bundles/org.eclipse.ecf.identity.jar > build/identity-contents
if grep -E '(^r7stubs[.]jar$|org/osgi/service/log/Logger[.]class$)' build/identity-contents; then exit 1; fi

%files
%license EPL-1.0.html EPL-2.0.txt
%doc README.md
%{_datadir}/maven-metadata/eclipse-ecf.xml
%{_datadir}/maven-metadata/eclipse-ecf-parent.xml
%{repo_dir}/org/eclipse/ecf/

%changelog
%autochangelog
