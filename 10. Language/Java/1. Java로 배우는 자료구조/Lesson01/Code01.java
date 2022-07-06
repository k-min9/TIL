// 변수 1
public class Code01 {

	// 외부 선언용 static
	static int num;

	public static void main(String[] args) {

		int anotherNum = 5;
		num = 2;
		
		System.out.println(num);
		System.out.println("another num : " + anotherNum);
	}
}