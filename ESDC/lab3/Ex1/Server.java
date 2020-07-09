import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server extends ImpHello {

    public Server () {}

    public static void main(String [] args) {

        try {

            ImpHello obj = new ImpHello();

            Hello skeleton = (Hello) UnicastRemoteObject.exportObject(obj, 0);

            Registry reg = LocateRegistry.createRegistry(1010);

            reg.rebind("Hello", skeleton);

            System.err.println("Server is running!");

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}