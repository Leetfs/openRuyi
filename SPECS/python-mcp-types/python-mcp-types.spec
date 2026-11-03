# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mcp-types
%global pypi_name mcp_types

Name:           python-%{srcname}
Version:        2.3.0
Release:        %autorelease
Summary:        Model Context Protocol wire types
License:        MIT
URL:            https://github.com/modelcontextprotocol/python-sdk
#!RemoteAsset:  sha256:d1e46549edb35ee19a94940fcee6d1addd7e589ab7ea92dda83f5d84781fc362
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Protocol types and validation models for the Model Context Protocol Python SDK.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
