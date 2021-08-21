package ch11;

//객체의 문자정보 반환, 기초정보가 너무 하찮아서 다들 재정의해서 쓴다.
public class Ch11_02_methodToString {
	public static void main(String[] args) {
		SmartPhone myPhone = new SmartPhone("구글", "안드로이드");
		
		String strObj = myPhone.toString();
		//방법 1, 2
		System.out.println(strObj);		
		System.out.println(myPhone);
	}
}

class SmartPhone {
	private String company;
	private String os;
	
	public SmartPhone(String company, String os) {
		this.company = company;
		this.os = os;
	}
	
	@Override
	public String toString() {
		return company + ", " + os;
	}
}
