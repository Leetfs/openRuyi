// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import bsh.Interpreter;
import java.io.File;
class CheckInvoker {
    public static void main(String[] args) throws Exception {
        var i = new Interpreter();
        i.set("basedir", new File(args[0]));
        i.set("localRepositoryPath", new File(args[1]));
        Object result = i.source(args[0] + "/verify.bsh");
        if (Boolean.FALSE.equals(result)) throw new AssertionError("verify.bsh returned false");
    }
}
