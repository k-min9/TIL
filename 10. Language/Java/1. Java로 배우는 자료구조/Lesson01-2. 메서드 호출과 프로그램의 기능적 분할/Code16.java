package Section02;

import java.util.Scanner;

/**
 * 
 * @author M9
 * 정수 a b를 받아 a의 b제곱을 구하라
 * 키포인트 : a의 b제곱을 계산하는 함수를 만들자
 */
public class Code16 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int result = power(a,b);
		System.out.println("결과 : " + result);
		sc.close();
	}
	
	// a의 b제곱 함수 정의
	static int power(int n, int m) {
		int result = 1;
		for (int i = 0; i < m; i++) {
			result *= n;
		}
		return result;
	}

}
