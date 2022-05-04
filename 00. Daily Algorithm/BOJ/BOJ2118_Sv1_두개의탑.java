import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * BOJ2118_Sv1_두개의탑
 * 거리가 최대가 되도록 -> 총합은 일정하니까...
 * 한쪽은 증가만 하고 한쪽은 감소만 하니까 그 수치가 역전되는 시점에서 고정점을 이동하는 식으로 투포인터를 구현할 수 있다.
 */
public class BOJ2118_Sv1_두개의탑 {

  public static void main(String[] args) throws IOException {
    BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());

    int[] boards = new int[N+1];

    // 입력
    int sum = 0;
    for (int i=0; i<N; i++) {
      int n = Integer.parseInt(br.readLine());
      boards[i] = n;
      sum += n;
    }

    int start = 0;
    int end = 0;

    int answer = 0;
    int now = boards[start];
    while (start <= end && end < N) {
      int cur = Integer.min(now, sum-now);
      answer = Integer.max(cur, answer);

      if (now == cur) {
        end++;
        now += boards[end];
      } else {
        now -= boards[start];
        start++;
      }
    }

    System.out.println(answer);

  }
}