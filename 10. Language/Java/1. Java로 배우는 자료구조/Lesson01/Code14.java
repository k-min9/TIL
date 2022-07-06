import java.util.Scanner;

/**
 * 
 * @author M9
 * n개의 정수를 받아 bubble sort 하라
 * 입력 : 8 8 4 1 7 11 13 5 2
 * 출력 : 1 2 4 5 7 8 11 13
 */
public class Code14 {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		for (int i = 0; i < data.length; i++) {
			data[i] = sc.nextInt();
		}
		sc.close();

		// bubble sort
		for (int i = n - 1; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (data[j] > data[j + 1]) {
					// swap
					int tmp = data[j];
					data[j] = data[j + 1];
					data[j + 1] = tmp;
				}
			}
		}

		// 출력
		System.out.print("정렬 결과: ");
		for (int i = 0; i < data.length; i++) {
			System.out.println(data[i]);
		}
	}
}
