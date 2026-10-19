# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name io-extras
%global full_version 0.19.0
%global pkgname io-extras-0.19

Name:           rust-io-extras-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "io-extras"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/sunfishcode/io-extras
#!RemoteAsset:  sha256:20fd6de4ccfcc187e38bc21cfa543cb5a302cb86a8b114eb7f0bf0dc9f8ac00f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(io-lifetimes-3/default) >= 3.0.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-console) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "io-extras"

%package     -n %{name}+async-std
Summary:        File/socket handle/descriptor utilities - feature "async-std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.13.0
Requires:       crate(async-std-1/io-safety) >= 1.13.0
Provides:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/use-async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_async_std" feature.

%package     -n %{name}+mio
Summary:        File/socket handle/descriptor utilities - feature "mio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-1/default) >= 1.0.2
Provides:       crate(%{pkgname}/mio) = %{version}

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+os-pipe
Summary:        File/socket handle/descriptor utilities - feature "os_pipe" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(os-pipe-1/default) >= 1.2.1
Provides:       crate(%{pkgname}/os-pipe) = %{version}
Provides:       crate(%{pkgname}/use-os-pipe) = %{version}

%description -n %{name}+os-pipe
This metapackage enables feature "os_pipe" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_os_pipe" feature.

%package     -n %{name}+socket2
Summary:        File/socket handle/descriptor utilities - feature "socket2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/socket2) = %{version}
Provides:       crate(%{pkgname}/use-socket2) = %{version}

%description -n %{name}+socket2
This metapackage enables feature "socket2" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_socket2" feature.

%package     -n %{name}+tokio
Summary:        File/socket handle/descriptor utilities - feature "tokio" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.6.0
Requires:       crate(tokio-1/fs) >= 1.6.0
Requires:       crate(tokio-1/io-std) >= 1.6.0
Requires:       crate(tokio-1/net) >= 1.6.0
Requires:       crate(tokio-1/process) >= 1.6.0
Provides:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/use-tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_tokio" feature.

%package     -n %{name}+use-mio-net
Summary:        File/socket handle/descriptor utilities - feature "use_mio_net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mio) = %{version}
Requires:       crate(mio-1/net) >= 1.0.2
Provides:       crate(%{pkgname}/use-mio-net) = %{version}

%description -n %{name}+use-mio-net
This metapackage enables feature "use_mio_net" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-mio-os-ext
Summary:        File/socket handle/descriptor utilities - feature "use_mio_os_ext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mio) = %{version}
Requires:       crate(mio-1/os-ext) >= 1.0.2
Provides:       crate(%{pkgname}/use-mio-os-ext) = %{version}

%description -n %{name}+use-mio-os-ext
This metapackage enables feature "use_mio_os_ext" for the Rust io-extras crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
