import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.Platform;
import com.sun.jna.platform.linux.LibC;
class JnaCheck {
    interface ProcessLibrary extends Library { int getpid(); }
    public static void main(String[] args) {
        var libc = Native.load(Platform.C_LIBRARY_NAME, ProcessLibrary.class);
        if (libc.getpid() != ProcessHandle.current().pid()) throw new AssertionError("Incorrect native PID");
        var info = new LibC.Sysinfo();
        if (LibC.INSTANCE.sysinfo(info) != 0 || info.totalram.longValue() <= 0) throw new AssertionError("sysinfo");
    }
}
