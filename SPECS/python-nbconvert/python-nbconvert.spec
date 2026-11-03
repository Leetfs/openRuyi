# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nbconvert

Name:           python-%{srcname}
Version:        7.17.2
Release:        %autorelease
Summary:        Convert Jupyter notebooks to other formats
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbconvert
#!RemoteAsset:  sha256:344a218e8595117ce37396ed025d994f146d076226ebac59255a2fa085ab24d8
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l nbconvert

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(bleach[css])
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(jupyter-core)
BuildRequires:  python3dist(jupyterlab-pygments)
BuildRequires:  python3dist(markupsafe)
BuildRequires:  python3dist(mistune)
BuildRequires:  python3dist(nbclient)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pandocfilters)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(traitlets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
nbconvert converts Jupyter notebooks to formats including HTML, Markdown,
LaTeX, PDF, reStructuredText, and executable scripts.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/jupyter-dejavu
%{_bindir}/jupyter-nbconvert
%{_datadir}/jupyter/nbconvert/templates

%changelog
%autochangelog
