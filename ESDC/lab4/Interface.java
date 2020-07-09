import java.rmi.*;

public interface Interface extends Remote {

    public void loadData() throws RemoteException;
    
    public boolean findbyfirstname(String firstname) throws RemoteException;    //ex1
    public int countbylastname(String lastname) throws RemoteException;         //ex2
    public boolean findbyid(int id) throws RemoteException;                     //ex3
    public int getMedianAge() throws RemoteException;                           //ex4
    public int getMinBD() throws RemoteException;                               //ex5
    public int getMaxBD() throws RemoteException;                               //ex6
    public int countbygender(String gender) throws RemoteException;             //ex7
    public String getInfo(String address) throws RemoteException;              //ex8
    public int countbystate(String statename) throws RemoteException;           //ex9

}