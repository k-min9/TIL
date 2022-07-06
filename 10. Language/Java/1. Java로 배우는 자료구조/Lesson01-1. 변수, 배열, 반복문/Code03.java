import java.util.Scanner;

public class Code03 {
	public static void main(String[] args) {
		int number = 123;
		
		String str = "Hello World";
		String input;
		Scanner keyboard = new Scanner(System.in);
		System.out.print("문자열 입력 : ");

		// 하나의 문자열을 입력받는다. 라인통째로 = nextLine
//		input = keyboard.next(); // Hello World 입력시 Hello만 들어감
		input = keyboard.nextLine();

//		if(str == input) {
		if(str.equals(input)) {
			System.out.println("같음");
		} else {
			System.out.println("다름");
		}
		
		// 스캐너 닫기
		keyboard.close();
	}
}
