import java.io.File;
import java.util.Map;
import org.apache.maven.model.Model;
import org.apache.maven.model.building.ModelProcessor;
import org.apache.maven.model.building.StringModelSource;
import org.codehaus.plexus.DefaultContainerConfiguration;
import org.codehaus.plexus.DefaultPlexusContainer;
import org.codehaus.plexus.PlexusConstants;
import org.sonatype.maven.polyglot.mapping.Mapping;

class PolyglotCheck {
    public static void main(String[] args) throws Exception {
        var config = new DefaultContainerConfiguration().setClassPathScanning(PlexusConstants.SCANNING_INDEX).setAutoWiring(true);
        var container = new DefaultPlexusContainer(config);
        try {
            Mapping mapping = container.lookup(Mapping.class, "xml");
            if (!mapping.accept(Map.of(ModelProcessor.SOURCE, new StringModelSource("<project/>")))) {
                throw new AssertionError("XML source was rejected");
            }
            Model model = mapping.getReader().read(new File(args[0]), Map.of());
            if (!"a".equals(model.getParent().getGroupId()) || !"b".equals(model.getParent().getArtifactId())
                    || !"c".equals(model.getParent().getVersion())) {
                throw new AssertionError("Unexpected upstream fixture parent " + model.getParent());
            }
        } finally {
            container.dispose();
        }
    }
}
