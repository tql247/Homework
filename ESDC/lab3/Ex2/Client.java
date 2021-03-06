import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;


public class Client {

    public Client() {}

    public static void main(String [] args) {

        try {

            Registry reg = LocateRegistry.getRegistry("localhost", 1010);
            Cal stub = (Cal) reg.lookup("Cal");

            System.out.print("3L + 2L = ");
            System.out.print(stub.add(3L, 2L));
            System.out.println();
            System.out.print("3L - 2L = ");
            System.out.print(stub.sub(3L, 2L));
            System.out.println();



            System.out.println("Client is running!");

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}