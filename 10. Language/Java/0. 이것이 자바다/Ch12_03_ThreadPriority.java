package ch12;

//자바 스레드 스케쥴러. 수동 : 우선순위 방식, 자동 : Round Robin(순환 할당)
public class Ch12_03_ThreadPriority {
	public static void main(String[] args) {
		for(int i=1; i<=10; i++) {
			//set name으로 스레드 이름 넣음
			Thread thread = new CalcThread("thread" + i);
			if(i != 10) {
				//최소 우선도 : 1
				//thread.setPriority(Thread.MIN_PRIORITY);
				thread.setPriority(i);
			} else {
				//최대 우선도 : 10 (높을수록 좋음)
				thread.setPriority(Thread.MAX_PRIORITY);
			}
			thread.start();
		}
	}
}

class CalcThread extends Thread {
	public CalcThread(String name) {
		setName(name);
	}
	
	public void run() {
		for(int i=0; i<2000000000; i++) {
		}
		System.out.println(getName());
	}
}
