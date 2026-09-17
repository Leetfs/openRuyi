# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ripgrep
Version:        15.2.0
Release:        %autorelease
Summary:        Fast recursive text search tool
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep
#!RemoteAsset:  sha256:7605249d3eb0d5f170e3414498e3344e26b1e7a147aec518b57090b80036a562
Source:         https://github.com/BurntSushi/ripgrep/archive/refs/tags/%{version}.tar.gz
BuildSystem:    rust

# The OBS targets use glibc; avoid resolving the unused musl allocator.
Patch2000:      2000-remove-musl-jemalloc-dependency.patch

BuildOption(build):  --features pcre2

BuildRequires:  rust >= 1.85
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  crate(aho-corasick-1/default) >= 1.1.1
BuildRequires:  crate(arbitrary-1/default) >= 1.3.2
BuildRequires:  crate(arbitrary-1/derive) >= 1.3.2
BuildRequires:  crate(anyhow-1/default) >= 1.0.75
BuildRequires:  crate(bstr-1/default) >= 1.6.2
BuildRequires:  crate(bstr-1/std) >= 1.6.2
BuildRequires:  crate(crossbeam-channel-0.5/default) >= 0.5.15
BuildRequires:  crate(crossbeam-deque-0.8/default) >= 0.8.3
BuildRequires:  crate(encoding-rs-0.8/default) >= 0.8.33
BuildRequires:  crate(encoding-rs-io-0.1/default) >= 0.1.7
BuildRequires:  crate(glob-0.3/default) >= 0.3.1
BuildRequires:  crate(lexopt-0.3/default) >= 0.3.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.148
BuildRequires:  crate(log-0.4/default) >= 0.4.20
BuildRequires:  crate(memchr-2/default) >= 2.6.3
BuildRequires:  crate(memmap2-0.9/default) >= 0.9.0
BuildRequires:  crate(pcre2-0.2/default) >= 0.2.6
BuildRequires:  crate(regex-1/default) >= 1.9.5
BuildRequires:  crate(regex-automata-0.4/default) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/dfa-onepass) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/hybrid) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/meta) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/nfa) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/perf) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/std) >= 0.4.0
BuildRequires:  crate(regex-automata-0.4/syntax) >= 0.4.0
BuildRequires:  crate(regex-syntax-0.8/default) >= 0.8.0
BuildRequires:  crate(regex-syntax-0.8/std) >= 0.8.0
BuildRequires:  crate(same-file-1/default) >= 1.0.6
BuildRequires:  crate(serde-1/default) >= 1.0.193
BuildRequires:  crate(serde-derive-1/default) >= 1.0.77
BuildRequires:  crate(serde-json-1/default) >= 1.0.107
BuildRequires:  crate(termcolor-1/default) >= 1.3.0
BuildRequires:  crate(textwrap-0.16) >= 0.16.0
BuildRequires:  crate(walkdir-2/default) >= 2.4.0
BuildRequires:  crate(winapi-util-0.1/default) >= 0.1.6

%description
ripgrep (rg) recursively searches directories for regular expression
matches. It respects ignore files and skips hidden and binary files by
default, and supports PCRE2 patterns, Unicode, and parallel searching.

%install
install -Dpm0755 target/release/rg %{buildroot}%{_bindir}/rg
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
install -d %{buildroot}%{_datadir}/zsh/site-functions
target/release/rg --generate man > %{buildroot}%{_mandir}/man1/rg.1
target/release/rg --generate complete-bash > %{buildroot}%{_datadir}/bash-completion/completions/rg
target/release/rg --generate complete-fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/rg.fish
target/release/rg --generate complete-zsh > %{buildroot}%{_datadir}/zsh/site-functions/_rg

# rust-rpm-macros 0.5 passes BuildOption(check) as test-runner arguments after
# Cargo's -- separator. --workspace and --features are Cargo options, so pass
# them before the separator with an explicit command. Test the pcre2 build.
%check
cargo test --offline --workspace --features pcre2

%files
%doc README.md CHANGELOG.md FAQ.md GUIDE.md
%license COPYING LICENSE-MIT UNLICENSE
%{_bindir}/rg
%{_mandir}/man1/rg.1*
%{_datadir}/bash-completion/completions/rg
%{_datadir}/fish/vendor_completions.d/rg.fish
%{_datadir}/zsh/site-functions/_rg

%changelog
%autochangelog
