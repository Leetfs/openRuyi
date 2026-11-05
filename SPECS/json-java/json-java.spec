# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           json-java
Version:        20260814
Release:        %autorelease
Summary:        Reference JSON parser and object model for Java
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/stleary/JSON-java
VCS:            git:https://github.com/stleary/JSON-java.git
#!RemoteAsset:  sha256:395e5e9c22a8265365a6a6a5bb724e66544177d01bc28516395fcdb1df112862
Source0:        https://github.com/stleary/JSON-java/archive/refs/tags/%{version}.tar.gz#/JSON-java-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4

Requires:       java-25-openjdk-headless

%description
JSON-java provides the org.json parser, JSON objects and arrays, streaming
writers and conversions between JSON, XML, HTTP headers and CSV data.

%prep
%autosetup -n JSON-java-%{version}
find . -type f -name '*.jar' -delete

%build
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
cat > json.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}
Automatic-Module-Name: org.json

MANIFEST
jar --create --file json.jar --manifest json.mf -C classes .

%install
install -Dpm644 json.jar %{buildroot}%{_datadir}/java/json.jar

%check
# Run the upstream parser, number, pointer, record, XML and conversion tests.
# Five integration test classes require JsonPath or Mockito; those integrations
# are excluded here. Object/array mutations used by ODFDOM are checked below.
mkdir test-classes
find src/test -name '*.java' \
    ! -name CookieListTest.java ! -name EnumTest.java ! -name JSONArrayTest.java \
    ! -name JSONObjectTest.java ! -name JSONStringerTest.java | sort > tests.list
cp=json.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
javac --release 17 -encoding UTF-8 -cp "$cp" -d test-classes @tests.list
tests=$(find src/test/java/org/json/junit -maxdepth 1 -name '*Test.java' \
    ! -name CookieListTest.java ! -name EnumTest.java ! -name JSONArrayTest.java \
    ! -name JSONObjectTest.java ! -name JSONStringerTest.java \
    -printf 'org.json.junit.%f\n' | sed 's/\.java$//' | sort)
java -cp "test-classes:src/test/resources:$cp" org.junit.runner.JUnitCore $tests
# Parse, modify and round-trip nested edit operations, and reject incomplete JSON.
cat > CheckEdits.java <<'JAVA'
import org.json.*;
public class CheckEdits {
    public static void main(String[] args) {
        JSONObject doc = new JSONObject("{\"operations\":[{\"insert\":\"中文\",\"position\":21}]}");
        JSONArray operations = doc.getJSONArray("operations");
        operations.getJSONObject(0).put("position", 42);
        operations.put(new JSONObject().put("delete", true));
        if (!new JSONObject(doc.toString()).similar(doc)
                || operations.getJSONObject(0).getInt("position") != 42
                || !operations.getJSONObject(0).getString("insert").equals("中文")
                || !operations.getJSONObject(1).getBoolean("delete"))
            throw new AssertionError("Nested edit operations");
        try { new JSONObject("{\"operations\":["); }
        catch (JSONException expected) { return; }
        throw new AssertionError("Incomplete JSON accepted");
    }
}
JAVA
javac --release 8 -encoding UTF-8 -cp json.jar CheckEdits.java
java -cp .:json.jar CheckEdits

%files
%license LICENSE
%doc README.md
%{_datadir}/java/json.jar

%changelog
%autochangelog
