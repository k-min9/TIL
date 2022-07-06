import java.util.Scanner;

/**
 * 
 * @author M9
 * 사용자로부터 n개의 정수를 입력받는다.
 * 정수가 하나 입력될 때 마다 현재까지 입력된 정수들을 오름차순으로 정렬하여 출력하라
 * 입력 : 7 3 1 6 4 7 2 9
 */
public class Code15 {
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		
		for (int i = 0; i < data.length; i++) {
			int tmp = sc.nextInt();
			int j = i-1;
			// 기존에 정렬이 되어있을테니 넣은 숫자가 원하는 위치일때까지 한칸씩 이동하자
			while (j >= 00 && data[j]>tmp) {
				data[j+1] = data[j];		
				j--;
			}
			data[j+1] = tmp;
			
			for (int k = 0; k < data.length; k++) {
				System.out.print(data[k]+ " ");
			}
			System.out.println();
		}
		
		sc.close();
	}
}
