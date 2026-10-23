# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           onnx
Version:        1.23.2
Release:        %autorelease
Summary:        Open standard for machine learning interoperability
License:        Apache-2.0
URL:            https://github.com/onnx/onnx
#!RemoteAsset:  sha256:2f23784e27d210a23b059a847c305e305034fb4a842fface3ff37283f85a2b40
Source:         https://github.com/onnx/onnx/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DONNX_BUILD_PYTHON=OFF
BuildOption(conf):  -DONNX_BUILD_TESTS=ON
BuildOption(conf):  -DONNX_USE_PROTOBUF_SHARED_LIBS=ON
BuildOption(conf):  -DFETCHCONTENT_FULLY_DISCONNECTED=ON

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  python3dist(nanobind)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(tabulate)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(ml-dtypes)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  pyproject-rpm-macros

%patchlist
# Build shared libraries instead of static
2000-Build-shared-libraries.patch
# Use the distribution Protobuf Python bindings for code generation.
2002-use-distribution-python-protobuf.patch
# https://github.com/onnx/onnx/commit/7e45ad5c7093ed498a5a09c1ef5537bb37da279c
2003-validate-layer-normalization-axis.patch

%description
%{name} provides an open source format for AI models, both deep learning and
traditional ML. It defines an extensible computation graph model, as well as
definitions of built-in operators and standard data types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(protobuf)

%description    devel
Development files for %{name}.

%package     -n python-onnx
Summary:        Python 3 bindings for %{name}
Provides:       python3-onnx
%python_provide python3-onnx

%description -n python-onnx
Python 3 bindings for %{name}.

%generate_buildrequires
%pyproject_buildrequires

%build -a
export CMAKE_ARGS="-Dnanobind_DIR=%{python3_sitelib}/nanobind/cmake \
-DONNX_USE_LITE_PROTO=OFF \
-DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
-DBUILD_SHARED_LIBS=ON \
-DFETCHCONTENT_FULLY_DISCONNECTED=ON \
-DCMAKE_SKIP_RPATH=ON"

%pyproject_wheel

%install -a
%pyproject_install
%pyproject_save_files onnx

install -p "./onnx/"*.proto -t "%{buildroot}/%{_includedir}/onnx/"

%check -a
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
# Fuzz drivers require Atheris; image fixtures and their doc generator require
# a Pillow JPEG 2000 encoder, which the distribution Pillow does not provide.
%pyproject_check_import -e 'onnx.fuzz.*' -e onnx.backend.test.case.node.image_decoder -e onnx.defs.gen_doc
cd %{buildroot}
# Python bindings and shared C++ consumers can coexist in one process.
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    %{__python3} -c "import ctypes, onnx; ctypes.CDLL('%{buildroot}%{_libdir}/libonnx.so.%{version}')"
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    %{__python3} -c "import ctypes; ctypes.CDLL('%{buildroot}%{_libdir}/libonnx.so.%{version}'); import onnx"
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest \
    --import-mode=importlib %{_builddir}/%{name}-%{version}/tests/python/checker_test.py \
    %{_builddir}/%{name}-%{version}/tests/python/external_data_test.py
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest \
    --import-mode=importlib %{_builddir}/%{name}-%{version}/tests/python/shape_inference_test.py \
    -k layer_normalization_axis_out_of_range

%files
%license LICENSE
%{_libdir}/libonnx.so.*
%{_libdir}/libonnx_proto.so.*

%files devel
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so
%{_libdir}/cmake/ONNX
%{_includedir}/onnx/

%files -n python-onnx -f %{pyproject_files}
%{_bindir}/backend-test-tools
%{_bindir}/check-model
%{_bindir}/check-node

%changelog
%autochangelog
