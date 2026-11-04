# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-noto-sans-arabic-testdata
Version:        2.010
Release:        %autorelease
Summary:        Noto Sans Arabic reference face for layout regression tests
License:        OFL-1.1
URL:            https://github.com/notofonts/arabic
#!RemoteAsset:  sha256:a5a34ac1ea01d0d71c083f99440ebfb1f64224474a0d88bb7ef0e2f8d9a996d2
Source0:        https://github.com/notofonts/arabic/releases/download/NotoSansArabic-v%{version}/NotoSansArabic-v%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip

%description
This versioned regular face supplies reproducible Arabic metrics and glyphs
for document layout and PDF regression tests. It is installed as test data.

%prep
%setup -q -c -T
# Read only the two named ZIP members, including the original license.
unzip -p %{SOURCE0} '../OFL.txt' > OFL.txt
unzip -p %{SOURCE0} 'NotoSansArabic/hinted/ttf/NotoSansArabic-Regular.ttf' > NotoSansArabic-Regular.ttf

%install
install -Dpm644 NotoSansArabic-Regular.ttf %{buildroot}%{_datadir}/openruyi-test-fonts/NotoSansArabic-Regular.ttf

%check
# Verify the precise reference face consumed by the layout tests.
printf '%%s  %%s\n' 'd6efa4c9fac8ecefd2de19676acc3a396ba7aee99ba7a2d513950246841b6725' 'NotoSansArabic-Regular.ttf' | sha256sum -c -

%files
%license OFL.txt
%dir %{_datadir}/openruyi-test-fonts/
%{_datadir}/openruyi-test-fonts/NotoSansArabic-Regular.ttf

%changelog
%autochangelog
