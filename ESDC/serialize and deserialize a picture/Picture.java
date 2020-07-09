import java.io.Serializable;
import java.io.File;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import javax.swing.ImageIcon;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.Dimension;
import java.io.IOException;


public class Picture implements Serializable {
    private BufferedImage myPicture;
    private String name;

    public Picture () {}

    public Picture(String path) {
        try {
            this.myPicture = ImageIO.read(new File(path));
        }
        catch (Exception e){
            System.err.println("Error :" + e.getMessage());
        }
    }

    public void writeObject(java.io.ObjectOutputStream out/*, String imgName*/)throws IOException{
        // out.writeObject(imgName);
        ImageIO.write(this.myPicture,"jpg",ImageIO.createImageOutputStream(out));
    }

    public void readObject(java.io.ObjectInputStream in)throws IOException, ClassNotFoundException{
        // name=(String)in.readObject();
        this.myPicture=ImageIO.read(ImageIO.createImageInputStream(in));
    }

    public void display() {
        JLabel picLabel = new JLabel(new ImageIcon(this.myPicture));
        JPanel jPanel = new JPanel();
        jPanel.add(picLabel);
        JFrame f = new JFrame();
        f.setSize(new Dimension(myPicture.getWidth(), myPicture.getHeight()));
        f.add(jPanel);
        f.setVisible(true);
    }
}