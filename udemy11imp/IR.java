public class IR{
	public static void main(String[] args){
		int[] array1 = {1, 2, 3, 4, 5, 6, 7};
        int[] array2a = {4, 5, 6, 7, 8, 1, 2, 3};
        // isRotation(array1, array2a) should return false.
        System.out.println(isRotation(array1, array2a));
        int[] array2b = {4, 5, 6, 7, 1, 2, 3};
        System.out.println(isRotation(array1, array2b));
        // isRotation(array1, array2b) should return true.
        int[] array2c = {4, 5, 6, 9, 1, 2, 3};
        System.out.println(isRotation(array1, array2c));
        // isRotation(array1, array2c) should return false.
        int[] array2d = {4, 6, 5, 7, 1, 2, 3};
        System.out.println(isRotation(array1, array2d));
        // isRotation(array1, array2d) should return false.
        int[] array2e = {4, 5, 6, 7, 0, 2, 3};
        System.out.println(isRotation(array1, array2e));
        // isRotation(array1, array2e) should return false.
        int[] array2f = {1, 2, 3, 4, 5, 6, 7};
        System.out.println(isRotation(array1, array2f));
        // isRotation(array1, array2f) should return true.
	}

	public static Boolean isRotation(int[] array1, int[] array2){
		if(array1.length != array2.length) return false;
		int first = array1[0];
		int key_index = -1;
		for (int index = 0; index < array2.length; index++){
			if (array2[index] == first){
				key_index = index;
				break;
			}
		}
		if (key_index == -1) return false;
		for(int index = 0; index < array1.length; index++){
			int indexB = (key_index + index) % array1.length;
			if(array1[index] != array2[indexB]) return false;
		}
		return true;
	}
}
