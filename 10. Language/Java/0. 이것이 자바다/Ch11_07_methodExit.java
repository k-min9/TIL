package ch11;


//JVM 강제 종료. 일반적으로 exit(0)가 정상 종료를 의미하는 말이라고 한다.
public class ExitExample {
	public static void main(String[] args)  {
		for(int i=0; i<10; i++) {
			System.out.println(i);
			//JVM 강제종료
			if(i == 5) {
				System.exit(i);
			}
		}
	}
}

