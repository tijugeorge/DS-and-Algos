class apples{
	public static void main(String[] args){
		timeClass1 timeClass1Object = new timeClass1();
		System.out.println(timeClass1Object.toMilitary());
		System.out.println(timeClass1Object.toString());

		timeClass1Object.setTime(13, 27, 6);
		System.out.println(timeClass1Object.toMilitary());
		System.out.println(timeClass1Object.toString());
	}
}
