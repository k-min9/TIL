package ch07;

public class Ch07_01_HankookTire extends Ch07_01_Tire {
	//초기화
	//super로 물려받기
	public Ch07_01_HankookTire(String location, int maxRotation) {
		super(location, maxRotation);
	}	
	//오버라이딩(재정의)
	@Override
	public boolean roll() {
		++accumulatedRotation;		
		if(accumulatedRotation<maxRotation) {
			System.out.println(location + " HankookTire 수명: " + (maxRotation-accumulatedRotation) + "회");
			return true;
		} else {
			System.out.println("*** " + location + " HankookTire 펑크");
			return false;
		}
	}
}
