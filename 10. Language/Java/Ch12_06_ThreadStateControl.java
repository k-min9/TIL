package ch12;

//직접 상태를 제어해보자!
public class Ch12_06_ThreadStateControl {
	public static void main(String[] args) {
		StatePrintThread2 statePrintThread = new StatePrintThread2(new TargetThread2());
		statePrintThread.start();
	}
}

//상태 조사할 스레드
class StatePrintThread2 extends Thread {	
	private Thread targetThread;

	public StatePrintThread2(Thread targetThread) {
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
class TargetThread2 extends Thread {	
	public void run() {
		for(long i=0; i<1000000000; i++) {}
		
		//1. sleep = 일시 정지
		try {
			//1.5초 일시 정지 이때는 timed_waiting
			Thread.sleep(1500);
		} catch(Exception e) {}

		//2. yield = 예를 들어 무의미한 while 실행 중 이걸 넣으면, 리소스를 양보함
//		while(false) {
//			Thread.yield();
//		}
		
		//3. join = 다른 스레드의 종료를 기다림, 종료시 시행
		//다른스레드이름.join();
		
		//4. notify, wait 교대실행을 위한 메소드 
		//notify(); wait 상태의 thread를 실행대기로 변경
		//wait(); wait 상태로 변경
		
		//5. stop 플래그를 사용해서 자연스럽게 종료하기
//		private boolean stop
//		while(!stop) {
//			setstop등으로 플래그 조절, false 되는 순간 종료해버리기
//		}
		
		//6. interruptedException 발생 시켜서 스레드 종료하기
		//Thread.interrupt();
		
		//6.1 interrupted 사용해서 스레드 종료하기
		while(true){
			System.out.println();
			if(Thread.interrupted()) {
				break;
			}
		}
		
		for(long i=0; i<1000000000; i++) {}
	}
}
