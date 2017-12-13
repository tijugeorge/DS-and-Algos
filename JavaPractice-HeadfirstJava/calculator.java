import java.util.Scanner;

class apples{
	public static void main(String args[]){
		Scanner bucky = new Scanner(System.in);
		double fnum, snum, answer;
		System.out.println("Enter first num: ");
		fnum = bucky.nextDouble();
		System.out.println("Enter second num: ");
		snum = bucky.nextDouble();
		answer = fnum + snum;
		System.out.println(answer);
		int tuna = 5;
		System.out.println(tuna++);
		System.out.println(tuna);	

		int test = 6;
		if (test < 9){
			System.out.println("yes");
		} else {
			System.out.println("This is else");
		}			
	}
}
