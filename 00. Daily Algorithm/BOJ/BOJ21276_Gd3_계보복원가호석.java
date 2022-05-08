import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * BOJ21276_Gd3_계보복원가호석
 * 위상정렬 자바
 */
public class BOJ21276_Gd3_계보복원가호석 {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder bw = new StringBuilder();

    // 사람 수, 정보
    int N = Integer.parseInt(br.readLine());
    String[] names = new String[N];
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    for (int i = 0; i < N; i++) {
      names[i] = st.nextToken();
    }
    Arrays.sort(names);

    // 이름의 인덱스 번호를 map에 저장
    Map<String, Integer> map = new HashMap<>();
    for (int i = 0; i < N; i++) {
      map.put(names[i], i);
    }

    // 위상정렬용 자료구조
    int [] indegree = new int[N];
    boolean[][] adj = new boolean[N][N];
    int M = Integer.parseInt(br.readLine());
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine(), " ");
      int u = map.get(st.nextToken());
      int v = map.get(st.nextToken());
      adj[v][u] = true;
      indegree[u]++;
    }

    // 들어오는 간선이 없음 = 루트
    int cnt = 0;
		for (int i = 0; i < N; i++)
			if (indegree[i] == 0) cnt++;
		bw.append(cnt).append("\n");
		Queue<Integer> q = new LinkedList<>();

		// 사전순으로 출력해야하므로 정렬된 배열 names의 순서에 맞게 큐에 삽입
		for (int i = 0; i < N; i++) {
      if (indegree[i] == 0) {
        bw.append(names[i]).append(" ");
        // queue 추가(add)시 문제가 있을 경우 false 리턴, 그냥 add 써도 된다.
        q.offer(i);
      }
    }
		bw.append("\n");

		// i번째 정점의 자식들을 사전순으로 정렬하기 위해서 우선순위 큐 사용
		ArrayList<PriorityQueue<Integer>> T = new ArrayList<>(N);
		for (int i = 0; i <= N; i++) T.add(new PriorityQueue<>());

		for (int i = 0; i < N; i++) {
			// indegree가 0인 가장 조상인 정점을 뽑는다 (자바: poll = 파이썬 : appendleft)
			int here = q.poll();
			for (int there = 0; there < N; there++) {
        if (adj[here][there]) {
          indegree[there]--;
          // 새롭게 indgree가 0인 정점이 있으면 큐에 삽입
          // 마찬가지로 S는 정렬되어 있으므로 큐에는 오름차순으로 들어감
          if (indegree[there] == 0) {
            q.offer(there);
            T.get(here).offer(there);
          }
        }
      }
		}

    // 출력
		for (int i = 0; i < N; i++) {
			bw.append(names[i]).append(" ");
			bw.append(T.get(i).size()).append(" ");
			PriorityQueue<Integer> pq = T.get(i);
			while (!pq.isEmpty()) bw.append(names[pq.poll()]).append(" ");
			bw.append("\n");
		}
		System.out.print(bw);
    
  }
}