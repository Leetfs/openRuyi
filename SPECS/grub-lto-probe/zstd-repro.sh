#!/usr/bin/bash
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

set -eu

archive=$1
target=$2
flags=$3
output=$(pwd)
mkdir -p zstd-evidence
gcc -v > zstd-evidence/compiler.txt 2>&1
printf '%s\n' "$flags" > zstd-evidence/optflags.txt
printf '%s\n' "$target" > zstd-evidence/target.txt

for mode in on off; do
    directory="$output/zstd-$mode"
    mkdir "$directory"
    tar -xJf "$archive" --strip-components=1 -C "$directory"
    if test "$mode" = on; then
        mode_flags="$flags"
    else
        mode_flags="$flags -fno-lto"
    fi
    (
        cd "$directory"
        autoreconf -fiv > autoreconf.log 2>&1 || {
            cat autoreconf.log
            exit 1
        }
        CFLAGS="$mode_flags" ./configure \
            --with-platform=efi \
            --target="$target" \
            --enable-stack-protector=strong \
            --disable-werror > configure.log 2>&1 || {
            tail -n 80 configure.log
            exit 1
        }
        status=0
        make -C grub-core -j1 V=1 \
            CFLAGS="$mode_flags -save-temps=obj" zstd.module > build.log 2>&1 || status=$?
        printf '%s\n' "$status" > exit-status
    )
    tail -n 12 "$directory/build.log"
    mkdir "zstd-evidence/$mode"
    cp "$directory/"{autoreconf.log,configure.log,config.log,build.log,exit-status} \
        "zstd-evidence/$mode/"
    cp "$directory/grub-core/lib/zstd/"*.i "$directory/grub-core/lib/zstd/"*.o \
        "zstd-evidence/$mode/"
    find "$directory/grub-core" -maxdepth 1 -type f -name 'zstd.module*' \
        -exec cp {} "zstd-evidence/$mode/" \;
    python3 - "$directory/build.log" "zstd-evidence/$mode/relink.sh" <<'PY'
from pathlib import Path
import shlex
import sys

for line in Path(sys.argv[1]).read_text().splitlines():
    if not line.startswith('gcc '):
        continue
    arguments = shlex.split(line)
    if not arguments or arguments[0] != 'gcc' or '-o' not in arguments:
        continue
    if arguments[arguments.index('-o') + 1] != 'zstd.module':
        continue
    arguments = [
        Path(argument).name if argument.endswith('.o') else argument
        for argument in arguments
    ]
    Path(sys.argv[2]).write_text(
        '#!/usr/bin/bash\nset -eu\ncd "$(dirname "$0")"\n'
        + shlex.join(arguments) + '\n'
    )
    break
else:
    raise SystemExit('Could not find the zstd.module link command')
PY
    relink_status=0
    bash "zstd-evidence/$mode/relink.sh" > "zstd-evidence/$mode/relink.log" 2>&1 || relink_status=$?
    printf '%s\n' "$relink_status" > "zstd-evidence/$mode/relink-exit-status"
    printf 'ZSTD_%s_EXIT=%s\n' "$mode" "$(cat "$directory/exit-status")"
    printf 'ZSTD_%s_RELINK_EXIT=%s\n' "$mode" "$relink_status"
    grep -A 22 -B 2 'internal compiler error' "$directory/build.log" || :
done

cp zstd-repro.sh zstd-evidence/
sha256sum "$archive" > zstd-evidence/source-sha256.txt
cp zstd-on/COPYING zstd-evidence/
tar -cJf zstd-evidence.tar.xz zstd-evidence
