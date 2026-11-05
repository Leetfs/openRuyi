# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jquery3
Version:        3.7.1
Release:        %autorelease
Summary:        jQuery 3 JavaScript library
License:        MIT
URL:            https://jquery.com/
VCS:            git:https://github.com/jquery/jquery.git
#!RemoteAsset:  sha256:78a85aca2f0b110c29e0d2b137e09f0a1fb7a8e554b499f740d6744dc8962cfe
Source0:        https://code.jquery.com/jquery-%{version}.js
#!RemoteAsset:  sha256:d4db9ebe6f29f5168eac45ad713f055623ac5d0dcd5ba92da23d650ae012020d
Source1:        https://raw.githubusercontent.com/jquery/jquery/%{version}/LICENSE.txt
BuildArch:      noarch

BuildRequires:  nodejs

%description
jQuery provides DOM traversal, event handling and browser utilities for
JavaScript applications. This package supplies the jQuery 3 API used by
applications such as the TestNG HTML report viewer.

%prep
%setup -q -c -T
cp -p %{SOURCE0} jquery.js
cp -p %{SOURCE1} LICENSE.txt

%install
install -Dpm644 jquery.js %{buildroot}%{_datadir}/javascript/jquery3/jquery.js

%check
node --check jquery.js
node <<'JS'
const assert = require('node:assert/strict');
const createJQuery = require('./jquery.js');
assert.equal(typeof createJQuery, 'function');
assert.throws(() => createJQuery({}), /jQuery requires a window with a document/);
JS

%files
%license LICENSE.txt
%{_datadir}/javascript/jquery3/

%changelog
%autochangelog
