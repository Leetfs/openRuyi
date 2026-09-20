# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rubato
%global full_version 0.16.2
%global pkgname rubato-0.16

Name:           rust-rubato-0.16
Version:        0.16.2
Release:        %autorelease
Summary:        Rust crate "rubato"
License:        MIT
URL:            https://github.com/HEnquist/rubato
#!RemoteAsset:  sha256:5258099699851cfd0082aeb645feb9c084d9a5e1f1b8d5372086b989fc5e56a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/default) >= 0.1.46
Requires:       crate(num-traits-0.2/default) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rubato"

%package     -n %{name}+fft-resampler
Summary:        Asynchronous resampling library intended for audio data - feature "fft_resampler" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-complex) = %{version}
Requires:       crate(%{pkgname}/realfft) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fft-resampler) = %{version}

%description -n %{name}+fft-resampler
This metapackage enables feature "fft_resampler" for the Rust rubato crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+log
Summary:        Asynchronous resampling library intended for audio data - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.18
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rubato crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-complex
Summary:        Asynchronous resampling library intended for audio data - feature "num-complex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-complex-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/num-complex) = %{version}

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust rubato crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+realfft
Summary:        Asynchronous resampling library intended for audio data - feature "realfft"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(realfft-3/default) >= 3.5.0
Provides:       crate(%{pkgname}/realfft) = %{version}

%description -n %{name}+realfft
This metapackage enables feature "realfft" for the Rust rubato crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
