#!/usr/bin/python3
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Select installed OSGi bundles and start the services used by the headless PDE model."""
from email import message_from_bytes
from pathlib import Path
import sys
from zipfile import ZipFile

repo, built = map(Path, sys.argv[1:])
start = (
    "org.osgi.util.function org.osgi.util.promise org.osgi.service.component org.osgi.service.prefs "
    "org.apache.felix.scr org.eclipse.equinox.common org.eclipse.core.jobs org.eclipse.equinox.registry "
    "org.eclipse.equinox.preferences org.eclipse.equinox.app org.eclipse.core.contenttype "
    "org.eclipse.core.runtime org.eclipse.core.expressions org.eclipse.core.variables org.eclipse.ant.core "
    "org.eclipse.core.filesystem org.eclipse.core.resources org.eclipse.pde.core org.eclipse.pde.api.tools"
).split()
files = {}
for root in (repo, built):
    for jar in sorted(root.rglob("*.jar")):
        if jar.name.endswith(("-sources.jar", "-javadoc.jar", "-tests.jar")):
            continue
        with ZipFile(jar) as archive:
            if "META-INF/MANIFEST.MF" not in archive.namelist():
                continue
            manifest = message_from_bytes(archive.read("META-INF/MANIFEST.MF").replace(b"\r\n ", b"").replace(b"\n ", b""))
        name = manifest.get("Bundle-SymbolicName", "").split(";")[0]
        version = manifest.get("Bundle-Version")
        if name and name != "org.eclipse.osgi" and version:
            files[name, version] = jar.resolve()
started = {}
for (name, version), jar in sorted(files.items()):
    if name in start:
        if name in started:
            raise ValueError(f"Multiple installed versions of startup bundle {name}")
        started[name] = jar
    else:
        print("install", jar)
for name in start:
    print("start", started[name])
