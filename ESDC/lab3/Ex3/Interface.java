import java.rmi.*;

public interface Interface extends Remote {

    public boolean find(String surname) throws RemoteException;

    public String pctwhite(int num) throws RemoteException;

    public void list(int num) throws RemoteException;
}