# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-noto-sans-hebrew-testdata
Version:        3.001
Release:        %autorelease
Summary:        Noto Sans Hebrew reference face for layout regression tests
License:        OFL-1.1
URL:            https://github.com/notofonts/hebrew
#!RemoteAsset:  sha256:df0a71814b4e63644cf40fcc4529111b61266b7a2dafbe95068b29a7520cc3cb
Source0:        https://github.com/notofonts/hebrew/releases/download/NotoSansHebrew-v%{version}/NotoSansHebrew-v%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip

%description
This versioned regular face supplies reproducible Hebrew metrics and glyphs
for document layout and PDF regression tests. It is installed as test data.

%prep
%setup -q -c -T
# Read only the two named ZIP members, including the original license.
unzip -p %{SOURCE0} 'OFL.txt' > OFL.txt
unzip -p %{SOURCE0} 'NotoSansHebrew/full/ttf/NotoSansHebrew-Regular.ttf' > NotoSansHebrew-Regular.ttf

%install
install -Dpm644 NotoSansHebrew-Regular.ttf %{buildroot}%{_datadir}/openruyi-test-fonts/NotoSansHebrew-Regular.ttf

%check
# Verify the precise reference face consumed by the layout tests.
printf '%%s  %%s\n' '671951828bd5c95db818e5bb12dcea2d0c0dda00311888522be061ee6835125e' 'NotoSansHebrew-Regular.ttf' | sha256sum -c -

%files
%license OFL.txt
%dir %{_datadir}/openruyi-test-fonts/
%{_datadir}/openruyi-test-fonts/NotoSansHebrew-Regular.ttf

%changelog
%autochangelog
