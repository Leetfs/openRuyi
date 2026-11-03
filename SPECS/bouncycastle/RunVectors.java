package org.bouncycastle.crypto.test;

import org.bouncycastle.util.test.Test;
import org.bouncycastle.util.test.TestResult;

class RunVectors {
    public static void main(String[] args) {
        for (Test test : new Test[]{new SHA256DigestTest(), new AESTest()}) {
            TestResult result = test.perform();
            if (!result.isSuccessful()) {
                throw new AssertionError(result.toString(), result.getException());
            }
            System.out.println(result);
        }
    }
}
