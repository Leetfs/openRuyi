# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hf-hub
%global full_version 0.4.3
%global pkgname hf-hub-0.4

Name:           rust-hf-hub-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "hf-hub"
License:        Apache-2.0
URL:            https://github.com/huggingface/hf-hub
#!RemoteAsset:  sha256:629d8f3bbeda9d148036d6b0de0a3ab947abd08ce90626327fc3547a49d59d97
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-6/default) >= 6.0.0
Requires:       crate(log-0.4/default) >= 0.4.19

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "hf-hub"

%package     -n %{name}+default
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/default-tls) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/ureq) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "native-tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(native-tls-0.2/default) >= 0.2.12
Requires:       crate(reqwest-0.12/default) >= 0.12.2
Requires:       crate(reqwest-0.12/json) >= 0.12.2
Requires:       crate(reqwest-0.12/stream) >= 0.12.2
Requires:       crate(ureq-2/default) >= 2.0.0
Requires:       crate(ureq-2/json) >= 2.0.0
Requires:       crate(ureq-2/native-tls) >= 2.0.0
Requires:       crate(ureq-2/socks-proxy) >= 2.0.0
Provides:       crate(%{pkgname}/default-tls) = %{version}
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-tls" feature.

%package     -n %{name}+rustls-tls
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.2
Requires:       crate(reqwest-0.12/rustls-tls) >= 0.12.2
Requires:       crate(reqwest-0.12/stream) >= 0.12.2
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.28
Requires:       crate(indicatif-0.17/default) >= 0.17.5
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(num-cpus-1/default) >= 1.15.0
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(reqwest-0.12/charset) >= 0.12.2
Requires:       crate(reqwest-0.12/http2) >= 0.12.2
Requires:       crate(reqwest-0.12/json) >= 0.12.2
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.2
Requires:       crate(reqwest-0.12/stream) >= 0.12.2
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.29.1
Requires:       crate(tokio-1/fs) >= 1.29.1
Requires:       crate(tokio-1/macros) >= 1.29.1
Requires:       crate(tokio-1/rt-multi-thread) >= 1.29.1
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ureq
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "ureq"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(indicatif-0.17/default) >= 0.17.5
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(ureq-2/default) >= 2.0.0
Requires:       crate(ureq-2/json) >= 2.0.0
Requires:       crate(ureq-2/socks-proxy) >= 2.0.0
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Provides:       crate(%{pkgname}/ureq) = %{version}

%description -n %{name}+ureq
This metapackage enables feature "ureq" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
