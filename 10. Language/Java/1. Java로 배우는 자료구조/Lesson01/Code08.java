import java.util.Scanner;

/**
 * 사용자로부터 n개의 정수를 입력받은 후 합과 최대값을 출력하시오
 */
public class Code08 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int [n];
		
		for (int i = 0; i < n; i++) {
			data[i] = sc.nextInt();
		}

		int sums = 0;
		int max = 0;
		for(int i =0 ; i<n; i++) {
			sums += data[i];
			if (data[i] > max) max = data[i];
		}
		
		System.out.println("총 합 : " + sums);
		System.out.println("최대값 : " + max);

	}

}
