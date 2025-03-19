import java.util.Scanner;

class Main {
	public static void main(String[] args) 
    {
		int x = 4;
		int y = 6;
		int z;

		Scanner myInput = new Scanner(System.in);
		System.out.println("Pick a number");
		int a = myInput.nextInt();
		System.out.println("The value a is:" + a);
		System.out.println("The variable X has a value of:" + x + " and the variable Y has a value of: " + y);
		System.out.println("The sum of both is: " + a);
	}
}