import java.util.Scanner;

/**
 * BOJ11726_Sv3_2n타일링
 * 써보면 안다. 이거 피보나치다.
 * dp
 */
public class BOJ11726_Sv3_2n타일링 {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    sc.close();
    int[] dp = new int[N+2];

    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= N; i++) {
      dp[i] = (dp[i-1] + dp[i-2]) % 10007;
    }
    System.out.println(dp[N]);
  }
}