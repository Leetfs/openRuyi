// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.lang.reflect.Proxy;
import org.eclipse.core.filebuffers.ITextFileBuffer;
import org.eclipse.core.filebuffers.manipulation.ConvertLineDelimitersOperation;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.jface.text.Document;
class FileBufferCheck extends ConvertLineDelimitersOperation {
    FileBufferCheck() { super("\n"); }
    public static void main(String[] args) throws Exception {
        var doc = new Document("first\r\nsecond\nthird");
        var buffer = (ITextFileBuffer)Proxy.newProxyInstance(FileBufferCheck.class.getClassLoader(),
            new Class<?>[]{ITextFileBuffer.class}, (proxy, method, values) -> {
                if (method.getName().equals("getDocument")) return doc;
                throw new UnsupportedOperationException(method.getName());
            });
        var operation = new FileBufferCheck();
        var edits = operation.computeTextEdit(buffer, new NullProgressMonitor());
        if (edits == null) throw new AssertionError("No edits for mixed delimiters");
        edits.apply(doc, new NullProgressMonitor());
        if (!doc.get().equals("first\nsecond\nthird") || operation.computeTextEdit(buffer, new NullProgressMonitor()) != null)
            throw new AssertionError(doc.get());
    }
}
