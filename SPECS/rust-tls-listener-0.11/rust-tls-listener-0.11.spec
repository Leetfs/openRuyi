# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tls-listener
%global full_version 0.11.2
%global pkgname tls-listener-0.11

Name:           rust-tls-listener-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "tls-listener"
License:        Apache-2.0
URL:            https://github.com/tmccombs/tls-listener
#!RemoteAsset:  sha256:1461056cc1ef47003f7ee16e4cef3741068d4c7f6b627bfce49b7c00c120a530
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-util-0.3/default) >= 0.3.32
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/time) >= 1.52.3

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tls-listener"

%package     -n %{name}+axum
Summary:        Wrap incoming Stream of connections in TLS - feature "axum"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(axum-0.8/http1) >= 0.8.8
Requires:       crate(axum-0.8/tokio) >= 0.8.8
Provides:       crate(%{pkgname}/axum) = %{version}

%description -n %{name}+axum
This metapackage enables feature "axum" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl
Summary:        Wrap incoming Stream of connections in TLS - feature "openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/openssl-impl) = %{version}
Requires:       crate(%{pkgname}/tokio-openssl) = %{version}
Provides:       crate(%{pkgname}/openssl) = %{version}

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-impl
Summary:        Wrap incoming Stream of connections in TLS - feature "openssl_impl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.81
Provides:       crate(%{pkgname}/openssl-impl) = %{version}

%description -n %{name}+openssl-impl
This metapackage enables feature "openssl_impl" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt
Summary:        Wrap incoming Stream of connections in TLS - feature "rt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/rt) >= 1.52.3
Requires:       crate(tokio-1/time) >= 1.52.3
Provides:       crate(%{pkgname}/rt) = %{version}

%description -n %{name}+rt
This metapackage enables feature "rt" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Wrap incoming Stream of connections in TLS - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-aws-lc) = %{version}
Requires:       crate(tokio-rustls-0.26/default) >= 0.26.1
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-aws-lc
Summary:        Wrap incoming Stream of connections in TLS - feature "rustls-aws-lc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-core) = %{version}
Requires:       crate(tokio-rustls-0.26/aws-lc-rs) >= 0.26.1
Provides:       crate(%{pkgname}/rustls-aws-lc) = %{version}

%description -n %{name}+rustls-aws-lc
This metapackage enables feature "rustls-aws-lc" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-fips
Summary:        Wrap incoming Stream of connections in TLS - feature "rustls-fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-aws-lc) = %{version}
Requires:       crate(tokio-rustls-0.26/fips) >= 0.26.1
Provides:       crate(%{pkgname}/rustls-fips) = %{version}

%description -n %{name}+rustls-fips
This metapackage enables feature "rustls-fips" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-ring
Summary:        Wrap incoming Stream of connections in TLS - feature "rustls-ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-core) = %{version}
Requires:       crate(tokio-rustls-0.26/ring) >= 0.26.1
Provides:       crate(%{pkgname}/rustls-ring) = %{version}

%description -n %{name}+rustls-ring
This metapackage enables feature "rustls-ring" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-native-tls
Summary:        Wrap incoming Stream of connections in TLS - feature "tokio-native-tls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-native-tls-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/native-tls) = %{version}
Provides:       crate(%{pkgname}/tokio-native-tls) = %{version}

%description -n %{name}+tokio-native-tls
This metapackage enables feature "tokio-native-tls" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "native-tls" feature.

%package     -n %{name}+tokio-net
Summary:        Wrap incoming Stream of connections in TLS - feature "tokio-net" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/net) >= 1.52.3
Requires:       crate(tokio-1/time) >= 1.52.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tokio-net) = %{version}

%description -n %{name}+tokio-net
This metapackage enables feature "tokio-net" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio-openssl
Summary:        Wrap incoming Stream of connections in TLS - feature "tokio-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-openssl-0.6/default) >= 0.6.5
Provides:       crate(%{pkgname}/tokio-openssl) = %{version}

%description -n %{name}+tokio-openssl
This metapackage enables feature "tokio-openssl" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-rustls
Summary:        Wrap incoming Stream of connections in TLS - feature "tokio-rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-rustls-0.26) >= 0.26.1
Provides:       crate(%{pkgname}/rustls-core) = %{version}
Provides:       crate(%{pkgname}/tokio-rustls) = %{version}

%description -n %{name}+tokio-rustls
This metapackage enables feature "tokio-rustls" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustls-core" feature.

%package     -n %{name}+tracing
Summary:        Wrap incoming Stream of connections in TLS - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/default) >= 0.1.44
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust tls-listener crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
