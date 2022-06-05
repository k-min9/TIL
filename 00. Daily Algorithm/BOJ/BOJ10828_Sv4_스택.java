import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * BOJ10828_Sv4_스택
 * 기초가 되는 스택 직접 만들어보기
 */


// 스택 클래스를 구현
class Stack {
  private int top; // 원소 위치
  private int arr[]; // 스택 구현에 사용할 배열

  // 생성자
  public Stack(int size) {
    this.top = -1;
    this.arr = new int[size];
  }

  // push
  public void push(int x) {
    this.arr[++top] = x;
  }

  // pop
  public int pop() {
    if (this.top == -1) return -1;
    return this.arr[top--];
  }

  // size
  public int size() {
    return this.top + 1;
  }

  // empty (원소 없으면 1, 아니면 0)
  public int empty() {
    if (this.top == -1) return 1;
    return 0;
  }

  // top
  public int top() {
    if (this.top == -1) return -1;
    return this.arr[top];
  }
}

public class BOJ10828_Sv4_스택 {
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // 입력
    int N = Integer.parseInt(br.readLine());

    Stack stack = new Stack(N);

    for (int i = 0; i < N; i++) {
      String query = br.readLine();

			if(query.contains("push")) {
				String spt[] = query.split(" ");
				stack.push(Integer.parseInt(spt[1]));
			} else if (query.contains("pop")) {
				bw.write(String.valueOf(stack.pop())+"\n"); 
			} else if (query.contains("size")) {
				bw.write(String.valueOf(stack.size())+"\n");
			} else if (query.contains("empty")) {
				bw.write(String.valueOf(stack.empty())+"\n"); 
			} else if (query.contains("top")) {
				bw.write(String.valueOf(stack.top())+"\n");
			}
    }

    bw.flush();
    bw.close();
    br.close();    
  }
}