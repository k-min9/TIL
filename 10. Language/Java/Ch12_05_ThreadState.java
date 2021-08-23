package ch12;

public class Ch12_05_ThreadState {
	public static void main(String[] args) {
		StatePrintThread statePrintThread = new StatePrintThread(new TargetThread());
		statePrintThread.start();
	}
}

//상태 조사할 스레드
class StatePrintThread extends Thread {	
	private Thread targetThread;

	public StatePrintThread(Thread targetThread) {
		this.targetThread = targetThread;
	}

	public void run() {
		while(true) {
			//getState = 스레드 상태 얻기
			Thread.State state = targetThread.getState();
			System.out.println("target thread 상태: " + state);
			//객체 생성 상태
			if(state == Thread.State.NEW) {
				//일단 runnable 상태, 그 다음 running 상태로
				targetThread.start();
			}
			//모든 작업이 종료됨
			if(state == Thread.State.TERMINATED) {
				break;
			}
			try {
				//0.5초 일시 정지
				Thread.sleep(500);
			} catch(Exception e) {}
		}
	}
}

//상태 조사 될 스레드
class TargetThread extends Thread {	
	public void run() {
		for(long i=0; i<1000000000; i++) {}
		
		try {
			//1.5초 일시 정지 이때는 timed_waiting
			Thread.sleep(1500);
		} catch(Exception e) {}
		
		for(long i=0; i<1000000000; i++) {}
	}
}
