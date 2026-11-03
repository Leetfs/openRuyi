#!/usr/bin/python3
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
"""Build the EMF source bundle for a release-qualified binary bundle."""
import os
from datetime import datetime, timezone
from email import message_from_string
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

module, output = map(Path, sys.argv[1:])
manifest = message_from_string((module / "META-INF/MANIFEST.MF").read_text().replace("\n ", ""))
name = manifest["Bundle-SymbolicName"].split(";")[0]
version = manifest["Bundle-Version"]
if name != module.name or version.endswith(".qualifier"):
    raise ValueError(f"Missing release coordinates in {module}")
build = re.sub(r"\\\r?\n[ \t]*", "", (module / "build.properties").read_text())
entries = dict(line.split("=", 1) for line in build.splitlines() if "=" in line and not line.lstrip().startswith("#"))
entries = {key.strip(): value.strip() for key, value in entries.items()}
translations = dict(line.split("=", 1) for line in (module / "plugin.properties").read_text().splitlines()
                    if "=" in line and not line.lstrip().startswith("#"))
translations = {key.strip(): value.strip() for key, value in translations.items()}

output.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(dir=output.parent) as work:
    root = Path(work) / "content"
    for folder in entries["source.."].split(","):
        shutil.copytree(module / folder.strip(), root, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("*.class", ".gitignore"))
    for pattern in entries["src.includes"].split(","):
        for source in module.glob(pattern.strip()):
            if source.is_file():
                target = root / source.relative_to(module)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
    messages = root / "OSGI-INF/l10n/bundle-src.properties"
    messages.parent.mkdir(parents=True, exist_ok=True)
    messages.write_text(f"bundleName={translations['pluginName']} Source\nbundleVendor={translations['providerName']}\n")
    mf = Path(work) / "source.mf"
    mf.write_text(f"""Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: {name}.source
Bundle-Version: {version}
Eclipse-SourceBundle: {name};version="{version}";roots:="."
Bundle-Name: %bundleName
Bundle-Vendor: %bundleVendor
Bundle-Localization: OSGI-INF/l10n/bundle-src
""")
    command = ["jar", "--create", "--file", str(output), "--manifest", str(mf)]
    if "SOURCE_DATE_EPOCH" in os.environ:
        timestamp = datetime.fromtimestamp(int(os.environ["SOURCE_DATE_EPOCH"]), timezone.utc)
        command.extend(["--date", timestamp.isoformat(timespec="seconds")])
    subprocess.run(command + ["-C", str(root), "."], check=True)
