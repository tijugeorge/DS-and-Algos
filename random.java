import java.util.Random;

class apples{
	public static void main(String[] args){
		Random dice = new Random();
		int number;

		for(int counter=1; counter<=10; counter++){
			number = 1+ dice.nextInt(6);  //to get the random nos from 1 to 6
			System.out.println(number + "  ");
		}
	}
}
