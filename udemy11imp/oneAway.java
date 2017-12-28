public class oneAway{
	public static void main(String[] args){
		System.out.println(isOneAway("abcde", "abcd"));  // should return true
        System.out.println(isOneAway("abde", "abcde"));  // should return true
        System.out.println(isOneAway("a", "a"));  // should return true
        System.out.println(isOneAway("abcdef", "abqdef"));  // should return true
        System.out.println(isOneAway("abcdef", "abccef"));  // should return true
        System.out.println(isOneAway("abcdef", "abcde"));  // should return true
        System.out.println(isOneAway("aaa", "abc"));  // should return false
        System.out.println(isOneAway("abcde", "abc"));  // should return false
        System.out.println(isOneAway("abc", "abcde"));  // should return false
        System.out.println(isOneAway("abc", "bcc"));  // should return false
	}

	public static Boolean isOneAway(String s1, String s2){
		if (s1.length() - s2.length() >= 2 || s2.length() - s1.length() >= 2){
			return false;
		} else if (s1.length() == s2.length()){
			return isOneAwaySameLength(s1, s2);
		} else if (s1.length() > s2.length()){
			return isOneAwayDiffLength(s1, s2);
		} else {
			return isOneAwayDiffLength(s2, s1);
		}
	}

	public static Boolean isOneAwaySameLength(String s1, String s2){
		int countDiff = 0;
		for (int i = 0; i < s1.length(); i++){
			if (s1.charAt(i) != s2.charAt(i)){
				countDiff += 1;
				if (countDiff > 1) return false;
			}
		}
		return true;
	}

	public static Boolean isOneAwayDiffLength(String s1, String s2){
		int i = 0;
		int countDiff = 0;
		while (i < s2.length()){
			if (s1.charAt(i + countDiff) == s2.charAt(i)){
				i += 1;
			} else {
				countDiff += 1;
			}
			if (countDiff > 1){
				return false;
			}
		}
		return true;
	}
}
