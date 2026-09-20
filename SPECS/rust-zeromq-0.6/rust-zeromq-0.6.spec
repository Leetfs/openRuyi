# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zeromq
%global full_version 0.6.0
%global pkgname zeromq-0.6

Name:           rust-zeromq-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "zeromq"
License:        MIT
URL:            https://github.com/zeromq/zmq.rs
#!RemoteAsset:  sha256:efb2c254fd8f366755335c9e43b865f8484fe3bd717d65ffe7c3f28852863030
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.89
Requires:       crate(asynchronous-codec-0.7/default) >= 0.7.0
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(crossbeam-queue-0.3/default) >= 0.3.12
Requires:       crate(futures-0.3/default) >= 0.3.32
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(once-cell-1/default) >= 1.21.4
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(regex-1/std) >= 1.12.3
Requires:       crate(regex-1/unicode-perl) >= 1.12.3
Requires:       crate(scc-3/default) >= 3.6.9
Requires:       crate(thiserror-1/default) >= 1.0.69
Requires:       crate(uuid-1/default) >= 1.22.0
Requires:       crate(uuid-1/v4) >= 1.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/tcp-transport) = %{version}

%description
Source code for takopackized Rust crate "zeromq"

%package     -n %{name}+all-transport
Summary:        Native Rust implementation of ZeroMQ - feature "all-transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ipc-transport) = %{version}
Requires:       crate(%{pkgname}/tcp-transport) = %{version}
Provides:       crate(%{pkgname}/all-transport) = %{version}

%description -n %{name}+all-transport
This metapackage enables feature "all-transport" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-dispatcher
Summary:        Native Rust implementation of ZeroMQ - feature "async-dispatcher"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-dispatcher-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/async-dispatcher) = %{version}

%description -n %{name}+async-dispatcher
This metapackage enables feature "async-dispatcher" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-dispatcher-macros
Summary:        Native Rust implementation of ZeroMQ - feature "async-dispatcher-macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-dispatcher-0.1/macros) >= 0.1.0
Provides:       crate(%{pkgname}/async-dispatcher-macros) = %{version}

%description -n %{name}+async-dispatcher-macros
This metapackage enables feature "async-dispatcher-macros" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-dispatcher-runtime
Summary:        Native Rust implementation of ZeroMQ - feature "async-dispatcher-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-dispatcher) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/async-dispatcher-runtime) = %{version}

%description -n %{name}+async-dispatcher-runtime
This metapackage enables feature "async-dispatcher-runtime" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Native Rust implementation of ZeroMQ - feature "async-std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/attributes) >= 1.0.0
Requires:       crate(async-std-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/async-std) = %{version}
Provides:       crate(%{pkgname}/async-std-runtime) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async-std-runtime" feature.

%package     -n %{name}+default
Summary:        Native Rust implementation of ZeroMQ - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-transport) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ipc-transport
Summary:        Native Rust implementation of ZeroMQ - feature "ipc-transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(win-uds-0.2/async) >= 0.2.2
Requires:       crate(win-uds-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/ipc-transport) = %{version}

%description -n %{name}+ipc-transport
This metapackage enables feature "ipc-transport" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Native Rust implementation of ZeroMQ - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/full) >= 1.52.3
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-runtime
Summary:        Native Rust implementation of ZeroMQ - feature "tokio-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Provides:       crate(%{pkgname}/tokio-runtime) = %{version}

%description -n %{name}+tokio-runtime
This metapackage enables feature "tokio-runtime" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Native Rust implementation of ZeroMQ - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/compat) >= 0.7.18
Requires:       crate(tokio-util-0.7/default) >= 0.7.18
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust zeromq crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
