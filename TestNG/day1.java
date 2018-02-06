package test;

import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

public class day1 {
	
	@AfterTest
	public void lastExecution() {
		System.out.println("Phew! I'm last!");
	}
	
	@Test
	public void Demo() {
		// TODO Auto-generated method stub
		System.out.println("Hey there");
	}
	
	@Test
	public void SecondTest() {
		System.out.println("Bye!");
	}

}
