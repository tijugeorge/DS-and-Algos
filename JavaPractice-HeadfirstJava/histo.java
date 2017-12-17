import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;

public class Histo{
	public static void main(String[] args){
		Scanner data = null;
		ArrayList<Integer> count;
		Integer idx;

		try{
			data = new Scanner(new File("test.dat"));
		}
		catch(IOException e){
			System.out.println("Sorry but I was unable to open your data file");
			e.printStackTrace();
			System.exit(0);
		}

		count = new ArrayList<Integer>(10);
		for (Integer i = 0; i<10; i++){
			count.add(i,0);
		}
		//System.out.println(count);

		while(data.hasNextInt()){
			idx = data.nextInt();
			System.out.println(idx);
			count.set(idx, count.get(idx)+1);
			System.out.println(count);
		}

		idx = 0;
		for (Integer i: count){
			System.out.println(idx+" occured "+i+" times.");
			idx++;
		}
	}
}
