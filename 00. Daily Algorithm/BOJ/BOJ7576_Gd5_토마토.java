import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.LinkedList;
import java.util.Queue;

/**
 * BOJ7576_Gd5_토마토
 * 언어 : java
 * BFS
 * 자바는 queue 를 linkedlist로 구현. offer로 추가 poll로 삭제
 */

// 그냥 new int[]로 넣어버리기
// class tomato {
//   int x;
//   int y;

//   tomato(int x, int y) {
//     this.x = x;
//     this.y = y;
//   }
// }

public class BOJ7576_Gd5_토마토 {

  static int m;
  static int n;

  static int[] dx = {-1, 1, 0, 0};
  static int[] dy = {0, 0, -1, 1};

  static int[][] graphs; // 토마토
  static Queue<int[]> que = new LinkedList<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());
    m = Integer.parseInt(st.nextToken());
    n = Integer.parseInt(st.nextToken());

    graphs = new int[n][m];
    
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        graphs[i][j] = Integer.parseInt(st.nextToken());
        if (graphs[i][j] == 1) que.add(new int[]{i, j});
      }
    }
    System.out.println(bfs());    
  }

  private static int bfs() {
    while (!que.isEmpty()) {
        int[] t = que.poll();
        int x = t[0];
        int y = t[1];

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (graphs[nx][ny] == 0) {
                graphs[nx][ny] = graphs[x][y] + 1;
                que.add(new int[]{nx, ny});
            }
        }
    }

      int max = Integer.MIN_VALUE;
      if (isZero()) {
          return -1;
      } else {
          for (int i = 0; i < n; i++) {
              for (int j = 0; j < m; j++) {
                  if (max < graphs[i][j]) {
                      max = graphs[i][j];
                  }
              }
          }

          return max - 1;
      }


  }

  private static boolean isZero() {
      for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
              if (graphs[i][j] == 0)
                  return true;
          }
      }
      return false;
  }

}