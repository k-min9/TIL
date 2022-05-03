import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

/**
 * BOJ1927_Sv2_최소힙
 * 실제 최소힙을 써서 그냥 넣고 뺄 뿐
 * ...아마 진짜 클래스 단위 구현을 원한거긴 할텐데?
 */
public class BOJ1927_Sv2_최소힙 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    PriorityQueue<Integer> q = new PriorityQueue<>();

    int N = Integer.parseInt(br.readLine());
    int val;

    for (int i = 0; i < N; i++) {
      val = Integer.parseInt(br.readLine());
      if (val != 0) {
        q.add(val);
      } else if (q.isEmpty()) {
        bw.write("0\n");
      } else {
        bw.write(q.poll() + "\n");
      }
    }

    bw.flush();
    bw.close();
    bw.close();
  }
}