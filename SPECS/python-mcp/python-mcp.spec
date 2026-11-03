# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mcp

Name:           python-%{srcname}
Version:        2.3.0
Release:        %autorelease
Summary:        Model Context Protocol SDK
License:        MIT
URL:            https://github.com/modelcontextprotocol/python-sdk
#!RemoteAsset:  sha256:8b147a50441cf059dc88c684e0aeed3687f0aa0f39c6cde7b90330effd2b34d8
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Patches

BuildOption(install):  -l %{srcname}
# The CLI needs the typer extra. The removed v1 fastmcp module raises on import
# to direct callers to the v2 MCPServer API.
BuildOption(check):  -e 'mcp.cli*' -e mcp.server.fastmcp %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(anyio)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(httpx2)
BuildRequires:  python3dist(httpx-sse)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pydantic-settings)
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(python-multipart)
BuildRequires:  python3dist(sse-starlette)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(typing-inspection)
BuildRequires:  python3dist(uvicorn)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python SDK for the Model Context Protocol (MCP), providing client and server
components for MCP-based integrations.

%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/mcp

%changelog
%autochangelog
