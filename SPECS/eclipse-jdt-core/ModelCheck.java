import org.eclipse.jdt.core.dom.AST;
import org.eclipse.jdt.core.dom.ASTParser;
import org.eclipse.jdt.core.dom.CompilationUnit;
import org.eclipse.jdt.core.dom.MethodDeclaration;
import org.eclipse.jdt.core.dom.TypeDeclaration;
class ModelCheck {
    public static void main(String[] args) {
        var parser = ASTParser.newParser(AST.JLS17);
        parser.setSource("class Answer { int value() { return 42; } }".toCharArray());
        var root = (CompilationUnit) parser.createAST(null);
        if (root.getProblems().length != 0 || root.types().size() != 1) throw new AssertionError();
        var type = (TypeDeclaration) root.types().get(0);
        MethodDeclaration method = type.getMethods()[0];
        if (!"Answer".equals(type.getName().getIdentifier()) || !"value".equals(method.getName().getIdentifier())
                || method.getBody().statements().size() != 1) throw new AssertionError("Unexpected syntax tree");
    }
}
