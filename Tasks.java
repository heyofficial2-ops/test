import java.util.Scanner;
public class Tasks {
    // Function 1: Reverse a string
    public static String reverse(String text) {
        return new StringBuilder(text).reverse().toString();
    }
    // Function 2: Find the maximum of two numbers
    //public static int max(int a, int b) {
      //  return (a > b) ? a : b;
    }
    // Function 3: Calculate the factorial of a number
    //ublic static int factorial(int n) {
      //  int result = 1;
        //for (int i = 1; i <= n; i++) {
          //  result *= i;
        //}
        //return result;
    //}

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Input for reverse
        System.out.print("Enter a string to reverse: ");
        String text = sc.nextLine();
        System.out.println("Reversed: " + reverse(text));

        // Input for max
        //System.out.print("Enter first number: ");
        //int a = sc.nextInt();
        //System.out.print("Enter second number: ");
        //int b = sc.nextInt();
        //System.out.println("Max: " + max(a, b));

        // Input for factorial
        //System.out.print("Enter a number to find factorial: ");
        //int n = sc.nextInt();
        //System.out.println("Factorial: " + factorial(n));
        //sc.close();
    }
}
