// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
package org.eclipse.compare.internal.merge;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import org.eclipse.compare.rangedifferencer.IRangeComparator;
class LineFixtures {
    static IRangeComparator lines(String data) {
        try {
            return new LineComparator(new ByteArrayInputStream(data.getBytes(StandardCharsets.UTF_8)), "UTF-8");
        } catch (IOException ex) {
            throw new AssertionError(ex);
        }
    }
}
