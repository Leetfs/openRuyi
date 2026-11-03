"""Run virtualenv's seed security tests against openRuyi's RPM wheel layout."""
import re
import sys
import tarfile
from pathlib import Path

tests = Path("tests/unit")
for path in (tests / "create/test_creator.py", tests / "seed/embed/test_bootstrap_link_via_app_data.py",
             tests / "seed/embed/test_pip_invoke.py"):
    source = path.read_text()
    # The distribution's seed source is "bundle"; "embed" deliberately raises.
    source = re.sub(r'("--(?:pip|setuptools|wheel)",\s*)"embed"', r'\1"bundle"', source)
    path.write_text(source)

# The reseed test needs a second pip version in its explicit extra-search-dir.
fixtures = Path(".rpm-seed-fixtures")
fixtures.mkdir(exist_ok=True)
with tarfile.open(sys.argv[1]) as archive:
    for member in archive:
        if "/seed/wheels/embed/pip-" in member.name and member.name.endswith(".whl") and member.isfile():
            (fixtures / Path(member.name).name).write_bytes(archive.extractfile(member).read())
path = tests / "seed/embed/test_pip_invoke.py"
source = path.read_text()
assert source.count("str(BUNDLE_FOLDER)") == 1
source = source.replace("import os\n", "import os\nfrom pathlib import Path\n")
source = source.replace("if TYPE_CHECKING:", 'BUNDLE_FOLDER_FIXTURES = Path.cwd() / ".rpm-seed-fixtures"\nSYSTEM_PIP_WHEEL, = Path("/usr/share/python-wheels").glob("pip-*.whl")\n\nif TYPE_CHECKING:')
source = source.replace('get_embed_wheel("pip", f"{sys.version_info.major}.{sys.version_info.minor}").version',
                        'SYSTEM_PIP_WHEEL.name.split("-")[1]')
source = source.replace('BUNDLE_SUPPORT[f"{sys.version_info.major}.{sys.version_info.minor}"]["pip"].split("-")[1]',
                        'SYSTEM_PIP_WHEEL.name.split("-")[1]')
path.write_text(source.replace("str(BUNDLE_FOLDER)", 'str(BUNDLE_FOLDER_FIXTURES)'))

# RPM owns installed files; openRuyi removes wheel RECORD from dist-info.
path = tests / "config/test___main__.py"
source = path.read_text()
old = 'for root in {file.parts[0] for file in metadata.files or () if file.parts[0] not in {"..", "__pycache__"}}:'
new = old[:-1] + ' or {name.replace("-", "_"), Path(str(metadata._path)).name}:'
assert source.count(old) == 1
path.write_text(source.replace(old, new))

path = tests / "seed/embed/test_bootstrap_link_via_app_data.py"
source = path.read_text()
old = 'BUNDLE_FOLDER / BUNDLE_SUPPORT[session.interpreter.version_release_str]["pip"]'
assert source.count(old) == 1
path.write_text(source.replace(old, 'next(Path("/usr/share/python-wheels").glob("pip-*.whl"))'))
