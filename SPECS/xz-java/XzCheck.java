import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import org.tukaani.xz.LZMA2Options;
import org.tukaani.xz.SeekableFileInputStream;
import org.tukaani.xz.SeekableXZInputStream;
import org.tukaani.xz.XZ;
import org.tukaani.xz.XZInputStream;
import org.tukaani.xz.XZOutputStream;

class XzCheck {
    public static void main(String[] args) throws Exception {
        Path dir = Path.of(args[1]);
        Path data = dir.resolve("payload"), encoded = dir.resolve("java.xz");
        if (args[0].equals("encode")) {
            byte[] bytes = new byte[32768];
            for (int i = 0; i < bytes.length; i++) bytes[i] = (byte) (i * 37 + (i >> 8));
            Files.write(data, bytes);
            try (var out = new XZOutputStream(Files.newOutputStream(encoded), new LZMA2Options(3), XZ.CHECK_CRC64)) {
                out.write(bytes, 0, 8192);
                out.endBlock();
                out.write(bytes, 8192, bytes.length - 8192);
            }
            return;
        }
        byte[] original = Files.readAllBytes(data);
        for (String file : new String[]{"native.xz", "java.xz"}) {
            try (var in = new XZInputStream(Files.newInputStream(dir.resolve(file)))) {
                if (!Arrays.equals(original, in.readAllBytes())) throw new AssertionError(file);
            }
        }
        try (var in = new SeekableXZInputStream(new SeekableFileInputStream(encoded.toFile()))) {
            if (in.length() != original.length || in.getBlockCount() != 2) throw new AssertionError("Bad index");
            in.seek(8190);
            if (!Arrays.equals(in.readNBytes(8), Arrays.copyOfRange(original, 8190, 8198))) {
                throw new AssertionError("Cross-block seek returned wrong data");
            }
        }
        byte[] broken = Files.readAllBytes(encoded);
        try (var in = new XZInputStream(new ByteArrayInputStream(broken, 0, broken.length - 7))) {
            in.readAllBytes();
            throw new AssertionError("Truncated XZ stream accepted");
        } catch (IOException expected) {
            System.out.println("Native and Java streams interoperate; block seek and truncation checks passed");
        }
    }
}
