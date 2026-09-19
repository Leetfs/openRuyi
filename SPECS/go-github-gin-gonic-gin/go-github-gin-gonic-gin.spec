# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gin
%define go_import_path  github.com/gin-gonic/gin

Name:           go-github-gin-gonic-gin
Version:        1.12.0
Release:        %autorelease
Summary:        Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.
License:        MIT
URL:            https://github.com/gin-gonic/gin
#!RemoteAsset:  sha256:c4210a179c9f129462eafcbd4d6d6dfe9559597be32c09041c1c9f797fa558bc
Source0:        https://github.com/gin-gonic/gin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/gin-gonic/gin/commit/b38c59de7fef67400a1c98efeae700a689c45783
Patch0:         0001-change-Unwrap-method-receiver-to-value-type.patch

BuildOption(prep):  -n %{_name}-%{version}

# For tests.



BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gin-contrib/sse)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/quic-go/quic-go)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/ugorji/go)
BuildRequires:  go(go.mongodb.org/mongo-driver/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(google.golang.org/protobuf/proto)

Provides:       go(github.com/gin-gonic/gin) = %{version}



Requires:       go(github.com/gin-contrib/sse)
Requires:       go(github.com/go-playground/validator/v10)
Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/pelletier/go-toml/v2)
Requires:       go(github.com/quic-go/quic-go)
Requires:       go(github.com/ugorji/go)
Requires:       go(go.mongodb.org/mongo-driver/v2)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/protobuf/proto)

%description
Gin is a high-performance HTTP web framework written in Go
(https://go.dev/). It provides a Martini-like API but with significantly
better performance—up to 40 times faster—thanks to httprouter
(https://github.com/julienschmidt/httprouter). Gin is designed for
building REST APIs, web applications, and microservices where speed and
developer productivity are essential.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
