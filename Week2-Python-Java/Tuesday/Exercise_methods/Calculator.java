import java.util.OptionalDouble;

/**
 * Week 2 Exercise — Calculator with static methods and overloads.
 *
 * Division by zero strategy (TODO — choose and implement):
 *   Option A: print error message and return Double.NaN
 *   Option B: return 0.0 and document why (not ideal for production)
 *
 * Compile: javac Calculator.java
 * Run:     java Calculator
 */
public class Calculator {

    public static double add(double a, double b) {
        return a + b;
    }

    /** Sum of three doubles — overloads add(a,b). */
    public static double add(double a, double b, double c) {
        return a + b + c;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static OptionalDouble divide(double a, double b) {
        if (b == 0) {
            return OptionalDouble.empty();
        }

        return OptionalDouble.of(a / b);
    }


    public static void main(String[] args) {
        System.out.println("\nAdding 2 numbers: 5 + 3 = " + add(5, 3));
        System.out.println("\nOverloading: Add 3 numbers: 5 + 3 + 2 = " + add(5, 3, 2));
        System.out.println("\nSubtraction: 7 - 2 = " + subtract(7, 2));
        System.out.println("\nMultiplying: 10 * 2 = " + multiply(10, 2));
        System.out.println("\nDivision: 10 / 2 = " + divide(10, 2));
        System.out.println("Division by zero: 10 / 0 = " + divide(10, 0));
    }
}