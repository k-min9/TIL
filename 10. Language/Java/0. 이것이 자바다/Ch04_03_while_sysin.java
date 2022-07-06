
public class Ch04_03_while_sysin {
	public static void main(String[] args) throws Exception {
		boolean run = true;		
		int speed = 0;
		int keyCode = 0;
		
		while(run) {
			//엔터 입력시 캐리지(13)와 라인(10)이 입력되므로 그걸 방지
			if(keyCode!=13 && keyCode!=10) {
				System.out.println("-----------------------------");
				System.out.println("1.가속 | 2. 감속 | 3. 중지");
				System.out.println("-----------------------------");
				System.out.print("선택: ");
			}
			
			//이게 키 받는 함수
			keyCode = System.in.read();
			
			if (keyCode == 49) { //1
				speed++;
				System.out.println("현재 속도=" + speed);
			} else if (keyCode == 50) { //2
				speed--;
				System.out.println("현재 속도=" + speed);
			} else if (keyCode == 51) { //3
				run = false;
			}
		}	
		
		System.out.println("프로그램 종료");
	}
}
