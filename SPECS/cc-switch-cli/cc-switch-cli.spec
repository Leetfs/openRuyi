# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cc-switch-cli
Version:        5.11.1
Release:        %autorelease
Summary:        All-in-one assistant for AI coding command-line tools
License:        MIT
URL:            https://github.com/SaladDay/cc-switch-cli
VCS:            git:https://github.com/SaladDay/cc-switch-cli.git
#!RemoteAsset:  sha256:8d9b6bc7f09f4e2177e3255a529b2616a76a514b5fcb4a90894cc86f84e8dc62
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    rust

Patch2000:      2000-align-integration-tests-with-5.11.patch

# Tests share process-global configuration.
BuildOption(check):  -- --test-threads=1

%ifarch riscv64
# Skip unsupported self-update target: Self-update is not supported for platform linux/riscv64.
BuildOption(check):  --skip cli::commands::update::tests::fetch_update_manifest_reads_latest_json_without_release_api
# Skip unsupported self-update target: Self-update is not supported for platform linux/riscv64.
BuildOption(check):  --skip cli::commands::update::tests::resolve_target_release_rejects_manifest_version_mismatch_for_explicit_version
%endif

# TakoPack-generated dependencies.
BuildRequires:  rust-rpm-macros
# Additional dependencies required by OBS builds.
BuildRequires:  rust
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-stream-0.3/default) >= 0.3.0
BuildRequires:  crate(axum-0.7/default) >= 0.7.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(brotli-7/default) >= 7.0.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.0
BuildRequires:  crate(clap-4/default) >= 4.5.0
BuildRequires:  crate(clap-complete-4/default) >= 4.5.0
BuildRequires:  crate(colored-2/default) >= 2.1.0
BuildRequires:  crate(comfy-table-7/default) >= 7.1.0
BuildRequires:  crate(console-0.15/default) >= 0.15.0
BuildRequires:  crate(dirs-5/default) >= 5.0.0
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.0
BuildRequires:  crate(flate2-1/default) >= 1.0.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(hmac-0.12/default) >= 0.12.0
BuildRequires:  crate(indexmap-2/default) >= 2.0.0
BuildRequires:  crate(indicatif-0.17/default) >= 0.17.0
BuildRequires:  crate(inquire-0.9/default) >= 0.9.0
BuildRequires:  crate(json-five-0.3/default) >= 0.3.1
BuildRequires:  crate(json5-0.4/default) >= 0.4.0
BuildRequires:  crate(minisign-verify-0.2/default) >= 0.2.4
BuildRequires:  crate(ratatui-0.30/default) >= 0.30.0
BuildRequires:  crate(reqwest-0.12/json) >= 0.12.0
BuildRequires:  crate(rquickjs-0.8/default) >= 0.8.0
BuildRequires:  crate(rusqlite-0.31/default) >= 0.31.0
BuildRequires:  crate(rust-decimal-1) >= 1.33.0
BuildRequires:  crate(serde-yaml-0.9/default) >= 0.9.0
BuildRequires:  crate(shlex-1/default) >= 1.3.0
BuildRequires:  crate(tachyonfx-0.25/default) >= 0.25.0
BuildRequires:  crate(tar-0.4/default) >= 0.4.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(toml-0.8/default) >= 0.8.0
BuildRequires:  crate(tower-http-0.5/default) >= 0.5.0
BuildRequires:  crate(unicode-width-0.1/default) >= 0.1.0
BuildRequires:  crate(which-6/default) >= 6.0.0
BuildRequires:  crate(zip-2/default) >= 2.2.0
BuildRequires:  crate(minisign-0.9/default) >= 0.9.1
BuildRequires:  crate(serial-test-3/default) >= 3.0.0
BuildRequires:  crate(self-replace-1) >= 1.0.0
BuildRequires:  crate(winreg-0.52) >= 0.52.0
BuildRequires:  crate(clap-4/derive) >= 4.5.0
BuildRequires:  crate(hyper-1/full) >= 1.0.0
BuildRequires:  crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/rustls-tls-webpki-roots) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.0
BuildRequires:  crate(borsh-1/unstable--schema) >= 1.1.1
BuildRequires:  crate(rkyv-0.7/size-32) >= 0.7.46
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(arbitrary-1/derive) >= 1.4.1
BuildRequires:  crate(clap-4/wrap-help) >= 4.5.0
BuildRequires:  crate(rand-chacha-0.3) >= 0.3.0
BuildRequires:  crate(rkyv-0.7/std) >= 0.7.46

%description
CC Switch CLI provides a terminal interface for managing providers,
configuration, prompts, and MCP servers for Claude Code, Codex, Gemini,
OpenCode, and OpenClaw.

%prep -a
# The Rust package is kept in src-tauri even though this CLI has no Tauri UI.
cp -a src-tauri/. .
# Preserve upstream relative paths to the install script and shared test data.
cp -p install.sh ..
install -Dm0644 tests/config/claudeKeyFields.json ../tests/config/claudeKeyFields.json
rm -f Cargo.lock rust-toolchain.toml

%check -p
export RUST_TEST_FLAGS="${RUST_TEST_FLAGS:+$RUST_TEST_FLAGS }--no-fail-fast"

%install
install -Dm0755 target/release/cc-switch %{buildroot}%{_bindir}/cc-switch

%files
%doc README.md README_ZH.md
%license LICENSE
%{_bindir}/cc-switch

%changelog
%autochangelog
