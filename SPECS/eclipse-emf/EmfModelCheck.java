import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.*;
import org.eclipse.emf.ecore.change.util.ChangeRecorder;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;
class EmfModelCheck {
    public static void main(String[] args) throws Exception {
        var f = EcoreFactory.eINSTANCE;
        var model = f.createEPackage();
        model.setName("check"); model.setNsPrefix("c"); model.setNsURI("urn:openruyi:emf-check");
        var type = f.createEClass(); type.setName("Item");
        var label = f.createEAttribute(); label.setName("label"); label.setEType(EcorePackage.Literals.ESTRING);
        type.getEStructuralFeatures().add(label); model.getEClassifiers().add(type);
        var object = model.getEFactoryInstance().create(type); object.eSet(label, "before");
        var recorder = new ChangeRecorder(object);
        object.eSet(label, "after"); var changes = recorder.endRecording(); recorder.dispose();
        changes.applyAndReverse();
        if (!"before".equals(object.eGet(label))) throw new AssertionError("undo");
        changes.applyAndReverse();
        var resources = new ResourceSetImpl();
        resources.getPackageRegistry().put(model.getNsURI(), model);
        resources.getResourceFactoryRegistry().getExtensionToFactoryMap().put("xmi", new XMIResourceFactoryImpl());
        var saved = resources.createResource(URI.createURI("memory:/saved.xmi")); saved.getContents().add(object);
        var output = new ByteArrayOutputStream(); saved.save(output, Map.of());
        if (!output.toString(StandardCharsets.UTF_8).contains("after")) throw new AssertionError("serialize");
        var loaded = resources.createResource(URI.createURI("memory:/loaded.xmi"));
        loaded.load(new ByteArrayInputStream(output.toByteArray()), Map.of());
        if (!"after".equals(loaded.getContents().get(0).eGet(label))) throw new AssertionError("XMI round trip");
        System.out.println("EMF dynamic model, change undo/redo, XMI save and load passed");
    }
}
