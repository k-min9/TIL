package ch07;

public class Ch07_01_Tire {
	//필드(타이어 수명, 누적 회전수, 타이어 위치)
	public int maxRotation;     		
	public int accumulatedRotation;		
	public String location;       			

	//생성자
	public Ch07_01_Tire(String location, int maxRotation) {
		this.location = location;
		this.maxRotation = maxRotation;
	}

	//메소드
	public boolean roll() {
		//누적하고 펑크 여부
		++accumulatedRotation;		
		if(accumulatedRotation<maxRotation) {
			System.out.println(location + " Tire 수명: " + (maxRotation-accumulatedRotation) + "회");
			return true;
		} else {
			System.out.println("*** " + location + " Tire 펑크");
			return false;
		}
	}
}

