import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# Failure signatures keep all assertions live and make a different error fatal.
# Numeric widening and BigInteger are part of the 3.x numeric-type changes.
# https://github.com/beanshell/beanshell/commit/7f08518d
# Synthesized super constructors depend on the later class generator.
# https://github.com/beanshell/beanshell/commit/22a6bfd9
# The 2.x fixture for resource closing does not use a resource declaration.
# https://github.com/beanshell/beanshell/commit/bff28804
expected = {
    ("bsh.NumberLiteralTest", "parsing_large_hex_literal"):
        ("failure", "junit.framework.AssertionFailedError", r"^expected:<4278190080> but was:<-16777216>$"),
    ("bsh.NumberLiteralTest", "parsing_very_large_hex_literal"):
        ("error", "bsh.ParseException", r"Number too big for integer type: 0xff00000000000000$"),
    # 2.x does not parse a qualified inner-class creation expression.
    ("bsh.OldScriptsTest", "accessibilityInner.bsh"):
        ("error", "bsh.ParseException", r'^In file: eval stream Encountered "new" at line 6, column 8\.$'),
    ("bsh.OldScriptsTest", "classinner.bsh"):
        ("error", "bsh.EvalError", r"Can't find constructor: global\$(\d+)\( java\.io\.PrintStream \) in class: global\$\1\b"),
    # An assignment from the child namespace updates the interpreter but not
    # its backing Map. The script records every failed assertion in its message.
    ("bsh.OldScriptsTest", "externalNameSpace.bsh"):
        ("failure", "junit.framework.AssertionFailedError", r'^Test FAILED: Line: 31 : assert \( myMap \.get \( "foo" \) == 55 \)  : while evaluating file: eval stream'
                    r'Test FAILED: Line: 34 : assert \( myMap \.get \( "flag" \) instanceof Boolean \)'
                    r'[^:]*: while evaluating file: eval stream expected:<false> but was:<true>$'),
    ("bsh.Project_Coin_Test", "try_with_resource"):
        ("failure", "junit.framework.AssertionFailedError", r"^expected exception$"),
}

source = Path("tests/junitTests/src")
suites = {".".join(p.relative_to(source).with_suffix("").parts) for p in source.rglob("*Test.java")}
reports = {p.name[5:-4]: p for p in Path("tests/junit-reports").glob("TEST-*.xml")}
if not suites or set(reports) != suites:
    sys.exit(f"Missing or unexpected JUnit reports: {sorted(suites ^ set(reports))}")

seen = set()
passed = skipped = xfailed = 0
problems = []
for suite, report in sorted(reports.items()):
    root = ET.parse(report).getroot()
    cases = root.findall("testcase")
    if root.get("name") != suite or len(cases) != int(root.attrib["tests"]):
        problems.append(f"Incomplete JUnit suite: {suite}")
    for case in cases:
        name = case.attrib["name"]
        key = (suite, name)
        full_name = f"{suite}.{name}"
        if key in seen:
            problems.append(f"Duplicate JUnit case: {full_name}")
        seen.add(key)
        errors = [node for node in case if node.tag in {"failure", "error"}]
        if case.find("skipped") is not None:
            skipped += 1
            if key in expected or errors:
                problems.append(f"Expected an executed test: {full_name}")
        elif not errors:
            passed += 1
            if key in expected:
                print(f"XPASS {full_name}")
        else:
            node = errors[0]
            message = node.get("message", "")
            rule = expected.get(key)
            if (len(errors) == 1 and rule and (node.tag, node.get("type")) == rule[:2]
                    and re.search(rule[2], message)):
                xfailed += 1
                print(f"XFAIL {full_name} ({node.get('type')}): {message.splitlines()[0]}")
            else:
                problems.append(f"FAIL {full_name} ({node.tag}, {node.get('type')}): {message}")
for key in sorted(expected.keys() - seen):
    problems.append(f"Missing test: {key}")
print(f"BeanShell JUnit: {passed} passed, {xfailed} expected failures, {skipped} upstream skips")
if problems:
    sys.exit("\n".join(problems))
