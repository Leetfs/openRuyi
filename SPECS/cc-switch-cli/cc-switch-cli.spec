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
