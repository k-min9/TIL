package Section02;

import java.util.Scanner;

/**
 * @author M9
 * Bubblesort를 추출하여 정렬해보자
 * 입력 : 8 8 4 1 7 11 13 5 2
 * 출력 : 1 2 4 5 7 8 11 13
 * 키워드 : Code14의 내용과 동일함. 추출할 뿐
 */
public class Code18 {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		for (int i = 0; i < data.length; i++) {
			data[i] = sc.nextInt();
		}
		sc.close();

		// bubble sort를 추출
		bubbleSort(data, n);

		// 출력
		System.out.print("정렬 결과: ");
		for (int i = 0; i < data.length; i++) {
			System.out.println(data[i]);
		}
	}
	
	// 배열 같은 primitive 타입이 아니면 호출한 쪽도 변경 됨
	static void bubbleSort(int[] data, int n) {
		for (int i = n - 1; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (data[j] > data[j + 1]) {
					// swap
					int tmp = data[j];
					data[j] = data[j + 1];
					data[j + 1] = tmp;
					
					// call by val에 의해 망가지는 swap
//					swap(data[j], data[j+1]);
				}
			}
		}
	}
	
	// 이대로 하면 당연히 망가진다. (내부에서만 바꿈)
	static void swap(int a, int b) {
		int tmp = a;
		a = b;
		b = tmp;
	}
}
