package ch12;

import java.awt.Toolkit;

public class Ch12_00_ThreadNew {
	//메인 스레드
	public static void main(String[] args) {
		//Runnable : run만 존재하는 함수적 인터페이스
		Runnable beepTask = new BeepTask();
		//작업 스레드 생성
		Thread thread = new Thread(beepTask);
		//작업 스레드 실행
		thread.start();
		
		for(int i=0; i<5; i++) {
			System.out.println("띵");
			//0.5초간 일시정지
			try { Thread.sleep(500); } catch(Exception e) {}
		}
	}
}
//인터페이스 함수 정의
class BeepTask implements Runnable {	
	public void run() {		
		Toolkit toolkit = Toolkit.getDefaultToolkit();	
		for(int i=0; i<20; i++) {
			System.out.println("똥");
			toolkit.beep();
			try { Thread.sleep(200); } catch(Exception e) {}
		}
	}
}

