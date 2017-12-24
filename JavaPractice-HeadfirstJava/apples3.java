import java.util.EnumSet;

class apples3{
	public static void main(String[] args){
		for(tuna3 people: tuna3.values())
			System.out.printf("%s\t%s\t\t%s\n", people, people.getDesc(), people.getYear());

		System.out.println("\nAnd now for he range of constants!!!\n");

		for(tuna3 people: EnumSet.range(tuna3.kelsey, tuna3.candy))
			System.out.printf("%s\t%s\t\t%s\n", people, people.getDesc(), people.getYear());
	}
}
