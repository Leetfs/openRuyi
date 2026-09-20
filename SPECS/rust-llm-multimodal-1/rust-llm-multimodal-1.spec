# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global git_commit 15adba5e025d8636ba4a334fb379b1371f6196a1
%global crate_name llm-multimodal
%global full_version 1.7.1
%global pkgname llm-multimodal-1

Name:           rust-llm-multimodal-1
Version:        1.7.1
Release:        %autorelease
Summary:        Rust crate "llm-multimodal"
License:        Apache-2.0
URL:            https://github.com/vllm-project/llm-multimodal
#!RemoteAsset:  sha256:5054aefa538b7f0ddc4cd839a27d60b5b25fa2aa104aa6efac7053158408cf56
Source:         https://github.com/smg-project/llm-multimodal/archive/%{git_commit}.tar.gz#/%{crate_name}-%{git_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates
BuildOption(prep):  -n llm-multimodal-15adba5e025d8636ba4a334fb379b1371f6196a1

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(blake3-1/default) >= 1.8.5
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(bytes-1/serde) >= 1.12.0
Requires:       crate(cc-1) >= 1.2.56
Requires:       crate(fast-image-resize-6/default) >= 6.0.0
Requires:       crate(fast-image-resize-6/image) >= 6.0.0
Requires:       crate(image-0.25/bmp) >= 0.25.10
Requires:       crate(image-0.25/gif) >= 0.25.10
Requires:       crate(image-0.25/ico) >= 0.25.10
Requires:       crate(image-0.25/jpeg) >= 0.25.10
Requires:       crate(image-0.25/png) >= 0.25.10
Requires:       crate(image-0.25/tiff) >= 0.25.10
Requires:       crate(image-0.25/webp) >= 0.25.10
Requires:       crate(libloading-0.8/default) >= 0.8.9
Requires:       crate(ndarray-0.17/default) >= 0.17.2
Requires:       crate(once-cell-1/default) >= 1.21.4
Requires:       crate(pkg-config-0.3) >= 0.3.32
Requires:       crate(rayon-1/default) >= 1.12.0
Requires:       crate(realfft-3/default) >= 3.5.0
Requires:       crate(reqwest-0.13/stream) >= 0.13.4
Requires:       crate(rustfft-6/default) >= 6.4.1
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(serde-json-1/preserve-order) >= 1.0.149
Requires:       crate(serde-with-3/default) >= 3.18.0
Requires:       crate(symphonia-0.6/all) >= 0.6.0
Requires:       crate(tempfile-3/default) >= 3.27.0
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/fs) >= 1.52.3
Requires:       crate(tokio-1/io-util) >= 1.52.3
Requires:       crate(tokio-1/process) >= 1.52.3
Requires:       crate(tokio-1/rt-multi-thread) >= 1.52.3
Requires:       crate(tokio-1/sync) >= 1.52.3
Requires:       crate(tokio-1/time) >= 1.52.3
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(url-2/default) >= 2.5.8

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "llm-multimodal"

%package     -n %{name}+default
Summary:        Multimodal processing for vision and other modalities - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hf-hub) = %{version}
Requires:       crate(%{pkgname}/rustls-tls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust llm-multimodal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hf-hub
Summary:        Multimodal processing for vision and other modalities - feature "hf-hub"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hf-hub-0.5/tokio) >= 0.5.0
Provides:       crate(%{pkgname}/hf-hub) = %{version}

%description -n %{name}+hf-hub
This metapackage enables feature "hf-hub" for the Rust llm-multimodal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Multimodal processing for vision and other modalities - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hf-hub-0.5/native-tls) >= 0.5.0
Requires:       crate(hf-hub-0.5/tokio) >= 0.5.0
Requires:       crate(reqwest-0.13/native-tls) >= 0.13.4
Requires:       crate(reqwest-0.13/stream) >= 0.13.4
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust llm-multimodal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opencv-video
Summary:        Multimodal processing for vision and other modalities - feature "opencv-video"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(opencv-0.99/clang-runtime) >= 0.99.0
Requires:       crate(opencv-0.99/imgproc) >= 0.99.0
Requires:       crate(opencv-0.99/videoio) >= 0.99.0
Provides:       crate(%{pkgname}/opencv-video) = %{version}

%description -n %{name}+opencv-video
This metapackage enables feature "opencv-video" for the Rust llm-multimodal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls
Summary:        Multimodal processing for vision and other modalities - feature "rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hf-hub-0.5/rustls-tls) >= 0.5.0
Requires:       crate(hf-hub-0.5/tokio) >= 0.5.0
Requires:       crate(reqwest-0.13/rustls) >= 0.13.4
Requires:       crate(reqwest-0.13/stream) >= 0.13.4
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust llm-multimodal crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
