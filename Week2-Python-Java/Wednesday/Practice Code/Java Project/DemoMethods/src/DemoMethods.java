import java.util.Scanner;

public class DemoMethods {
    public static void main(String[] args) {
        System.out.println("Hello There...");

        Scanner sc = new Scanner(System.in);

        String name = sc.next();

        String result = greet(name);

        System.out.println(result);

        sc.close();

    
    }

    public static int sum(int num1, int num2) {
        return (num1 + num2);
    } 

    public static int sum(int num1, int num2, int num3) {
        return (num1 + num2 + num3);
    }

    static String greet(String name) {
        return "Hello " + name;

    }
}
