package ch08;

interface Tire {
	public void roll();
}

class Car {
	Tire[] tires = {
		new HankookTire(),
		new HankookTire(),
		new HankookTire(),
		new HankookTire()
	};
	
	void run() {
		for(Tire tire : tires) {
			tire.roll();
		}
	}
}

class HankookTire implements Tire {
	@Override
	public void roll() {
		System.out.println("한국 바퀴 롤링.");
	}
}

class KumhoTire implements Tire {
	@Override
	public void roll() {
		System.out.println("금호 바퀴 롤링.");
	}
}

public class Ch08_02_InterfaceArray {
	public static void main(String[] args) {
		Car myCar = new Car();
		
		myCar.run();
		
		//인터페이스 교체
		myCar.tires[0] = new KumhoTire();
		myCar.tires[1] = new KumhoTire();
		
		myCar.run();
	}
}


