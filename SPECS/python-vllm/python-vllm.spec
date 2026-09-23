# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}

%global srcname vllm

%global onednn_ver 3.10

%global triton_kernels_ver 3.5.1

%global llvm_maj_ver 22

%if "%{flavor}" == "rocm"
%bcond rocm 1
%else
%bcond rocm 0
%endif

%if %{with rocm}
%global toolchain clang
%endif

%if %{with rocm}
Name:           python-%{srcname}-rocm
%else
Name:           python-%{srcname}
%endif
Version:        0.29.0
Release:        %autorelease
Summary:        A high-throughput and memory-efficient inference and serving engine for LLMs
License:        Apache-2.0
URL:            https://github.com/vllm-project/vllm
#!RemoteAsset:  sha256:c03feb07943ecae9e69e7dc424d7c5569ecf8d1292513aef2a4de67af381cd97
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:ba5834a1fdbb6d1c1b1c065dfd789438e7aa42c03fc52d92c02af85d78d1c75c
Source1:        https://github.com/uxlfoundation/oneDNN/archive/refs/tags/v%{onednn_ver}.tar.gz
#!RemoteAsset:  sha256:03d7c41f6f2dc1dfa3445776c4a893dc34b1e0ece42b953f036c071ff6409b80
Source2:        https://github.com/triton-lang/triton/archive/refs/tags/v%{triton_kernels_ver}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(jinja2)
BuildRequires:  libomp
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  python3dist(numpy)
BuildRequires:  rust >= 1.85
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(arc-swap-1/default) >= 1.9.1
BuildRequires:  crate(async-openai-0.33/native-tls) >= 0.33.1
BuildRequires:  crate(async-openai-macros-0.1/default) >= 0.1.1
BuildRequires:  crate(asynk-strim-attr-0.1/default) >= 0.1.0
BuildRequires:  crate(auto-enums-0.8/default) >= 0.8.9
BuildRequires:  crate(auto-enums-0.8/tokio1) >= 0.8.9
BuildRequires:  crate(axum-0.8/default) >= 0.8.8
BuildRequires:  crate(backoff-0.4/default) >= 0.4.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(bytemuck-1/default) >= 1.25.0
BuildRequires:  crate(bytemuck-1/extern-crate-alloc) >= 1.25.0
BuildRequires:  crate(byteorder-1/default) >= 1.5.0
BuildRequires:  crate(bytes-1/default) >= 1.12.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.44
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-4/env) >= 4.6.1
BuildRequires:  crate(criterion-0.5/default) >= 0.5.1
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(easy-ext-1/default) >= 1.0.3
BuildRequires:  crate(educe-0.6/default) >= 0.6.0
BuildRequires:  crate(enum-as-inner-0.7/default) >= 0.7.0
BuildRequires:  crate(eventsource-stream-0.2) >= 0.2.3
BuildRequires:  crate(expect-test-1/default) >= 1.5.1
BuildRequires:  crate(fastokens-0.2) >= 0.2.1
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(half-2/bytemuck) >= 2.7.1
BuildRequires:  crate(half-2/default) >= 2.7.1
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(hf-hub-0.5/tokio) >= 0.5.0
BuildRequires:  crate(hmac-0.12/default) >= 0.12.1
BuildRequires:  crate(http-body-1/default) >= 1.0.1
BuildRequires:  crate(hyper-util-0.1/default) >= 0.1.20
BuildRequires:  crate(hyper-util-0.1/server-graceful) >= 0.1.20
BuildRequires:  crate(hyper-util-0.1/service) >= 0.1.20
BuildRequires:  crate(hyper-util-0.1/tokio) >= 0.1.20
BuildRequires:  crate(hyper-1/default) >= 1.10.1
BuildRequires:  crate(hyper-1/http1) >= 1.10.1
BuildRequires:  crate(hyper-1/server) >= 1.10.1
BuildRequires:  crate(image-0.25/jpeg) >= 0.25.10
BuildRequires:  crate(indexmap-2/default) >= 2.14.0
BuildRequires:  crate(indicatif-0.18/default) >= 0.18.4
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(llm-multimodal-1/native-tls) >= 1.7.1
BuildRequires:  crate(mimalloc-0.1/default) >= 0.1.52
BuildRequires:  crate(minijinja-contrib-2/default) >= 2.24.0
BuildRequires:  crate(minijinja-contrib-2/pycompat) >= 2.24.0
BuildRequires:  crate(minijinja-2/builtins) >= 2.24.0
BuildRequires:  crate(minijinja-2/default) >= 2.24.0
BuildRequires:  crate(minijinja-2/json) >= 2.24.0
BuildRequires:  crate(minijinja-2/loader) >= 2.24.0
BuildRequires:  crate(minijinja-2/loop-controls) >= 2.24.0
BuildRequires:  crate(minijinja-2/preserve-order) >= 2.24.0
BuildRequires:  crate(minijinja-2/unstable-machinery) >= 2.24.0
BuildRequires:  crate(native-tls-0.2/default) >= 0.2.18
BuildRequires:  crate(native-tls-0.2/vendored) >= 0.2.18
BuildRequires:  crate(ndarray-0.17/default) >= 0.17.2
BuildRequires:  crate(ndarray-0.17/serde) >= 0.17.2
BuildRequires:  crate(openssl-0.10/default) >= 0.10.80
BuildRequires:  crate(oss-harmony-0.0.11) >= 0.0.11
BuildRequires:  crate(openai-protocol-1/default) >= 1.6.0
BuildRequires:  crate(parking-lot-0.12/default) >= 0.12.5
BuildRequires:  crate(parquet-59/brotli) >= 59.2.0
BuildRequires:  crate(parquet-59/flate2) >= 59.2.0
BuildRequires:  crate(parquet-59/flate2-rust-backend) >= 59.2.0
BuildRequires:  crate(parquet-59/json) >= 59.2.0
BuildRequires:  crate(parquet-59/lz4) >= 59.2.0
BuildRequires:  crate(parquet-59/snap) >= 59.2.0
BuildRequires:  crate(parquet-59/zstd) >= 59.2.0
BuildRequires:  crate(prometheus-client-0.24/default) >= 0.24.0
BuildRequires:  crate(prost-types-0.14/default) >= 0.14.3
BuildRequires:  crate(prost-0.14/default) >= 0.14.3
BuildRequires:  crate(protox-0.9/default) >= 0.9.1
BuildRequires:  crate(pyo3-0.28/abi3-py38) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.3
BuildRequires:  crate(pythonize-0.28/default) >= 0.28.0
BuildRequires:  crate(pythonize-0.28/serde-json) >= 0.28.0
BuildRequires:  crate(rand-distr-0.5/default) >= 0.5.1
BuildRequires:  crate(rand-0.9/default) >= 0.9.4
BuildRequires:  crate(rayon-1/default) >= 1.12.0
BuildRequires:  crate(reqwest-0.12/http2) >= 0.12.28
BuildRequires:  crate(reqwest-0.12/json) >= 0.12.28
BuildRequires:  crate(reqwest-0.12/native-tls) >= 0.12.28
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.28
BuildRequires:  crate(reqwest-0.13/native-tls) >= 0.13.4
BuildRequires:  crate(reqwest-eventsource-0.6/default) >= 0.6.0
BuildRequires:  crate(riptoken-0.3) >= 0.3.0
BuildRequires:  crate(rlimit-0.11/default) >= 0.11.0
BuildRequires:  crate(rmp-serde-1/default) >= 1.3.1
BuildRequires:  crate(rmpv-1/default) >= 1.3.1
BuildRequires:  crate(rmpv-1/with-serde) >= 1.3.1
BuildRequires:  crate(rustc-hash-1/default) >= 1.1.0
BuildRequires:  crate(secrecy-0.10/default) >= 0.10.3
BuildRequires:  crate(serde-default-0.2/default) >= 0.2.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(serde-json-1/preserve-order) >= 1.0.150
BuildRequires:  crate(serde-json-1/raw-value) >= 1.0.150
BuildRequires:  crate(serde-repr-0.1/default) >= 0.1.20
BuildRequires:  crate(serde-tuple-1/default) >= 1.1.3
BuildRequires:  crate(serde-with-3/default) >= 3.20.0
BuildRequires:  crate(serde-json-fmt-0.1/default) >= 0.1.0
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-1/rc) >= 1.0.228
BuildRequires:  crate(serial-test-3/file-locks) >= 3.2.0
BuildRequires:  crate(sha2-0.10/default) >= 0.10.9
BuildRequires:  crate(socket2-0.6/default) >= 0.6.3
BuildRequires:  crate(strum-0.27/default) >= 0.27.2
BuildRequires:  crate(strum-0.27/derive) >= 0.27.2
BuildRequires:  crate(subenum-1/default) >= 1.1.3
BuildRequires:  crate(subtle-2/default) >= 2.6.1
BuildRequires:  crate(task-local-0.1/default) >= 0.1.1
BuildRequires:  crate(tekken-rs-0.1) >= 0.1.1
BuildRequires:  crate(thiserror-ext-0.3/default) >= 0.3.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(tiktoken-rs-0.9/default) >= 0.9.1
BuildRequires:  crate(time-0.3/default) >= 0.3.47
BuildRequires:  crate(time-0.3/formatting) >= 0.3.47
BuildRequires:  crate(time-0.3/local-offset) >= 0.3.47
BuildRequires:  crate(time-0.3/macros) >= 0.3.47
BuildRequires:  crate(tls-listener-0.11/axum) >= 0.11.2
BuildRequires:  crate(tls-listener-0.11/openssl) >= 0.11.2
BuildRequires:  crate(tls-listener-0.11/tokio-net) >= 0.11.2
BuildRequires:  crate(tokenizers-0.22/default) >= 0.22.2
BuildRequires:  crate(tokio-openssl-0.6/default) >= 0.6.5
BuildRequires:  crate(tokio-stream-0.1/default) >= 0.1.18
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.18
BuildRequires:  crate(tokio-util-0.7/rt) >= 0.7.18
BuildRequires:  crate(tokio-1/default) >= 1.52.3
BuildRequires:  crate(tokio-1/macros) >= 1.52.3
BuildRequires:  crate(tokio-1/net) >= 1.52.3
BuildRequires:  crate(tokio-1/process) >= 1.52.3
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.52.3
BuildRequires:  crate(tokio-1/signal) >= 1.52.3
BuildRequires:  crate(tokio-1/sync) >= 1.52.3
BuildRequires:  crate(tokio-1/time) >= 1.52.3
BuildRequires:  crate(tonic-health-0.14/default) >= 0.14.6
BuildRequires:  crate(tonic-prost-build-0.14/default) >= 0.14.6
BuildRequires:  crate(tonic-prost-0.14/default) >= 0.14.6
BuildRequires:  crate(tonic-0.14/default) >= 0.14.6
BuildRequires:  crate(tool-parser-1/default) >= 1.2.0
BuildRequires:  crate(tower-http-0.6/cors) >= 0.6.8
BuildRequires:  crate(tower-http-0.6/default) >= 0.6.8
BuildRequires:  crate(tower-http-0.6/trace) >= 0.6.8
BuildRequires:  crate(tower-0.5/default) >= 0.5.3
BuildRequires:  crate(tower-0.5/util) >= 0.5.3
BuildRequires:  crate(tracing-futures-0.2/default) >= 0.2.5
BuildRequires:  crate(tracing-futures-0.2/futures-03) >= 0.2.5
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/fmt) >= 0.3.23
BuildRequires:  crate(tracing-0.1/default) >= 0.1.44
BuildRequires:  crate(tracing-0.1/release-max-level-debug) >= 0.1.44
BuildRequires:  crate(trait-set-0.3/default) >= 0.3.0
BuildRequires:  crate(url-2/default) >= 2.5.8
BuildRequires:  crate(uuid-1/default) >= 1.23.2
BuildRequires:  crate(uuid-1/v4) >= 1.23.2
BuildRequires:  crate(validator-0.20/default) >= 0.20.0
BuildRequires:  crate(validator-0.20/derive) >= 0.20.0
BuildRequires:  crate(winnow-1/default) >= 1.0.3
BuildRequires:  crate(winnow-1/simd) >= 1.0.3
BuildRequires:  crate(xgrammar-structural-tag-0.2/default) >= 0.2.0
BuildRequires:  crate(zeromq-0.6/all-transport) >= 0.6.0
BuildRequires:  crate(zeromq-0.6/tokio-runtime) >= 0.6.0

