package ch00;
//자바의 배열을 통으로 출력하고 싶으면 필요
import java.util.Arrays;

public class Ch05_01_array {
	public static void main(String[] args) {
		int[] a = new int[10];
		int[] b = new int[] {30,60,90};
		
		//자바 배열 출력해보자
		System.out.println(Arrays.toString(a));
		System.out.println(Arrays.toString(b));
		System.out.println(a.length);		
		System.out.println(b.length);
	}
}
