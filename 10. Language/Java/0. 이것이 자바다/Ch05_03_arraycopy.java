package ch00;
//자바의 배열을 통으로 출력하고 싶으면 필요
import java.util.Arrays;

public class Ch05_03_arraycopy {
	public static void main(String[] args) {
		int[] oldIntArray = { 1, 2, 3 };
		int[] newIntArray = new int[5];
		int[] newIntArray2 = new int[5];
		
		//하나하나 복사
		for(int i=0; i<oldIntArray.length; i++) {
			newIntArray[i] = oldIntArray[i];
		}
		
		//깊은 복사
		System.arraycopy( oldIntArray, 0, newIntArray2, 0, oldIntArray.length);
		
		for(int i=0; i<newIntArray.length; i++) {
			System.out.print(newIntArray[i] + ", ");
		}
		System.out.println();
		System.out.println(Arrays.toString(newIntArray2));
	}
}
