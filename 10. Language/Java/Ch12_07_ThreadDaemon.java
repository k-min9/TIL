package ch12;

// 데몬 스레드 : 주 스레드를 돕는 보조적인 역할을 수행. 주 스레드 종료시 강제 종료
public class Ch12_07_ThreadDaemon {
	public static void main(String[] args) {
		AutoSaveThread autoSaveThread = new AutoSaveThread();
		autoSaveThread.setDaemon(true);
		autoSaveThread.start();
		
		try {
			Thread.sleep(3300);
		} catch (InterruptedException e) {
		}
		
		System.out.println("메인 종료");
	}
}

//1초 주기로 save() 메소드를 호출하는 데몬 스레드
class AutoSaveThread extends Thread {
	public void save() {
		System.out.println("작업내용을 저장");
	}
	
	@Override
	public void run() {
		while(true) {
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				break;
			}
			save();
		}
	}
}