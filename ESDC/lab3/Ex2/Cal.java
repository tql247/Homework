import java.rmi.*;

public interface Cal extends Remote {

    public long add (long a, long b) throws RemoteException;
    public long sub (long a, long b) throws RemoteException;
}