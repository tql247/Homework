import java.rmi.*;

public class ImpHello implements Hello {

    public void getAge(int age) {
        System.out.print("Age: ");
        System.out.println(age);
    }
}