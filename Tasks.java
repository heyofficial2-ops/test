public class Tasks {

    // Function 1: Reverse a string
    //public static String reverse(String text) {
//    return new StringBuilder(text).reverse().toString();
    //}

    // Function 2: Find the maximum of two numbers
    //public static int max(int a, int b) {
      //  return (a > b) ? a : b;
    //}

    // Function 3: Calculate the factorial of a number
    public static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    public static void main(String[] args) {
    //    System.out.println("Reversed: " + reverse("Hello"));
      //  System.out.println("Max: " + max(10, 25));
        System.out.println("Factorial: " + factorial(5));
    }
}
