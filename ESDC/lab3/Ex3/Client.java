import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    public Client () {}

    public static void main(String [] args) {

        if (args.length != 4) {
            System.out.println("Usage: java Server <host> <post> <command> <value>");
            System.exit(1);
        }


        try {

            int index = 0;
            String host = args[index++];
            int port = Integer.parseInt(args[index++]);
            String cmd = args[index++];

            Registry reg = LocateRegistry.getRegistry(host, port);

            Interface stub = (Interface) reg.lookup("Person");

            switch(cmd) {

                case "find":
                    System.out.println(stub.find(args[index++]));
                break;

                case "pctwhite":
                    System.out.println(stub.pctwhite(Integer.parseInt(args[index++])));
                break;

                case "list":
                    stub.list(Integer.parseInt(args[index++]));
                break;

                default:
                    System.out.println("Wrong command!");
                    System.exit(1);
            }

            System.out.print("Client evoke Success!");



        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}