%if %{with rocm}
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hipblaslt)
BuildRequires:  cmake(hipcub)
BuildRequires:  cmake(hipfft)
BuildRequires:  cmake(hiprand)
BuildRequires:  cmake(hipsparse)
BuildRequires:  cmake(hipsparselt)
BuildRequires:  cmake(hipsolver)
BuildRequires:  cmake(miopen)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(rocrand)
BuildRequires:  cmake(rocfft)
BuildRequires:  cmake(rccl)
BuildRequires:  cmake(rocprim)
BuildRequires:  cmake(rocsolver)
BuildRequires:  cmake(rocthrust)
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(rocm-core)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocm_smi)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  hipcc
BuildRequires:  libstdc++-devel
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  python-torch-rocm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros
BuildRequires:  rocminfo
BuildRequires:  roctracer-devel
%else
BuildRequires:  cmake(sleef)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(numa)
BuildRequires:  python-torch-devel
%endif

Requires:       ninja
Requires:       python3dist(uvloop)
%if %{with rocm}
Requires:       python-torch-rocm
Requires:       python3dist(triton)
Requires:       amdsmi
%else
Requires:       python3dist(torch)
%endif

%if %{with rocm}
Provides:       vllm-rocm = %{version}-%{release}
Conflicts:      python-%{srcname}
%else
Provides:       python-%{srcname} = %{version}-%{release}
Provides:       vllm = %{version}-%{release}
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
Conflicts:      python-%{srcname}-rocm
%endif

