// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;
import org.objectweb.asm.tools.Retrofitter;
class RetrofitModule {
    public static void main(String[] args) throws Exception {
        var tool = new Retrofitter();
        tool.retrofit(Path.of(args[0]), args[1]);
        tool.verify(Path.of(args[0]), args[1], Arrays.asList(args[2].split(",")),
                    args.length == 4 ? Arrays.asList(args[3].split(",")) : Collections.emptyList());
    }
}
