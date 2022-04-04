import java.util.Scanner;

/**
 * java 강화 기간
 * 소수를 체로 걸러서 구하면서 더하기
 */
public class BOJ2581_Sv5_소수 {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    scan.close();

    int M = scan.nextInt();
    int N = scan.nextInt();

    boolean prime[] = new boolean[N+1];

    // 소수가 아니면 true
    prime[0] = true;
    prime[1] = true;

    for (int i=2; i<=Math.sqrt(N+1); i++) {
      for (int j = i * i; j < N+1; j += i) {
        prime[j] = true;
      }
    }

    int min = Integer.MAX_VALUE;
    int sum = 0;
    for (int i = M; i<N+1; i++) {
      if (prime[i] == false) {
        if (min > i) {
          min = i;
        }
        sum += i;
      }
    }

    if (sum == 0) System.out.println(-1);
    else {
      System.out.println(sum);
      System.out.println(min);
    }
  }
}