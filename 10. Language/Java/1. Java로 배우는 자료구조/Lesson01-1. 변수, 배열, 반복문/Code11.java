import java.util.Scanner;

/**
 * @author M9
 * 사용자로부터 먼저 정수의 개수 n을 입력 받는다
 * n개의 정수를 받아 순서대로 배열에 저장한다
 * 중복된 정수 쌍의 갯수를 카운트 하여 출력하라
 * 입력 : 6 / 2 / 4 / 2 / 4 / 5 / 2
 * 과정 : (2,2), (2,2), (2,2), (4,4) 4쌍이 존재함
 * 출력 : 4
 */
public class Code11 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		for (int i = 0; i < n; i++) {
			data[i] = sc.nextInt();
		}
		sc.close();
		
		int count = 0;
		for (int i = 0; i < n-1; i++) {
			for (int j = i+1; j < n; j++) {
				if(data[i] == data[j]) count++;
			}
		}
		System.out.println(count);
	}
}
