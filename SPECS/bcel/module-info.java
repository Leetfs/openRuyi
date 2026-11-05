module org.apache.bcel {
    requires java.desktop;
    requires org.apache.commons.io;
    requires org.apache.commons.lang3;

    exports org.apache.bcel;
    exports org.apache.bcel.classfile;
    exports org.apache.bcel.generic;
    exports org.apache.bcel.util;
    exports org.apache.bcel.verifier;
    exports org.apache.bcel.verifier.exc;
    exports org.apache.bcel.verifier.statics;
    exports org.apache.bcel.verifier.structurals;
}
