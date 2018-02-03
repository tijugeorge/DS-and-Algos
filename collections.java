import java.util.ArrayList;

public class collections {
	public static void main(String [] args){
		ArrayList grades = new ArrayList();
		grades.add(100);
		grades.add(97);
		grades.add(85);
		//System.out.println(grades.get(1));
		//System.out.println(grades.size());

		int size = grades.size();

		for (int i=0; i<size; i++){
			System.out.println(grades.get(i));
		}

		ArrayList<String> grades1 = new ArrayList();
		grades1.add("100");
		grades1.add("97");
		grades1.add("85");		
		for (String item : grades1){
			System.out.println(Integer.parseInt(item));
		}
	}
}
