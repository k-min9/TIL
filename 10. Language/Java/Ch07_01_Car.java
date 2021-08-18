package ch07;

public class Ch07_01_Car {
	//하나의 배열로 객체 관리
	Ch07_01_Tire[] tires = {
			new Ch07_01_Tire("앞L", 6),
			new Ch07_01_Tire("앞R", 2),
			new Ch07_01_Tire("뒤L", 3),
			new Ch07_01_Tire("뒤R", 4)
	};

	//for문으로 작성이 가능해진ㄴ다.
	int run() {
		System.out.println("[자동 running...]");
		for(int i=0; i<tires.length; i++) {	
			//펑크일시 false 반환
			if(tires[i].roll()==false) { 
				stop(); 
				return (i+1); 
			} 
		}
		return 0;
	}
	
	void stop() {
		System.out.println("[자동차 stop.]");
	}
}

