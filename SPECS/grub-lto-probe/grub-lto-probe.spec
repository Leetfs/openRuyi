# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           grub-lto-probe
Version:        1.0
Release:        %autorelease
Summary:        Linker wrapping behavior with LTO
License:        MulanPSL-2.0 AND GPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/Leetfs/openRuyi
VCS:            git:https://github.com/Leetfs/openRuyi.git
# Reduced cross-translation-unit wrapping example for the TPCM test failure.
Source0:        real.c
Source1:        caller.c
Source2:        main.c
Source3:        LICENSE
Source4:        zstd-repro.sh
#!RemoteAsset:  sha256:f0db0104927df0b9a48bc41b735c702936190d17eb2d73d3018fa77474a0cabe
Source5:        https://gitlab.freedesktop.org/api/v4/projects/26558/packages/generic/source-assets/grub-2.16/grub-2.16.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  python3

%description
This diagnostic compares GNU linker symbol wrapping with and without
GCC link-time optimization and reproduces the GRUB zstd module link failure.

%prep
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
gcc -v
rpm -qf "$(readlink -f "$(command -v gcc)")"
rpm -qf "$(readlink -f "$(command -v ld)")"
for mode in off on; do
    mkdir "$mode"
    if test "$mode" = on; then
        lto_flag=-flto
    else
        lto_flag=-fno-lto
    fi
    for source in real caller main; do
        gcc -O2 -g "$lto_flag" -c "$source.c" -o "$mode/$source.o"
    done
    gcc -O2 -g "$lto_flag" -Wl,--wrap=target "$mode/"*.o -o "wrap-$mode"
    objdump -dr "wrap-$mode" > "wrap-$mode.disassembly"
done
bash zstd-repro.sh %{SOURCE5} %{_arch} "%{optflags}"

%check
# Compare the wrapped function's exit status with the real function's value.
./wrap-off
status=0
./wrap-on || status=$?
printf 'WRAP_OFF_EXIT=0\nWRAP_ON_EXIT=%s\n' "$status" | tee results.txt
test "$status" -eq 0 || test "$status" -eq 42
# Check the reduced module build against its non-LTO control.
test "$(cat zstd-off/exit-status)" -eq 0
test "$(cat zstd-evidence/off/relink-exit-status)" -eq 0
%ifarch x86_64
test "$(cat zstd-on/exit-status)" -ne 0
grep -q 'ipa_merge_modref_summary_after_inlining' zstd-on/build.log
test "$(cat zstd-evidence/on/relink-exit-status)" -ne 0
grep -q 'ipa_merge_modref_summary_after_inlining' zstd-evidence/on/relink.log
%endif

%install
install -Dm0755 -t %{buildroot}%{_libexecdir}/%{name} wrap-off wrap-on

%files
%doc *.c results.txt *.disassembly zstd-repro.sh zstd-evidence.tar.xz
%license LICENSE zstd-on/COPYING
%{_libexecdir}/grub-lto-probe/

%changelog
%autochangelog
