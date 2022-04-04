/**
 * 자바 강화 기간
 * 스택 문제
 */
import java.util.Scanner;
import java.util.Stack;
 
// 제출시 Main
public class BOJ9012_Sv4_괄호 {
 
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		in.close();
		
		for(int i = 0; i < T; i++) {
			System.out.println(solve(in.next()));	// nextLine()쓰면 안된다.
		}
	}
 
	public static String solve(String s) {
 
		Stack<Character> stack = new Stack<>();
 
		for (int i = 0; i < s.length(); i++) {
 
			char c = s.charAt(i);
 
			// 여는 괄호일 경우 스택에 넣는다.
			if (c == '(') {
				stack.push(c);
			}
 			// 아래는 모두 닫는 괄호 일 경우들이다.
			// 스택이 비어있는 경우. 즉, 닫는 괄호를 입력받았으나 pop할 원소가 없을 경우
			else if (stack.empty()) {
				return "NO";
			}
			// 그 외의 경우 stack 원소를 pop 한다.
			else {
				stack.pop();
			}
		}
 
		/*
		 * 모든 검사 마치고 스택에 잔여 요소가 있으면 여는 괄호가 많은 경우는 "NO" 
		 * 스택이 비어있으면 온전한 수식이므로 "YES" 이다.
		 */

		if (stack.empty()) {
			return "YES";
		} 
		else {
			return "NO";
		}
	}
}