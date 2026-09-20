# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name opencv
%global full_version 0.99.1
%global pkgname opencv-0.99

Name:           rust-opencv-0.99
Version:        0.99.1
Release:        %autorelease
Summary:        Rust crate "opencv"
License:        MIT
URL:            https://github.com/twistedfall/opencv-rust
#!RemoteAsset:  sha256:4da218a3f75062a3980b33f8e31545d3bde91f935cae18b80c0617c0f3a59a65
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.83
Requires:       crate(cc-1/parallel) >= 1.0.83
Requires:       crate(dunce-1) >= 1.0.0
Requires:       crate(jobserver-0.1) >= 0.1.25
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(opencv-binding-generator-0.103) >= 0.103.0
Requires:       crate(pkg-config-0.3) >= 0.3.0
Requires:       crate(semver-1) >= 1.0.0
Requires:       crate(shlex-2) >= 2.0.0
Requires:       crate(vcpkg-0.2) >= 0.2.9
Requires:       crate(windows-0.62/default) >= 0.62.0
Requires:       crate(windows-0.62/win32-graphics-direct3d10) >= 0.62.0
Requires:       crate(windows-0.62/win32-graphics-direct3d11) >= 0.62.0
Requires:       crate(windows-0.62/win32-graphics-direct3d9) >= 0.62.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alphamat) = %{version}
Provides:       crate(%{pkgname}/aruco) = %{version}
Provides:       crate(%{pkgname}/aruco-detector) = %{version}
Provides:       crate(%{pkgname}/barcode) = %{version}
Provides:       crate(%{pkgname}/bgsegm) = %{version}
Provides:       crate(%{pkgname}/bioinspired) = %{version}
Provides:       crate(%{pkgname}/calib) = %{version}
Provides:       crate(%{pkgname}/calib3d) = %{version}
Provides:       crate(%{pkgname}/ccalib) = %{version}
Provides:       crate(%{pkgname}/cudaarithm) = %{version}
Provides:       crate(%{pkgname}/cudabgsegm) = %{version}
Provides:       crate(%{pkgname}/cudacodec) = %{version}
Provides:       crate(%{pkgname}/cudafeatures2d) = %{version}
Provides:       crate(%{pkgname}/cudafilters) = %{version}
Provides:       crate(%{pkgname}/cudaimgproc) = %{version}
Provides:       crate(%{pkgname}/cudalegacy) = %{version}
Provides:       crate(%{pkgname}/cudaobjdetect) = %{version}
Provides:       crate(%{pkgname}/cudaoptflow) = %{version}
Provides:       crate(%{pkgname}/cudastereo) = %{version}
Provides:       crate(%{pkgname}/cudawarping) = %{version}
Provides:       crate(%{pkgname}/cvv) = %{version}
Provides:       crate(%{pkgname}/dnn) = %{version}
Provides:       crate(%{pkgname}/dnn-superres) = %{version}
Provides:       crate(%{pkgname}/dpm) = %{version}
Provides:       crate(%{pkgname}/face) = %{version}
Provides:       crate(%{pkgname}/features) = %{version}
Provides:       crate(%{pkgname}/features2d) = %{version}
Provides:       crate(%{pkgname}/flann) = %{version}
Provides:       crate(%{pkgname}/freetype) = %{version}
Provides:       crate(%{pkgname}/fuzzy) = %{version}
Provides:       crate(%{pkgname}/gapi) = %{version}
Provides:       crate(%{pkgname}/geometry) = %{version}
Provides:       crate(%{pkgname}/hdf) = %{version}
Provides:       crate(%{pkgname}/hfs) = %{version}
Provides:       crate(%{pkgname}/highgui) = %{version}
Provides:       crate(%{pkgname}/img-hash) = %{version}
Provides:       crate(%{pkgname}/imgcodecs) = %{version}
Provides:       crate(%{pkgname}/imgproc) = %{version}
Provides:       crate(%{pkgname}/intensity-transform) = %{version}
Provides:       crate(%{pkgname}/line-descriptor) = %{version}
Provides:       crate(%{pkgname}/mcc) = %{version}
Provides:       crate(%{pkgname}/ml) = %{version}
Provides:       crate(%{pkgname}/objdetect) = %{version}
Provides:       crate(%{pkgname}/optflow) = %{version}
Provides:       crate(%{pkgname}/ovis) = %{version}
Provides:       crate(%{pkgname}/phase-unwrapping) = %{version}
Provides:       crate(%{pkgname}/photo) = %{version}
Provides:       crate(%{pkgname}/plot) = %{version}
Provides:       crate(%{pkgname}/ptcloud) = %{version}
Provides:       crate(%{pkgname}/quality) = %{version}
Provides:       crate(%{pkgname}/rapid) = %{version}
Provides:       crate(%{pkgname}/rgbd) = %{version}
Provides:       crate(%{pkgname}/saliency) = %{version}
Provides:       crate(%{pkgname}/sfm) = %{version}
Provides:       crate(%{pkgname}/shape) = %{version}
Provides:       crate(%{pkgname}/signal) = %{version}
Provides:       crate(%{pkgname}/stereo) = %{version}
Provides:       crate(%{pkgname}/structured-light) = %{version}
Provides:       crate(%{pkgname}/superres) = %{version}
Provides:       crate(%{pkgname}/surface-matching) = %{version}
Provides:       crate(%{pkgname}/text) = %{version}
Provides:       crate(%{pkgname}/tracking) = %{version}
Provides:       crate(%{pkgname}/video) = %{version}
Provides:       crate(%{pkgname}/videoio) = %{version}
Provides:       crate(%{pkgname}/videostab) = %{version}
Provides:       crate(%{pkgname}/viz) = %{version}
Provides:       crate(%{pkgname}/wechat-qrcode) = %{version}
Provides:       crate(%{pkgname}/xfeatures2d) = %{version}
Provides:       crate(%{pkgname}/ximgproc) = %{version}
Provides:       crate(%{pkgname}/xobjdetect) = %{version}
Provides:       crate(%{pkgname}/xphoto) = %{version}
Provides:       crate(%{pkgname}/xstereo) = %{version}

