import java.util.Scanner;

public class Code02 {

	public static void main(String[] args) {
		int number = 123;
		
		// System.in : 표준 입력
		// Scanner(키보드로부터 데이터를 입력받기 위한 객체) 제작
		Scanner keyboard = new Scanner(System.in);

		System.out.print("정수 123 입력: ");  // 줄 안바꿈

		// 하나의 정수를 입력받는다
		int input = keyboard.nextInt();

		if(input == number) {
			System.out.println("같음");
		} else {
			System.out.println("다름");
		}
		
		// 스캐너 닫기
		keyboard.close();
	}
}