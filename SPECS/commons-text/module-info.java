// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0

module org.apache.commons.text {
    requires java.scripting;
    requires java.xml;
    requires org.apache.commons.lang3;

    exports org.apache.commons.text;
    exports org.apache.commons.text.diff;
    exports org.apache.commons.text.io;
    exports org.apache.commons.text.lookup;
    exports org.apache.commons.text.matcher;
    exports org.apache.commons.text.numbers;
    exports org.apache.commons.text.similarity;
    exports org.apache.commons.text.translate;
}
