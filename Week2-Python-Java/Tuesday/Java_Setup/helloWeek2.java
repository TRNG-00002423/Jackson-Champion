public class helloWeek2 {
    public static void main(String[] args) {
        if (args.length >= 1) {
            System.out.println("Hello, " + args[0] + "!");
        }
        else {
            System.out.println("Hello, trainee!");
        }

        System.out.println("Java Version: " + Runtime.version());
    }    
}

/*Hello, trainee!
Java Version: 20.0.1+9-29 */