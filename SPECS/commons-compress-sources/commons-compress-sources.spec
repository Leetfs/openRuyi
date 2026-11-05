# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global artifact_dir %{_datadir}/maven-repository/org/apache/commons/commons-compress/%{version}

Name:           commons-compress-sources
Version:        1.28.0
Release:        %autorelease
Summary:        Original Java source attachment for Apache Commons Compress
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-compress/
VCS:            git:https://github.com/apache/commons-compress
#!RemoteAsset:  sha256:6de9de4559f12bba6d41789c72f6a2a424514f2d2a3f7f49e2a3c52414db9632
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-compress/%{version}/commons-compress-%{version}-sources.jar
BuildArch:      noarch
BuildRequires:  unzip
Provides:       mvn(org.apache.commons:commons-compress:jar:sources) == %{version}

%description
This package provides the original Commons Compress Java source attachment.
Tycho's p2 director plugin includes this source artifact in its dependencies.

%prep
%setup -q -T -c
unzip -p %{SOURCE0} META-INF/LICENSE.txt > LICENSE.txt
unzip -p %{SOURCE0} META-INF/NOTICE.txt > NOTICE.txt

%install
install -Dm644 %{SOURCE0} %{buildroot}%{artifact_dir}/commons-compress-%{version}-sources.jar
mkdir -p %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.commons</groupId><artifactId>commons-compress</artifactId><version>%{version}</version><extension>jar</extension><classifier>sources</classifier><path>%{artifact_dir}/commons-compress-%{version}-sources.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Verify the installed source archive is complete and contains the public archive API.
cmp %{SOURCE0} %{buildroot}%{artifact_dir}/commons-compress-%{version}-sources.jar
unzip -t %{buildroot}%{artifact_dir}/commons-compress-%{version}-sources.jar
unzip -p %{SOURCE0} org/apache/commons/compress/archivers/ArchiveStreamFactory.java | grep -Fx 'package org.apache.commons.compress.archivers;'

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/commons-compress-sources.xml
%{artifact_dir}/commons-compress-%{version}-sources.jar

%changelog
%autochangelog
