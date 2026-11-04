#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
launcher=$(realpath "$1")
framework=$(realpath "$2")
fixture=$(realpath "$3")
shift 3
state=$PWD/build/director-check
configuration=$state/configuration
installation=$state/installation
mkdir -p "$configuration" "$installation"
entries=()
for jar do
    uri=reference:file:$(realpath "$jar")
    case "$jar" in
        */org.eclipse.osgi.compatibility.state-*.jar) entries+=("$uri");;
        *) entries+=("$uri@start");;
    esac
done
(IFS=,; printf 'osgi.bundles=%s\nosgi.bundles.defaultStartLevel=4\n' "${entries[*]}") > "$configuration/config.ini"
director() {
    java -Dosgi.framework="file:$framework" -jar "$launcher" -nosplash -consoleLog \
        -configuration "$configuration" -data "$state/workspace" \
        -application org.eclipse.equinox.p2.director \
        -destination "$installation" -profile native "$@" || {
        find "$state" -type f -name '*.log' -exec cat {} +
        return 1
    }
}
director -repository "file:$fixture/" -installIU zFeature.feature.group -roaming
plugin=plugins/zzz_1.0.0.jar
cmp "$fixture/$plugin" "$installation/$plugin"
director -listInstalledRoots | tee "$state/roots.txt"
grep -Fx 'zFeature.feature.group/1.0.0' "$state/roots.txt"
director -repository "file:$fixture/" -uninstallIU zFeature.feature.group
test ! -e "$installation/$plugin"
director -listInstalledRoots > "$state/roots-after-uninstall.txt"
if grep -Fxq 'zFeature.feature.group/1.0.0' "$state/roots-after-uninstall.txt"; then exit 1; fi
echo 'Equinox director installed the feature and its required plugin, then removed them'
