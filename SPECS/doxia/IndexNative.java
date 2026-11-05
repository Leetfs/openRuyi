// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0

import java.io.File;
import java.net.URL;
import java.net.URLClassLoader;
import org.eclipse.sisu.space.SisuIndex;
import org.eclipse.sisu.space.URLClassSpace;
class IndexNative {
    public static void main(String[] args) throws Exception {
        File classes = new File(args[0]);
        URL[] urls = { classes.toURI().toURL() };
        try (URLClassLoader loader = new URLClassLoader(urls, IndexNative.class.getClassLoader())) {
            new SisuIndex(classes).index(new URLClassSpace(loader, urls));
        }
    }
}
