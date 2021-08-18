package ch07;

public class Ch07_01_inheritArray {
	public static void main(String[] args) {
		Ch07_01_Car car = new Ch07_01_Car();
		
		for(int i=1; i<=5; i++) {
			int problemLocation = car.run();
			//펑크난 타이어의 인덱스를 받는다.
			if(problemLocation != 0) {
				System.out.println(car.tires[problemLocation-1].location + " HankookTire로 교체");
				car.tires[problemLocation-1] = new Ch07_01_HankookTire(car.tires[problemLocation-1].location, 15);
			}
			System.out.println("----------------------------------------");
		}
	}
}


//동시에 두 군데 이상 펑크나지 않는다던가, 망가지기 전까지 앞에서부터만 망가진다던가 고칠점이 많은 코드