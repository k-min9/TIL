import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ11403_Sv1_경로찾기 {
  /**
   * 당분간 자바 능력 강화...
   * 일단 딱 봐도 플로이드 와셜인데 내용물이 1임 ㅎ!
   * 시간 문제상 오늘은 라이브 코딩하고 코틀린가즈아!
   */
  public static void main(String[] args) throws NumberFormatException, IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    // 입력
    int N = Integer.parseInt(br.readLine());
    int[][] arr = new int[N][N];

    for (int i = 0; i < N ; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        arr[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    // 플로이드 와셜
    for (int k = 0; k < N; k++) {
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          if (arr[i][k] == 1 && arr[k][j] == 1) arr[i][j] = 1;
        }
      }
    }

    // arr 출력할 빌더
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
          sb.append(arr[i][j] + " ");
      }
      sb.append("\n");
    }
    
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }
}

// 다음부터 자바로 풀거면 애초에 인텔리제이 켜야겠다. 단축키가 너무 없어...
// import 빼먹기 주의 이름 Main 까먹고 안바꾸기 주의... orz