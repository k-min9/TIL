/**
 * 자바 오랜만에 한번 더 class main으로 쉽게 만들기
 * 장르 : DP
 */

import java.util.*;

public class BOJ15489_Sv5_파스칼삼각형 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[][] dp = new int[31][31];
		
		int R = sc.nextInt();
		int C = sc.nextInt();
		int W = sc.nextInt();
    sc.close();
		
		//1C1의 값은 1
		dp[1][1] = 1;
		
		//30줄까지 뿌려놓기
		for(int i=1;i<=30;i++) {
			for(int j=1;j<=i;j++) {
				//j가 i랑 같은 맨 뒤이거나, 맨 앞이 j가 1이라면 1로 설정
				//즉, 3C3도 1 3C0 일 경우 1이다
				if(j==i || j==1) dp[i][j] = 1;
				
				//아닐 경우에는 위의 왼쪽과 오른쪽의 합이 dp[i][j]가 된다.
				else dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
			}
		}
		int sum = 0;
				
    // 직접 더하기
		for(int i=0;i<W;i++) {
			for(int j=0;j<i+1;j++) {
				sum += dp[R+i][C+j];
			}
		}
		
		System.out.println(sum);		
	}
}


