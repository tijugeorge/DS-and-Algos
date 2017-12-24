public enum tuna3 {
	bucky("nice", "32"),
	kelsey("cutie", "10"),
	julia("bigmistake", "12"),
	nicole("italian", "13"),
	candy("different", "14"),
	erin("iwish", "16");

	private final String desc;
	private final String year;

	tuna3(String description, String birthday){
		desc = description;
		year = birthday;
	}

	public String getDesc(){
		return desc;
	}

	public String getYear(){
		return year;
	}


}
