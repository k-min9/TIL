package ch06;

public class Ch06_00_class {
	public static void main(String[] args) {
		Car myCar = new Car();

		myCar.setSpeed(-50);		
		System.out.println("출력: " + myCar.getSpeed());

		myCar.setSpeed(60);
		System.out.println("출력: " + myCar.getSpeed());
		
		if(!myCar.isStop()) {
			myCar.setStop(true);
		}		
		System.out.println("출력: " + myCar.getSpeed());
	}
}
