// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.io.File;
import org.eclipse.pde.core.target.TargetBundle;
import org.eclipse.pde.core.target.TargetFeature;

public class PdeTargetCheck {
    public static void main(String[] args) throws Exception {
        var bundle = new TargetBundle(new File(args[0]));
        var info = bundle.getBundleInfo();
        if (!info.getSymbolicName().equals("org.eclipse.pde.build")
                || !info.getVersion().equals("3.12.900") || bundle.isSourceBundle()) {
            throw new AssertionError("Unexpected target bundle: " + info);
        }
        var feature = new TargetFeature(new File(args[1]));
        if (!"org.openruyi.check".equals(feature.getId()) || !"1.2.3".equals(feature.getVersion())) {
            throw new AssertionError("Unexpected target feature: " + feature);
        }
        System.out.println("PDE target read org.eclipse.pde.build 3.12.900 and feature org.openruyi.check 1.2.3");
    }
}
