import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;


public class Server extends Civilian {
    public Server () {}

    public static void main(String [] args) {
        try {
            if (args.length != 1) {
                System.out.println("usage: java Server <port>");
                System.exit(1);
            }

            int port = Integer.parseInt(args[0]);
            
            Civilian obj = new Civilian();

            Interface skeleton = (Interface) UnicastRemoteObject.exportObject(obj, 0);

            Registry reg = LocateRegistry.createRegistry(port);

            reg.rebind("Civilian", skeleton);

            System.err.println("Server run successfully!");

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}