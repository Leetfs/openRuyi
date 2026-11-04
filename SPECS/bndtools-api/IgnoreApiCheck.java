// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import org.bndtools.versioncontrol.ignores.manager.VersionControlIgnoresManagerImpl;
class IgnoreApiCheck {
    public static void main(String[] args) throws Exception {
        var manager=new VersionControlIgnoresManagerImpl();
        if (!"/build/generated/".equals(manager.sanitiseGitIgnoreGlob(true, " //build///generated/ ", true)))
            throw new AssertionError("Rooted directory glob");
        if (!"classes".equals(manager.sanitiseGitIgnoreGlob(false, "/classes/", false)))
            throw new AssertionError("Unrooted file glob");
        if (!manager.getAllPluginsInformation().isEmpty()) throw new AssertionError("Unexpected provider");
        Class<?> api=Class.forName("org.bndtools.versioncontrol.ignores.manager.api.VersionControlIgnoresManager");
        if (!api.isInstance(manager)) throw new AssertionError("Manager did not implement its released API");
    }
}
