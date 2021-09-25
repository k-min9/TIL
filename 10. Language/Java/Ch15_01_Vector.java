//ArrayList와 가장 큰 차이점 : 동기화된 메소드로 구성되어있어서 멀티스레드가 동시에 실행할 수 없다.
// 안전하게 객체를 추가하고 삭제할 수 있는 Thread Safe가 보장

package ch15;

import java.util.List;
import java.util.Vector;

public class Ch15_01_Vector {
	public static void main(String[] args) {
		List<Board> list = new Vector<Board>();
	
		list.add(new Board("title1", "content1", "writer1"));
		list.add(new Board("title2", "content2", "writer2"));
		list.add(new Board("title3", "content3", "writer3"));
		list.add(new Board("title4", "content4", "writer4"));
		list.add(new Board("title5", "content5", "writer5"));
		
		list.remove(2);
		list.remove(3);
		
		for(int i=0; i<list.size(); i++) {
			Board board = list.get(i);
			System.out.println(board.subject + "\t" + board.content + "\t" + board.writer);
		}
	}
}

class Board {
	String subject;
	String content;
	String writer;
	public Board(String subject, String content, String writer) {
		this.subject = subject;
		this.content = content;
		this.writer = writer;
	}
}
