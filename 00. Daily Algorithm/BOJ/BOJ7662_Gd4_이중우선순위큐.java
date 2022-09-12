import java.util.*;
import java.io.*;

/**
 * 언어 : java
 * 학습사항 : treemap에 대해 학습하자
 * 개요 : 키와 map, entry를 저장함. 자동으로 오름차순 정렬. 레드 블랙트리 사용
 * 정렬이 필요한 상황에서는 Hashmap보다 효율적!
 * 출처 : https://coding-factory.tistory.com/557
 */
public class BOJ7662_Gd4_이중우선순위큐 {
	static TreeMap<Integer, Integer> treeMap = new TreeMap<>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int t=0; t<T; t++) {
			int Q = Integer.parseInt(br.readLine());
			
			while(Q-->0) {
				st = new StringTokenizer(br.readLine());
				String func = st.nextToken();
				int num = Integer.parseInt(st.nextToken());
				
				if(func.equals("I")) input(num); 
				else delete(num); 
			}
            
			if(treeMap.isEmpty()) sb.append("EMPTY").append('\n');
			else sb.append(treeMap.lastKey()).append(' ').append(treeMap.firstKey()).append('\n');
			
			treeMap.clear();
		}

		bw.write(sb.toString()); bw.flush(); bw.close();
	} // End of main
	
	private static void input(int num) {
		treeMap.put(num, treeMap.getOrDefault(num, 0)+1);
	} // End of input
	
	private static void delete(int num) {
		
		if(treeMap.isEmpty()) return;
		else if(num == 1) { // 최댓값 삭제
			int maxNum = treeMap.lastKey();
			int defaultNum = treeMap.get(maxNum);
			if(defaultNum == 1) treeMap.remove(maxNum); // default수가 1이면 해당 key삭제
			else treeMap.put(maxNum, defaultNum-1); // 1이상이면 해당 key의 value를 value-1로 갱신
	
		}
		else if(num == -1) { // 최솟값 삭제
			int minNum = treeMap.firstKey();
			int defaultNum = treeMap.get(minNum);
			if(defaultNum == 1) treeMap.remove(minNum); // default수가 1이면 해당 key삭제
			else treeMap.put(minNum, defaultNum-1); // 1이상이면 해당 key의 value를 value-1로 갱신
		}
		
	} // End of delete
} // End of Main class