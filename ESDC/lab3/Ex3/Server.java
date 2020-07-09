import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server extends Person {

    public Server() {

    }

    public static void main(String [] args) {

        if (args.length != 1) {
            System.out.println("Usage: java Server <post>");
            System.exit(1);
        }


        try {

            int index = 0;
            int port = Integer.parseInt(args[index++]);

            Person obj = new Person();

            Interface skeleton = (Interface) UnicastRemoteObject.exportObject(obj, 0);

            Registry reg = LocateRegistry.createRegistry(port);

            reg.rebind("Person", skeleton);

            System.err.println("Server is running!");

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}