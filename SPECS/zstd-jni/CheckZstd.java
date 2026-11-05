// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import com.github.luben.zstd.*;
import java.io.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.security.MessageDigest;
class CheckZstd {
    private static void same(byte[] expected, byte[] actual) {
        if (!Arrays.equals(expected, actual)) throw new AssertionError("Data differs");
    }
    public static void main(String[] args) throws Exception {
        byte[] payload = Files.readAllBytes(Path.of(args[0], "xml"));
        for (int level : new int[] {-5, 0, 1, 3, 9, 19}) {
            byte[] compressed = Zstd.compress(payload, level);
            same(payload, Zstd.decompress(compressed, payload.length));
        }
        for (String file : new String[] {"xml-1.zst", "xml-3.zst", "xml-6.zst", "xml-9.zst"}) {
            try (var stream = new ZstdInputStream(Files.newInputStream(Path.of(args[0], file)))) {
                same(payload, stream.readAllBytes());
            }
        }
        var direct = java.nio.ByteBuffer.allocateDirect(payload.length);
        direct.put(payload).flip();
        var packed = java.nio.ByteBuffer.allocateDirect(Math.toIntExact(Zstd.compressBound(payload.length)));
        Zstd.compress(packed, direct, 3);
        packed.flip();
        var restored = java.nio.ByteBuffer.allocateDirect(payload.length);
        Zstd.decompress(restored, packed);
        restored.flip();
        byte[] decoded = new byte[restored.remaining()];
        restored.get(decoded);
        same(payload, decoded);
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        try (var stream = new ZstdOutputStream(bytes).setLevel(7)) { stream.write(payload); }
        try (var stream = new ZstdInputStream(new ByteArrayInputStream(bytes.toByteArray()))) {
            same(payload, stream.readAllBytes());
        }
        byte[][] samples = new byte[512][];
        for (int i = 0; i < samples.length; i++)
            samples[i] = ("<record><id>" + i + "</id><name>openRuyi source build</name><value>"
                + (i * 37) + "</value><description>dictionary regression data</description></record>")
                .getBytes(StandardCharsets.UTF_8);
        for (boolean legacy : new boolean[] {false, true}) {
            for (int level : new int[] {0, 7}) {
                byte[] buffer = new byte[2048];
                long size = Zstd.trainFromBuffer(samples, buffer, legacy, level);
                if (Zstd.isError(size)) throw new AssertionError(Zstd.getErrorName(size));
                byte[] dict = Arrays.copyOf(buffer, Math.toIntExact(size));
                byte[] compressed = Zstd.compressUsingDict(samples[271], dict, 5);
                same(samples[271], Zstd.decompress(compressed, dict, samples[271].length));
                System.out.println("dictionary " + legacy + " " + level + " " + HexFormat.of().formatHex(
                    MessageDigest.getInstance("SHA-256").digest(dict)));
            }
        }
        try {
            Zstd.decompress(new byte[] {1, 2, 3, 4}, 100);
            throw new AssertionError("Invalid compressed data accepted");
        } catch (ZstdException expected) { }
        System.out.println("Byte arrays, streams, upstream frames, dictionaries and invalid input passed");
    }
}
