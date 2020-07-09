import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.IOException;
import java.io.Serializable;


class deserializePicture {
    public static void main(String [] args) {
        try {
            String filename = "picture.ser";
            Picture p = new Picture();
            
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename));
            p.readObject(ois);
            p.display();
            ois.close();
        }
        catch (Exception e) {
            System.out.print("Error: " );
            System.err.println(e.getMessage());
        }
    }
}