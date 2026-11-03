import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import org.codehaus.mojo.animal_sniffer.Clazz;
import org.codehaus.mojo.animal_sniffer.SignatureChecker;

class CheckSignature {
    public static void main(String[] args) throws Exception {
        try (InputStream input = Files.newInputStream(Path.of(args[0]))) {
            Map<String, Clazz> classes = SignatureChecker.loadClasses(input);
            int members = classes.values().stream().mapToInt(c -> c.getSignatures().size()).sum();
            Clazz string = classes.get("java/lang/String");
            if (classes.size() != 20166 || members != 258983 || string == null
                    || !string.getSignatures().contains("length()I")
                    || string.getSignatures().contains("strip()Ljava/lang/String;")
                    || !classes.containsKey("java/time/LocalDate")) {
                throw new AssertionError("Unexpected Java 8 API signature contents");
            }
            System.out.printf("Read %,d classes and %,d members%n", classes.size(), members);
        }
    }
}
