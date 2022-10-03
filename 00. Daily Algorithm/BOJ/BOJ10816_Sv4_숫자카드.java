import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

/**
 * BOJ10816_Sv4_숫자카드
 * 파이썬으로 풀면 너무 쉽고, 자바도 비슷은 할거 같은데에...
 */
public class BOJ10816_Sv4_숫자카드 {

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();

    // 입력해서 hashmap에 넣고
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i< N; i++) {
      int input = Integer.parseInt(st.nextToken());
      if (counter.get(input) == null) {
        counter.put(input, 1);
      } else {
        counter.put(input, counter.get(input)+1);
      }
    }

    // 그저 읽을 뿐
    int M = Integer.parseInt(br.readLine());

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < M; i++) {
      int input = Integer.parseInt(st.nextToken());
      if (counter.get(input) == null) {
        sb.append("0 ");
      } else {
        sb.append(counter.get(input)).append(" ");
      }
    }
    System.out.println(sb);
  }
}