package ch11;

//finalize는 객체가 가비지콜렉터에 줏어질때 시행됨

public class Ch11_04_methodFinalize {
	public static void main(String[] args) {
		Counter counter = null;
		for(int i=1; i<=50; i++) {
			counter = new Counter(i);
			//일부러 쓰레기 만들기
			counter = null;
			//가비지 콜렉터 부르는 메소드
			System.gc();
		}
	}
}

class Counter {
	private int no;
	
	public Counter(int no) {
		this.no = no;
	}
	
	@Override
	protected void finalize() throws Throwable {
		System.out.println(no + "번 객체의 finalize");
	}
}
