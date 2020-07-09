import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server extends ImpCal {

    public Server () {}

    public static void main(String [] args) {

        try {

            ImpCal obj = new ImpCal();

            Cal skeleton = (Cal) UnicastRemoteObject.exportObject(obj, 0);

            Registry reg = LocateRegistry.createRegistry(1010);

            reg.rebind("Cal", skeleton);

            System.err.println("Server is running!");

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}