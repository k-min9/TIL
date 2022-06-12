/**
 * 자료구조 만들기 시리즈는 죄다 자바로 라이브 코딩 중
 * 그리고 만들어서 쓰는거라 그런지 스캐너라 그런지 하여튼 느리다... bw br 씁시당
 */
import java.util.Scanner;

class Queue{
	private int[] queue;
	private int frontIndex = 0;
	private int backIndex = -1;
	
	Queue(){
		
	}
	
	Queue(int number){
		queue = new int[number];
	}
	
	public void push(int x) {
		queue[++backIndex] = x;
	}
	
	public int size() {
		return backIndex - frontIndex + 1;
	}
	
	public boolean isEmpty() {
		if (size()==0)
			return true;
		else
			return false;
	}
	
	public int pop() {
		if (isEmpty())
			return -1;
		else
			return queue[frontIndex++];
	}
	
	public int front() {
		if (isEmpty())
			return -1;
		else
			return queue[frontIndex];
	}
	
	public int back() {
		if (isEmpty())
			return -1;
		else
			return queue[backIndex];
	}
	
}

public class BOJ10845_Sv4_큐 {

	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		int number = scanner.nextInt();
		Queue queue = new Queue(number);
		for(int i = 0; i <number; i++) {
			String command = scanner.next();
			switch(command) {
				case "push":
					int x = scanner.nextInt();
					queue.push(x);
					break;
				case "pop":
					System.out.println(queue.pop());
					break;
				case "empty":
					if (queue.isEmpty())
						System.out.println(1);
					else
						System.out.println(0);
					break;
				case "front":
					System.out.println(queue.front());
					break;
				case "back":
					System.out.println(queue.back());
					break;
				case "size":
					System.out.println(queue.size());
					break;
			}
		}
	}
}