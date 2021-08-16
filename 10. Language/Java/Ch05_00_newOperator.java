package ch00;

public class Ch05_00_newOperator {
	public static void main(String[] args) {
		//new 연산자 사용시, 같은 참조값을 쓰지 않는다
		String name = new String("강민구");
		String chk = new String("강민구");
		
		System.out.println(name == chk);
		System.out.println(name.equals(chk));
	}
}
