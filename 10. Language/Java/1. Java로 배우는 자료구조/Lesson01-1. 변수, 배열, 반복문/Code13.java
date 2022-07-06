import java.util.Scanner;

/**
 * 
 * @author M9
 * n개의 음이 아닌 한자리 정수를 받아 배열에 저장한다
 * 이들 중 1개 이상의 연속된 정수들을 이어서(2 1 0 -> 210) 얻을 수 있는 소수 중에서 최대값인 수를 구하라
 * 입력 : 20 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 9 1 1 1 1
 * 출력 : 1234567891
 */
public class Code13 {
	public static void main(String[] args) {
		// 입력
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		for (int i = 0; i < data.length; i++) {
			data[i] = sc.nextInt();
		}
		sc.close();

		// 풀이
		int answer = 0;
		for (int i = 0; i < data.length; i++) {
			for (int j = i; j < data.length; j++) {
				// i번부터 j까지 합
				int sums = 0;
				for (int k = i; k <= j; k++) {
					sums = sums * 10 + data[k];
				}

				// 소수 체크
				Boolean isPrime = false;
				if (sums > 1) isPrime = true;
				for (int p = 2; p * p < sums; p++) {
					if (sums % p == 0)
						isPrime = false;
				}
				
				if(isPrime && sums>answer) answer = sums;
			}
		}
		
		System.out.println(answer);

	}
}