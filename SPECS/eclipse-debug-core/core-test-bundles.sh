#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu
repo=/usr/share/maven-repository; platform=$repo/org/eclipse/platform; osgi=$repo/org/osgi
for pair in org.osgi.util.function/1.2.0 org.osgi.util.promise/1.3.0 org.osgi.service.component/1.5.1 org.osgi.service.prefs/1.1.2; do
 n=${pair%/*}; printf 'start %s/%s/%s-%s.jar\n' "$osgi" "$pair" "$n" "${pair#*/}"
done
printf 'start %s\n' "$repo/org/apache/felix/org.apache.felix.scr/2.2.18/org.apache.felix.scr-2.2.18.jar"
for pair in org.eclipse.equinox.common/3.20.300 org.eclipse.core.jobs/3.15.700 org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 org.eclipse.core.contenttype/3.9.800 org.eclipse.core.runtime/3.34.200; do
 n=${pair%/*}; printf 'start %s/%s/%s-%s.jar\n' "$platform" "$pair" "$n" "${pair#*/}"
done
for n in jna jna-platform; do printf 'start %s/net/java/dev/jna/%s/5.18.1/%s-5.18.1.jar\n' "$repo" "$n" "$n"; done
for n in org.eclipse.core.expressions org.eclipse.core.variables org.eclipse.ant.core org.eclipse.core.filesystem org.eclipse.core.resources; do
 f=$(find "$platform/$n" -type f -name "$n-*.jar" ! -name '*-sources.jar' | head -1); printf 'start %s\n' "$f"
done
