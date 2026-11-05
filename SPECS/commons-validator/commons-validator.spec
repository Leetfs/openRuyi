# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-validator
Version:        1.11.0
Release:        %autorelease
Summary:        Reusable validation routines and XML validation rules for Java
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-validator/
VCS:            git:https://github.com/apache/commons-validator.git
#!RemoteAsset:  sha256:a9396cc16e1e2096e9cab6bbe07ee64c5bfa0f5eed101ee12985bca7c3e71445
Source0:        https://downloads.apache.org/commons/validator/source/commons-validator-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  commons-beanutils
BuildRequires:  commons-collections3
BuildRequires:  commons-digester2
BuildRequires:  java-25-openjdk-devel
BuildRequires:  slf4j-jcl
BuildRequires:  slf4j-jdk14

Requires:       commons-beanutils
Requires:       commons-collections3
Requires:       commons-digester2
Requires:       java-25-openjdk-headless
Requires:       slf4j-jcl

%description
Commons Validator provides reusable checks for URLs, email addresses,
numbers and other data. Its XML-configured validation engine applies
custom rules to JavaBean properties. ODFDOM uses its URL validator when
extracting RDF metadata.

%prep
%autosetup -n commons-validator-%{version}-src
find . -type f -name '*.jar' -delete

%build
# Build the library with the existing Commons APIs and logging bridge.
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
deps=%{_datadir}/java/commons-beanutils.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/commons-digester2.jar:%{_datadir}/java/jcl-over-slf4j.jar
javac --release 8 -encoding UTF-8 -cp "$deps" -d classes @sources.list
cp -a src/main/resources/. classes/
cat > validator.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}
Class-Path: commons-beanutils.jar commons-collections3.jar
  commons-digester2.jar jcl-over-slf4j.jar

MANIFEST
jar --create --file commons-validator.jar --manifest validator.mf -C classes .

%install
install -Dpm644 commons-validator.jar %{buildroot}%{_datadir}/java/commons-validator.jar

%check
# Cover ODFDOM's URL check and the XML/Digester/BeanUtils validation path.
# The separate Maven test suite also needs Jupiter, Pioneer and classpath fixtures.
cat > CheckValidator.java <<'JAVA'
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;
import org.apache.commons.beanutils.PropertyUtils;
import org.apache.commons.validator.Field;
import org.apache.commons.validator.Validator;
import org.apache.commons.validator.ValidatorResources;
import org.apache.commons.validator.ValidatorResult;
import org.apache.commons.validator.routines.EmailValidator;
import org.apache.commons.validator.routines.UrlValidator;
public class CheckValidator {
    public static class Answer {
        private final int value;
        public Answer(int value) { this.value = value; }
        public int getValue() { return value; }
    }
    public static boolean validateAnswer(Object bean, Field field) throws Exception {
        return Integer.valueOf(42).equals(PropertyUtils.getProperty(bean, field.getProperty()));
    }
    public static void main(String[] args) throws Exception {
        UrlValidator urls = new UrlValidator();
        if (!urls.isValid("https://openruyi.cn/docs/")
                || urls.isValid("javascript:alert(1)"))
            throw new AssertionError("URL validation");
        if (!EmailValidator.getInstance().isValid("user@example.org")
                || EmailValidator.getInstance().isValid("not an address"))
            throw new AssertionError("Email validation");
        String xml = "<?xml version=\"1.0\"?>"
                + "<!DOCTYPE form-validation PUBLIC "
                + "\"-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.4.0//EN\" "
                + "\"https://commons.apache.org/dtds/validator_1_4_0.dtd\">"
                + "<form-validation><global>"
                + "<validator name=\"answer\" classname=\"CheckValidator\" "
                + "method=\"validateAnswer\" methodParams=\"java.lang.Object,org.apache.commons.validator.Field\" "
                + "msg=\"answer.invalid\"/></global><formset><form name=\"answer\">"
                + "<field property=\"value\" depends=\"answer\"/></form></formset></form-validation>";
        ValidatorResources resources = new ValidatorResources(
                new ByteArrayInputStream(xml.getBytes(StandardCharsets.UTF_8)));
        for (int value : new int[] {42, 41}) {
            Validator validator = new Validator(resources, "answer");
            validator.setParameter(Validator.BEAN_PARAM, new Answer(value));
            ValidatorResult result = validator.validate().getValidatorResult("value");
            if (result == null || result.isValid("answer") != (value == 42))
                throw new AssertionError("XML validation rule for " + value);
        }
    }
}
JAVA
deps=commons-validator.jar:%{_datadir}/java/commons-beanutils.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/commons-digester2.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar
javac --release 8 -encoding UTF-8 -cp "$deps" CheckValidator.java
java -cp ".:$deps" CheckValidator

%files
%license LICENSE.txt NOTICE.txt
%doc README.md RELEASE-NOTES.txt
%{_datadir}/java/commons-validator.jar

%changelog
%autochangelog
