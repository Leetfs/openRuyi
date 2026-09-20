# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hf-hub
%global full_version 0.5.0
%global pkgname hf-hub-0.5

Name:           rust-hf-hub-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "hf-hub"
License:        Apache-2.0
URL:            https://github.com/huggingface/hf-hub
#!RemoteAsset:  sha256:aef3982638978efa195ff11b305f51f1f22f4f0a6cabee7af79b383ebee6a213
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-6/default) >= 6.0.0
Requires:       crate(log-0.4/default) >= 0.4.29

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "hf-hub"

%package     -n %{name}+default
Summary:        This crates aims ease the interaction with huggingface It aims to be compatible with the huggingface_hub python package, but only implements a smaller subset of functions - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/default-tls) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/ureq) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        This crates aims ease the interaction with huggingface It aims to be compatible with the huggingface_hub python package, but only implements a smaller subset of functions - feature "native-tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.18
Requires:       crate(reqwest-0.12/default) >= 0.12.28
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(ureq-3/default) >= 3.3.0
Requires:       crate(ureq-3/json) >= 3.3.0
Requires:       crate(ureq-3/native-tls) >= 3.3.0
Requires:       crate(ureq-3/socks-proxy) >= 3.3.0
Provides:       crate(%{pkgname}/default-tls) = %{version}
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-tls" feature.

%package     -n %{name}+rustls-tls
Summary:        This crates aims ease the interaction with huggingface It aims to be compatible with the huggingface_hub python package, but only implements a smaller subset of functions - feature "rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/rustls-tls) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        This crates aims ease the interaction with huggingface It aims to be compatible with the huggingface_hub python package, but only implements a smaller subset of functions - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.32
Requires:       crate(indicatif-0.18/default) >= 0.18.4
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(num-cpus-1/default) >= 1.17.0
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(reqwest-0.12/charset) >= 0.12.28
Requires:       crate(reqwest-0.12/http2) >= 0.12.28
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/fs) >= 1.52.3
Requires:       crate(tokio-1/macros) >= 1.52.3
Requires:       crate(tokio-1/rt-multi-thread) >= 1.52.3
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ureq
Summary:        This crates aims ease the interaction with huggingface It aims to be compatible with the huggingface_hub python package, but only implements a smaller subset of functions - feature "ureq"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(indicatif-0.18/default) >= 0.18.4
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(ureq-3/default) >= 3.3.0
Requires:       crate(ureq-3/json) >= 3.3.0
Requires:       crate(ureq-3/socks-proxy) >= 3.3.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Provides:       crate(%{pkgname}/ureq) = %{version}

%description -n %{name}+ureq
This metapackage enables feature "ureq" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
