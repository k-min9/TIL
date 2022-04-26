import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

/**
 * BOJ1021_Sv4_회전하는큐
 */
public class BOJ1021_Sv4_회전하는큐 {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    LinkedList<Integer> deque = new LinkedList<Integer>();

    int count = 0;

    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    for (int i = 1; i<=N; i++) {
      deque.offer(i);
    }

    int[] seq = new int[M];

    st = new StringTokenizer(br.readLine(), " ");
    for (int i = 0; i < M; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }

    for (int i = 0; i<M; i++) {
      int target = deque.indexOf(seq[i]);
      int half;

      if (deque.size() % 2 == 0) {
        half = deque.size() / 2 - 1;
      } else {
        half = deque.size() / 2;
      }

      // 원소가 중간 앞에 있음
      if (target <= half) {
        for (int j = 0; j < target; j++) {
          int temp = deque.pollFirst();
          deque.offerLast(temp);
          count++;
        }
      // 원소가 중간 뒤에 있음
      } else {
        for (int j = 0; j < deque.size() - target; j++ ) {
          int temp = deque.pollLast();
          deque.offerFirst(temp);
          count++;
        }
      }
      deque.pollFirst(); // 연산 종료 후 맨 앞 원소 아웃
    }
    System.out.println(count);    
  }
}