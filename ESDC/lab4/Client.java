import java.lang.reflect.Parameter;
import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    public static void main(String [] args) {
        try {

            if (args.length != 4 && args.length != 3) {
                System.out.println("usage: java Client <host> <port> <command> <parameter>");
                System.exit(1);
            }

            int index = 0;
            String host = args[index++];
            int port = Integer.parseInt(args[index++]);
            String cmd = args[index++];

            String parameter = args.length == 4?args[index].strip():"";

            Registry reg = LocateRegistry.getRegistry(host, port);

            Interface stub = (Interface) reg.lookup("Civilian");
            stub.loadData();

            switch (cmd) {
                case "-findbyfirstname":
                    System.out.println(stub.findbyfirstname(parameter));;
                    break;

                case "-countbylastname":
                    System.out.println(stub.countbylastname(parameter));;
                    break;

                case "-findbyid":
                    System.out.println(stub.findbyid(Integer.parseInt(parameter)));;
                    break;

                case "-getMedianAge":
                    System.out.println(stub.getMedianAge());
                    break;

                case "-getMinBD":
                    System.out.println(stub.getMinBD());
                    break;

                case "-getMaxBD":
                    System.out.println(stub.getMaxBD());
                    break;

                case "-countbygender":
                    System.out.println(stub.countbygender(parameter));
                    break;

                case "-getInfo":
                    System.out.println(stub.getInfo(parameter));
                    break;

                case "-countbystate":
                    System.out.println(stub.countbystate(parameter));
                    break;

                default:
                    System.out.println("Command not found!");
                    System.exit(1);
                    break;
            }

            System.err.println("Client run successfully!");

        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

}