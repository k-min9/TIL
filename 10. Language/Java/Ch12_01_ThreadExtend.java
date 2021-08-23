package ch12;

public class Ch12_01_ThreadExtend {
	public static void main(String[] args) {
		//how1
		Thread thread = new BeepThread();
		
		thread.start();		
		
		for(int i=0; i<5; i++) {
			System.out.println("메인");
			try { Thread.sleep(500); } catch(Exception e) {}
		}
	}
}

//thread 클래스 상속하고 재정의
class BeepThread extends Thread {
	@Override
	public void run() {		

		for(int i=0; i<5; i++) {		
			System.out.println("서브");
			try { Thread.sleep(300); } catch(Exception e) {}
		}
	}
}