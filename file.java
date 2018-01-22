import java.io.File;

class apples{
	public static void main(String[] args){
		File x = new File("E:\\1StudyPlan\\DailyPractice\\java\\greg.txt"); 

		if(x.exists())
			System.out.println(x.getName() + " exists!");
		else
			System.out.println("This thing doesn't exists!");
	}
}
