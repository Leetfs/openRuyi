# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otlptrace
%define go_import_path  go.opentelemetry.io/otel/exporters/otlp/otlptrace

Name:           go-opentelemetry-otel-exporters-otlp-otlptrace
Version:        1.47.0
Release:        %autorelease
Summary:        OTLP trace exporter abstractions for OpenTelemetry Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:4e8bd2fcc26dd6a61df4edf478c00c9cf661bae4cbc1f4621df006a9e642b7da
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/refs/tags/exporters/otlp/otlptrace/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules



BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp) = %{version}

Requires:       go(github.com/cenkalti/backoff/v5)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
OTLP trace exporter abstractions and gRPC and HTTP exporters for OpenTelemetry Go.

%install
# The parent source directory contains all three nested modules.
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a exporters/otlp/otlptrace/. %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/go.opentelemetry.io
cp -a . %{_builddir}/go/src/go.opentelemetry.io/otel
cd %{_builddir}/go/src/%{go_import_path}
go test -v ./...

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
