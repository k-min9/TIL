package ch12;
// 스레드를 묶어서 관리

public class Ch12_08_ThreadGroup {
	public static void main(String[] args) {
		//myGroup에 두 스레드를 포함시킴
		ThreadGroup myGroup = new ThreadGroup("myGroup");
		WorkThread workThreadA = new WorkThread(myGroup, "workThreadA");
		WorkThread workThreadB = new WorkThread(myGroup, "workThreadB");
		
		workThreadA.start();
		workThreadB.start();
		
		//list : 현재 그룹 포함 스레드와 하위 그룹에 대한 정보를 출력한다.
		System.out.println("[ main 스레드 그룹의 list() 메소드 출력 내용]");
		ThreadGroup mainGroup = Thread.currentThread().getThreadGroup();		
		mainGroup.list();
		System.out.println();
		
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
		}
		
		System.out.println("[ myGroup 스레드 그룹의 interrupt() 메소드 호출 ]");
		//스레드 그룹의 메소드 interrupt : 이렇게 하면 스레드마다 interrupt할 필요 없어짐.
		myGroup.interrupt();
	}
}

class WorkThread extends Thread {
	public WorkThread(ThreadGroup threadGroup, String threadName) {
		super(threadGroup, threadName);
	}
	
	@Override
	public void run() {
		while(true) {
			try {
				Thread.sleep(1000);
				//interrupt 발생시, break로 빠져 나오게 설정
			} catch (InterruptedException e) {
				System.out.println(getName() + " interrupted");
				break;
			}
		}
		System.out.println(getName() + " 종료됨");
	}
}