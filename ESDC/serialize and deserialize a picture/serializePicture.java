import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.IOException;
import java.io.Serializable;


class serializePicture {
    public static void main(String [] args) {
        try {
            String filename = "picture.ser";
            String path = "img.jpg";
            // String imgName = "img";
            Picture p = new Picture(path);

            ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename));
            
            p.writeObject(oos/*, imgName*/);
           
            oos.close();
        }
        catch (Exception e) {
            System.out.print("Error: " );
            System.err.println(e.getMessage());
        }
    }
}