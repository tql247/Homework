import java.rmi.*;

public class ImpCal implements Cal {

    public long add (long a, long b) throws RemoteException {
        return Long.sum(a, b);
    }

    public long sub (long a, long b) throws RemoteException {
        return a - b;
    }
}