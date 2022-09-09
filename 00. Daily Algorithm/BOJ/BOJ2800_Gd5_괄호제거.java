import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.Stack;
import java.util.TreeSet;

/**
 * BOJ2800_Gd5_괄호제거
 * 문자열 + 스택 + dfs
 * () 인덱스를 저장하자
 */
public class BOJ2800_Gd5_괄호제거 {

	static List<int[]> brackets;
	static Set<String> result;
	static boolean[] visited;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		
    // 괄호 인덱스 정보 모음
		brackets = new ArrayList<>();
		Stack<Integer> s = new Stack<>(); // 열린괄호 임시
		for(int i=0; i<line.length(); i++) {
			char c = line.charAt(i);
			if(c == '(') {
				s.push(i);
			}else if(c == ')'){
				brackets.add(new int[] {s.pop(), i});
			}
		}
		
		visited = new boolean[line.length()];
		result = new TreeSet<>();  // ordered set!
		dfs(0, line.toCharArray());
		
		result.stream().forEach(System.out::println);
	}
	
	static void dfs(int depth, char[] str) {
		if(depth == brackets.size()) {
			boolean f = false;
			StringBuilder sb = new StringBuilder();
			for(int i=0; i<str.length; i++) {
				if(!visited[i]) {
					sb.append(str[i]);
				} else f = true;
			}
			if(f) {
				result.add(sb.toString());
			}
			return;
		}
		
		dfs(depth+1, str);
		
		int[] bracket = brackets.get(depth);
		visited[bracket[0]] = true;
		visited[bracket[1]] = true;
		dfs(depth+1, str);
		visited[bracket[0]] = false;
		visited[bracket[1]] = false;
	}
}