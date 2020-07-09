import java.rmi.*;

public interface Hello extends Remote {

    public void getAge(int age) throws RemoteException;
}