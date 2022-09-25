import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

/**
 * BOJ18870_Sv2_좌표압축
 * 문제 이해에 시간이 걸림
 * (=리스트 안에서의 크기 순서를 출력하시오. 0부터)
 * 
 * 해쉬맵으로 해결
 */
public class BOJ18870_Sv2_좌표압축 {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int N = Integer.parseInt(br.readLine());

    String[] nums = br.readLine().split(" ");
    int[] answers = new int[N];

    for (int i = 0; i < nums.length; i++) {
      answers[i] = Integer.parseInt(nums[i]);
    }
    int[] tmp = answers.clone();

    Arrays.sort(answers);

    int cnt = 0;
    HashMap<Integer, Integer> hashMap = new HashMap<>();
    for (int i = 0; i < answers.length; i++) {
      if (!hashMap.containsKey(answers[i])) {
        hashMap.put(answers[i], cnt++);
      }
    }

    for (int i = 0; i < tmp.length; i++) {
      sb.append(hashMap.get(tmp[i])).append(" ");
    }

    System.out.println(sb.toString());   
  }
}