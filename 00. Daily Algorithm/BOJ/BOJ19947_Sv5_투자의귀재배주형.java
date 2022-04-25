import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/**
 * BOJ19947_Sv5_투자의귀재배주형
 * DP
 */
public class BOJ19947_Sv5_투자의귀재배주형 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // 초기 비용, 투자 기간
    int H = Integer.parseInt(st.nextToken());
    int Y = Integer.parseInt(st.nextToken());

    long[] dp = new long[Y+1];
    dp[0] = H;

    // 이자
    for (int i = 1; i <= Y; i++) {
      dp[i] = (long)Math.floor(dp[i-1] * 1.05);
      if(i >= 3)
          dp[i] = Math.max((long)Math.floor(dp[i-3] * 1.2), dp[i]);
      if(i >= 5)
          dp[i] = Math.max((long)Math.floor(dp[i-5] * 1.35), dp[i]);
    }

    bw.write(dp[Y] + "\n");
    bw.flush();
    br.close();
    bw.close();
  }
}