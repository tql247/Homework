import java.rmi.*;

public class Person {
    private String fullname;
    private int id;
    private String gender;
    private int birthyear;
    private String address;
    
    public Person(String fullname, int id, String gender, int birthyear, String addrees) {
        this.fullname = fullname;
        this.id = id;
        this.gender = gender;
        this.birthyear = birthyear;
        this.address = addrees;
    }

    public String getfirstname() {
        return this.fullname.split(" ")[0];
    }

    public String getlastname() {
        return this.fullname.split(" ")[1];
    }

    public int getid() {
        return this.id;
    }

    public String getgender() {
        return this.gender;
    } 

    public int getBD() {
        return this.birthyear;
    }

    public String getaddress() {
        return this.address;
    }

    public String getinfo() {
        return "{"+this.fullname+","+this.id+","+this.gender+","+this.birthyear+"}";
    }

    public String getstatename() {
        String [] addressDetail = this.address.split(" ");
        return addressDetail[addressDetail.length - 2];
    }
}