%patchlist
%if %{with rocm}
# Unmerged upstream PR retained only for ROCm gfx12xx architecture support:
# https://github.com/vllm-project/vllm/pull/45916
2000-ROCm-split-KV-paged-decode.patch
%endif
2001-Adjust-dependencies-for-openRuyi.patch
# Allow single-process execution when PyTorch lacks the Gloo backend
2002-CPU-single-process-fake-distributed-backend.patch
%if %{with rocm}
# Define roc::hipsparselt before importing Torch's CMake targets
2003-ROCm-hipsparselt-ordering.patch
# Build cumem_allocator with ROCm HIP
2004-cumem_allocator-define-USE_ROCM-for-CXX-target.patch
%else
# Adjust CPU backend for openRuyi's OpenMP path
2005-CPU-backend-OpenMP-path.patch
%endif
# Redirect fixed Git Rust dependencies to system registry providers
2006-Use-system-registry-for-Git-Rust-dependencies.patch
# Resolve the Rust workspace against the packaged system-registry versions
2007-Refresh-Rust-lockfile-for-system-registry.patch
# Match the currently published system-registry package versions
2008-Refresh-Cargo-lockfile-for-current-system-registry.patch

%description
vLLM is a fast and easy-to-use library for LLM inference and serving, featuring
PagedAttention for efficient management of attention key/value memory,
continuous batching of incoming requests, and an OpenAI-compatible API server.

