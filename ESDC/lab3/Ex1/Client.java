import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;


public class Client {

    public Client() {}

    public static void main(String [] args) {

        try {

            Registry reg = LocateRegistry.getRegistry("localhost", 1010);
            Hello stub = (Hello) reg.lookup("Hello");

            stub.getAge(22);

            System.out.println("Client is running!");

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}