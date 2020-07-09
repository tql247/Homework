import java.rmi.*;

public class Person implements Interface{

    public boolean find(String surname) throws RemoteException {

        return true;
    }

    public String pctwhite(int num) throws RemoteException {

        return "all the surnames have pctwhite smaller than " + Integer.toString(num);
    }

    public void list(int num) throws RemoteException {

        System.out.println("list all Person whose count is larger than " + Integer.toString(num));
    }
}