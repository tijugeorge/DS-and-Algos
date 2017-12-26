import java.util.HashMap;

public class MF{
    public static void main(String[] args){
        int[] array1 = {1,3,1,3,2,1};
        int[] array2 = {2,4,5,2,3,5,2,3,4};

        System.out.println(mostFrequent(array1));
        System.out.println(mostFrequent(array2));
    }

    public static Integer mostFrequent(int[] givenArray){
        Integer maxCount = -1;
        Integer maxItem = null;

        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        for(int i: givenArray){
            if (count.containsKey(i)){
                Integer newVal = count.get(i)+1;
                count.put(i, newVal);
            } else {
                count.put(i, 1);
            }
            if (count.get(i)> maxCount){
                maxCount = count.get(i);
                maxItem = i;
            }
        }
        return maxItem;
    }
}
