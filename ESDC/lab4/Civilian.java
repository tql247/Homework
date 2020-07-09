import java.io.BufferedReader;
import java.io.FileReader;
import java.lang.reflect.Array;
import java.rmi.*;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Map;

public class Civilian implements Interface {
    ArrayList<Person> listPerson = new ArrayList<Person>();
    int data_length = 0;
    
    Map<String, String> USPS = new HashMap<String, String>();

    public Civilian() {}

    public void loadData() throws RemoteException {
        listPerson.clear();


        try {
            BufferedReader br = new BufferedReader(new FileReader("data.csv"));
        
            String line;
            String address = "";
            String [] infor;
            line = br.readLine();

            while ((line = br.readLine()) != null) {
                infor = line.split(",");
                address = infor[4] + "," + infor[5];
                address = address.substring(1, address.length() - 1);
                listPerson.add(new Person(infor[0], Integer.parseInt(infor[1]), infor[2], Integer.parseInt(infor[3]), address));
                data_length++;
            }

            br.close();

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    } 
    

    public void loadUSPS() {
        USPS.clear();
        USPS.put("Alabama", "AL");
        USPS.put("Alaska", "AK");
        USPS.put("Arizona", "AZ");
        USPS.put("Arkansas", "AR");
        USPS.put("California", "CA");
        USPS.put("Colorado", "CO");
        USPS.put("Connecticut", "CT");
        USPS.put("Delaware", "DE");
        USPS.put("Florida", "FL");
        USPS.put("Georgia", "GA");
        USPS.put("Hawaii", "HI");
        USPS.put("Idaho", "ID");
        USPS.put("Illinois", "IL");
        USPS.put("Indiana", "IN");
        USPS.put("Iowa", "IA");
        USPS.put("Kansas", "KS");
        USPS.put("Kentucky", "KY");
        USPS.put("Louisiana", "LA");
        USPS.put("Maine", "ME");
        USPS.put("Maryland", "MD");
        USPS.put("Massachusetts", "MA");
        USPS.put("Michigan", "MI");
        USPS.put("Minnesota", "MN");
        USPS.put("Mississippi", "MS");
        USPS.put("Missouri", "MO");
        USPS.put("Montana", "MT");
        USPS.put("Nebraska", "NE");
        USPS.put("Nevada", "NV");
        USPS.put("New Hampshire", "NH");
        USPS.put("New Jersey", "NJ");
        USPS.put("New Mexico", "NM");
        USPS.put("New York", "NY");
        USPS.put("North Carolina", "NC");
        USPS.put("North Dakota", "ND");
        USPS.put("Ohio", "OH");
        USPS.put("Oklahoma", "OK");
        USPS.put("Oregon", "OR");
        USPS.put("Pennsylvania", "PA");
        USPS.put("Rhode Island", "RI");
        USPS.put("South Carolina", "SC");
        USPS.put("South Dakota", "SD");
        USPS.put("Tennessee", "TN");
        USPS.put("Texas", "TX");
        USPS.put("Utah", "UT");
        USPS.put("Vermont", "VT");
        USPS.put("Virginia", "VA");
        USPS.put("Washington", "WA");
        USPS.put("West Virginia", "WV");
        USPS.put("Wisconsin", "WI");
        USPS.put("Wyoming", "WY");
    }

    public boolean findbyfirstname(String firstname) throws RemoteException {    //ex1
        
        for (Person p: listPerson) {
            if (p.getfirstname().equals(firstname))
                return true;   

        }
        
        return false;
    }


    public int countbylastname(String lastname) throws RemoteException {         //ex2
        int count = 0;

        for (Person p: listPerson)
            count += p.getlastname().equals(lastname)?1:0;

        return count;
    }


    public boolean findbyid(int id) throws RemoteException {

        for (Person p: listPerson)
            if (p.getid() == id)
                return true;   
        
        return false;
    }


    public int getMedianAge() throws RemoteException {
        int sumAge = 0;
        int crr_year = Calendar.getInstance().get(Calendar.YEAR);

        for (Person p: listPerson)
            sumAge += (crr_year - p.getBD());  

        return sumAge/data_length;
    }


    public int getMinBD() throws RemoteException {
        int minBD = Calendar.getInstance().get(Calendar.YEAR);

        for (Person p: listPerson)
            minBD = p.getBD()<minBD?p.getBD():minBD;

        return minBD;
    }


    public int getMaxBD() throws RemoteException {
        int maxBD = 0;

        for (Person p: listPerson)
            maxBD = p.getBD()>maxBD?p.getBD():maxBD;

        return maxBD;
    }


    public int countbygender(String gender) throws RemoteException {
        int count = 0;

        for (Person p: listPerson)
            count += p.getgender().equals(gender)?1:0;

        return count;
    }


    public String getInfo(String address) throws RemoteException {
        String personInfo = "";

        for (Person p: listPerson) 
            if (p.getaddress().equals(address))
                personInfo += p.getinfo();


        return personInfo;
    }


    public int countbystate(String statename) throws RemoteException {
        int count = 0;

        this.loadUSPS();
        statename = statename.length() != 2?this.USPS.get(statename):statename;


        for (Person p: listPerson)
            count += p.getstatename().equals(statename)?1:0;

        return count;
    }
    
}