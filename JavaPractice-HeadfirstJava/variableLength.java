class apples{
	public static void main(String[] args){
		System.out.println(average(23,445,3,34,56, 23));	
	}
	public static int average(int...numbers){
		int total=0;
		for(int x:numbers)
			total+=x;

		return total/numbers.length;
	}
}
