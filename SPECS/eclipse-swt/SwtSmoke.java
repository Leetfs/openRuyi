import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.*;
class SwtSmoke {
    public static void main(String[] args) {
        var display = new Display();
        try {
            var shell = new Shell(display);
            var input = new Text(shell, SWT.SINGLE);
            input.setText("openRuyi SWT");
            shell.setSize(220, 80);
            shell.open();
            boolean[] invoked = {false};
            display.asyncExec(() -> {invoked[0] = input.getText().equals("openRuyi SWT"); shell.dispose();});
            while (!shell.isDisposed()) if (!display.readAndDispatch()) display.sleep();
            if (!invoked[0]) throw new AssertionError("GTK display event");
            System.out.println("GTK "+SWT.getPlatform()+" display event passed for SWT "+SWT.getVersion());
        } finally {display.dispose();}
    }
}
