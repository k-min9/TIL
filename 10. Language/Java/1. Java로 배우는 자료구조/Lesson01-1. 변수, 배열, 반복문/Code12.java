import java.util.Scanner;

/**
 * 
 * @author M9
 * n개의 정수를 입력받아 배열에 저장한다.
 * 이들 중 0개 이상의 연속된 정수를 더하여 얻을 수 있는 최대값을 구하여 출력하라
 * 입력 : 13 -2 3 5 -14 12 3 -9 8 -1 13 2 -5 4
 * 출력 : 28
 */
public class Code12 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		for (int i = 0; i < data.length; i++) {
			data[i] = sc.nextInt();
		}
		sc.close();
		
		int answer = 0;
		for (int i = 0; i < data.length; i++) {
			for (int j = 0; j < data.length; j++) {
				int sums = 0;
				for (int k = i; k <=j ; k++) {
					sums += data[k];
				}
				if (sums > answer) answer = sums;
			}
		}
		System.out.println(answer);
		
	}
}
