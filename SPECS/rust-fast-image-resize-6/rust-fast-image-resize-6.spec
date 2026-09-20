# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fast_image_resize
%global full_version 6.0.0
%global pkgname fast-image-resize-6

Name:           rust-fast-image-resize-6
Version:        6.0.0
Release:        %autorelease
Summary:        Rust crate "fast_image_resize"
License:        MIT OR Apache-2.0
URL:            https://github.com/cykooz/fast_image_resize
#!RemoteAsset:  sha256:12dd43e5011e8d8411a3215a0d57a2ec5c68282fb90eb5d7221fab0113442174
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.4
Requires:       crate(num-traits-0.2) >= 0.2.19
Requires:       crate(thiserror-2) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/only-u8x4) = %{version}

%description
Source code for takopackized Rust crate "fast_image_resize"

%package     -n %{name}+bytemuck
Summary:        Fast image resizing with using of SIMD instructions - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.25.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust fast_image_resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+for-testing
Summary:        Fast image resizing with using of SIMD instructions - feature "for_testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytemuck) = %{version}
Requires:       crate(%{pkgname}/image) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(image-0.25/png) >= 0.25.10
Provides:       crate(%{pkgname}/for-testing) = %{version}

%description -n %{name}+for-testing
This metapackage enables feature "for_testing" for the Rust fast_image_resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Fast image resizing with using of SIMD instructions - feature "image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.25.0
Requires:       crate(image-0.25) >= 0.25.10
Provides:       crate(%{pkgname}/image) = %{version}

%description -n %{name}+image
This metapackage enables feature "image" for the Rust fast_image_resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std
Summary:        Fast image resizing with using of SIMD instructions - feature "no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cpufeatures-0.2/default) >= 0.2.17
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust fast_image_resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Fast image resizing with using of SIMD instructions - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(image-0.25/rayon) >= 0.25.10
Requires:       crate(rayon-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust fast_image_resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast image resizing with using of SIMD instructions - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.12
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(thiserror-2/std) >= 2.0.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust fast_image_resize crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