%prep -a
%rust_setup_registry
%if %{without rocm}
# OneDNN is used for CPU backend
tar -xzf %{SOURCE1}
%else
# triton_kernels is required by the ROCm backend and must be provided offline.
tar -xzf %{SOURCE2}
%endif

%generate_buildrequires
%if %{with rocm}
export VLLM_VERSION_OVERRIDE=%{version}+rocm
export VLLM_TARGET_DEVICE=rocm
%else
export VLLM_VERSION_OVERRIDE=%{version}+cpu
export VLLM_TARGET_DEVICE=cpu
%endif
%pyproject_buildrequires -R

%build -p
%if %{with rocm}
export VLLM_VERSION_OVERRIDE=%{version}+rocm
export VLLM_TARGET_DEVICE=rocm
export PYTORCH_ROCM_ARCH=%{rocm_gpu_list_default}
export ROCM_HOME=%{_prefix}
export PATH=%{rocmllvm_bindir}:$PATH
export HIP_CLANG_PATH=%{rocmllvm_bindir}
export TRITON_KERNELS_SRC_DIR="$PWD/triton-%{triton_kernels_ver}/python/triton_kernels/triton_kernels"
export CMAKE_ARGS="-DCMAKE_HIP_FLAGS=--rocm-device-lib-path=$(%{rocmllvm_bindir}/clang -print-resource-dir)/amdgcn/bitcode"
%else
export VLLM_VERSION_OVERRIDE=%{version}+cpu
export VLLM_TARGET_DEVICE=cpu
export FETCHCONTENT_SOURCE_DIR_ONEDNN="$PWD/oneDNN-%{onednn_ver}"
# RISC-V CPU: cpu_extension.cmake auto-detects the RVV vector length from /proc/cpuinfo
# SG2044 has VLEN=128
%ifarch riscv64
export CMAKE_ARGS="-DVLLM_RVV_VLEN=128"
%endif
%endif
export VLLM_REQUIRE_RUST_FRONTEND=1
export CMAKE_BUILD_TYPE=Release

# Limit parallelism by available memory to avoid builder OOM.
mem_gb=$(awk '/MemTotal/ {print int($2/1024/1024)}' /proc/meminfo)
compile_jobs=$(nproc)
mem_jobs=$(( 1 + mem_gb / 3 ))
[ "$mem_jobs" -lt "$compile_jobs" ] && compile_jobs=$mem_jobs
[ "$compile_jobs" -lt 1 ] && compile_jobs=1
export MAX_JOBS=$compile_jobs

%check
# Not all runtime dependencies and backend setup are unavailable.
# vLLM have several backend and we only use two of them.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/vllm

%changelog
%autochangelog
