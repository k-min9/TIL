import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * 언어 : JAVA
 * BOJ1260_Sv2_DFS와BFS
 */
public class BOJ1260_Sv2_DFS와BFS {

  static ArrayList<Integer>[] graphs;
  static int n;
  static boolean[] visited;

  public static void dfs(int x) {
    if (visited[x]) return;

    visited[x] = true;
    System.out.print(x + " ");
    for (int y: graphs[x]) {
      if (!visited[y]) dfs(y);
    }
  }

  public static void bfs(int start) {
    Queue<Integer> queue = new LinkedList<>();
    queue.add(start);
    visited[start] = true;

    while (!queue.isEmpty()) {
      int x = queue.poll();
      System.out.print(x + " ");
      for (int y : graphs[x]) {
        if (!visited[y]) {
          visited[y] = true;
          queue.add(y);
        }
      }
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    int M = sc.nextInt();
    int start = sc.nextInt();

    graphs = new ArrayList[n+1];

    for (int i = 1; i< n+1; i++) {
      graphs[i] = new ArrayList<Integer>();
    }

    for (int i = 0; i < M; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();

      graphs[a].add(b);
      graphs[b].add(a);
    }

    for (int i = 1; i < n+1; i++) {
      Collections.sort(graphs[i]);
    }
    visited = new boolean[n+1];
    dfs(start);
    System.out.println();

    visited = new boolean[n+1];
    bfs(start);
    System.out.println();


    sc.close();
  }
}