%description
Source code for takopackized Rust crate "opencv"

%package     -n %{name}+clang-runtime
Summary:        Rust bindings for OpenCV - feature "clang-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(opencv-binding-generator-0.103) >= 0.103.0
Requires:       crate(opencv-binding-generator-0.103/clang-runtime) >= 0.103.0
Provides:       crate(%{pkgname}/clang-runtime) = %{version}

%description -n %{name}+clang-runtime
This metapackage enables feature "clang-runtime" for the Rust opencv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust bindings for OpenCV - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alphamat) = %{version}
Requires:       crate(%{pkgname}/aruco) = %{version}
Requires:       crate(%{pkgname}/aruco-detector) = %{version}
Requires:       crate(%{pkgname}/barcode) = %{version}
Requires:       crate(%{pkgname}/bgsegm) = %{version}
Requires:       crate(%{pkgname}/bioinspired) = %{version}
Requires:       crate(%{pkgname}/calib) = %{version}
Requires:       crate(%{pkgname}/calib3d) = %{version}
Requires:       crate(%{pkgname}/ccalib) = %{version}
Requires:       crate(%{pkgname}/cudaarithm) = %{version}
Requires:       crate(%{pkgname}/cudabgsegm) = %{version}
Requires:       crate(%{pkgname}/cudacodec) = %{version}
Requires:       crate(%{pkgname}/cudafeatures2d) = %{version}
Requires:       crate(%{pkgname}/cudafilters) = %{version}
Requires:       crate(%{pkgname}/cudaimgproc) = %{version}
Requires:       crate(%{pkgname}/cudalegacy) = %{version}
Requires:       crate(%{pkgname}/cudaobjdetect) = %{version}
Requires:       crate(%{pkgname}/cudaoptflow) = %{version}
Requires:       crate(%{pkgname}/cudastereo) = %{version}
Requires:       crate(%{pkgname}/cudawarping) = %{version}
Requires:       crate(%{pkgname}/cvv) = %{version}
Requires:       crate(%{pkgname}/dnn) = %{version}
Requires:       crate(%{pkgname}/dnn-superres) = %{version}
Requires:       crate(%{pkgname}/dpm) = %{version}
Requires:       crate(%{pkgname}/face) = %{version}
Requires:       crate(%{pkgname}/features) = %{version}
Requires:       crate(%{pkgname}/features2d) = %{version}
Requires:       crate(%{pkgname}/flann) = %{version}
Requires:       crate(%{pkgname}/freetype) = %{version}
Requires:       crate(%{pkgname}/fuzzy) = %{version}
Requires:       crate(%{pkgname}/gapi) = %{version}
Requires:       crate(%{pkgname}/geometry) = %{version}
Requires:       crate(%{pkgname}/hdf) = %{version}
Requires:       crate(%{pkgname}/hfs) = %{version}
Requires:       crate(%{pkgname}/highgui) = %{version}
Requires:       crate(%{pkgname}/img-hash) = %{version}
Requires:       crate(%{pkgname}/imgcodecs) = %{version}
Requires:       crate(%{pkgname}/imgproc) = %{version}
Requires:       crate(%{pkgname}/intensity-transform) = %{version}
Requires:       crate(%{pkgname}/line-descriptor) = %{version}
Requires:       crate(%{pkgname}/mcc) = %{version}
Requires:       crate(%{pkgname}/ml) = %{version}
Requires:       crate(%{pkgname}/objdetect) = %{version}
Requires:       crate(%{pkgname}/optflow) = %{version}
Requires:       crate(%{pkgname}/ovis) = %{version}
Requires:       crate(%{pkgname}/phase-unwrapping) = %{version}
Requires:       crate(%{pkgname}/photo) = %{version}
Requires:       crate(%{pkgname}/plot) = %{version}
Requires:       crate(%{pkgname}/ptcloud) = %{version}
Requires:       crate(%{pkgname}/quality) = %{version}
Requires:       crate(%{pkgname}/rapid) = %{version}
Requires:       crate(%{pkgname}/rgbd) = %{version}
Requires:       crate(%{pkgname}/saliency) = %{version}
Requires:       crate(%{pkgname}/sfm) = %{version}
Requires:       crate(%{pkgname}/shape) = %{version}
Requires:       crate(%{pkgname}/signal) = %{version}
Requires:       crate(%{pkgname}/stereo) = %{version}
Requires:       crate(%{pkgname}/stitching) = %{version}
Requires:       crate(%{pkgname}/structured-light) = %{version}
Requires:       crate(%{pkgname}/superres) = %{version}
Requires:       crate(%{pkgname}/surface-matching) = %{version}
Requires:       crate(%{pkgname}/text) = %{version}
Requires:       crate(%{pkgname}/tracking) = %{version}
Requires:       crate(%{pkgname}/video) = %{version}
Requires:       crate(%{pkgname}/videoio) = %{version}
Requires:       crate(%{pkgname}/videostab) = %{version}
Requires:       crate(%{pkgname}/viz) = %{version}
Requires:       crate(%{pkgname}/wechat-qrcode) = %{version}
Requires:       crate(%{pkgname}/xfeatures2d) = %{version}
Requires:       crate(%{pkgname}/ximgproc) = %{version}
Requires:       crate(%{pkgname}/xobjdetect) = %{version}
Requires:       crate(%{pkgname}/xphoto) = %{version}
Requires:       crate(%{pkgname}/xstereo) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust opencv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f16
Summary:        Rust bindings for OpenCV - feature "f16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(half-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/f16) = %{version}

%description -n %{name}+f16
This metapackage enables feature "f16" for the Rust opencv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rgb
Summary:        Rust bindings for OpenCV - feature "rgb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rgb-0.8/argb) >= 0.8.20
Provides:       crate(%{pkgname}/rgb) = %{version}

%description -n %{name}+rgb
This metapackage enables feature "rgb" for the Rust opencv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stitching
Summary:        Rust bindings for OpenCV - feature "stitching"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/features2d) = %{version}
Requires:       crate(%{pkgname}/imgproc) = %{version}
Provides:       crate(%{pkgname}/stitching) = %{version}

%description -n %{name}+stitching
This metapackage enables feature "stitching" for the Rust opencv crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
