import java.util.Scanner;

/**
 * n개의 정수를 입력받아 순서대로 배열에 저장하고, 모든 정수들을 한 칸 씩 오른쪽으로 shift하시오
 */
public class Code09 {
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] data = new int[n];
		for (int i = 0; i < n; i++) {
			data[i] = sc.nextInt();
		}
		sc.close();
		
		int tmp = data[n-1];
		for (int i = n-2; i>=0; i--)
			data[i+1] = data[i];
		data[0] = tmp;
		
		for (int i = 0; i  < data.length; i ++) {
			System.out.println(data[i]);
		}
	}
}

// input
//8
//8
//4
//1
//7
//11
//13
//5
//2
// output
//2
//8
//4
//1
//7
//11
//13
//5
