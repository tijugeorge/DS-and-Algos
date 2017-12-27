import java.util.HashMap;

public class nr{
	public static void main(String[] args){
		System.out.println(nonRepeating("abcab")); // should return 'c'
        System.out.println(nonRepeating("abab")); // should return null
        System.out.println(nonRepeating("aabbbc")); // should return 'c'
        System.out.println(nonRepeating("aabbdbc")); // should return 'd'
	}

	public static Character nonRepeating(String s){
		HashMap<Character, Integer> Counter = new HashMap<Character, Integer>();
		for (char c: s.toCharArray()){
			if (Counter.containsKey(c)){
				Integer newVal = Counter.get(c)+1;
				Counter.put(c, newVal);
			} else {
				Counter.put(c, 1);
			}
		}
		for (char c: s.toCharArray()){
			if (Counter.get(c) == 1) return c;
		}
		return null;
	}
}
