# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cohere

Name:           python-%{srcname}
Version:        6.1.0
Release:        %autorelease
Summary:        Python Library for Accessing the Cohere API
License:        MIT
URL:            https://github.com/cohere-ai/cohere-python
#!RemoteAsset:  sha256:6a52bb459b71b5e79735412ee1a8e87028c5b3afba050c39815fe03c083249b3
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Upstream supports pydantic-core 2.x in its SDK metadata.
# https://github.com/cohere-ai/cohere-python/commit/b751bc1ad568b13a557c90d2e8d57972e078f05a
Patch1000:      1000-backport-pydantic-core-range.patch

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(fastavro)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pydantic-core)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(tokenizers)
BuildRequires:  python3dist(types-requests)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The Cohere Python SDK allows access to Cohere models across many different
platforms: the cohere platform, AWS (Bedrock, Sagemaker), Azure, GCP and
Oracle OCI.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Check that Cohere's Pydantic adapter still coerces string values to typed integers.
%py3_test_envvars %{__python3} -c 'from cohere.core.pydantic_utilities import parse_obj_as; assert parse_obj_as(list[int], ["42"]) == [42]'

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
