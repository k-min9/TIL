package ch12;

public class Ch12_02_ThreadName {
	public static void main(String[] args) {
		Thread mainThread = Thread.currentThread();
		System.out.println("메인 스레드: " + mainThread.getName());
		
		ThreadA threadA = new ThreadA();
		System.out.println("작업 스레드 A: " + threadA.getName());
		threadA.start();
		
		ThreadB threadB = new ThreadB();
		System.out.println("작업 스레드 B: " + threadB.getName());
		threadB.start();
	}
}

class ThreadA extends Thread {	
	public ThreadA() {
		//스레드 이름 설정
		setName("ThreadA");
	}
	
	public void run() {		
		for(int i=0; i<2; i++) {	
			//getName = thread 이름 얻기
			System.out.println(getName() + "가 출력중...");
		}
	}
}

class ThreadB extends Thread {	
	public void run() {		
		for(int i=0; i<2; i++) {		
			System.out.println(getName() + "가 출력중...");
		}
	}
}