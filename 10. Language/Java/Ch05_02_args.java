package ch00;
//Run -> Run configurations > arguments에서 입력값 제어 가능
public class Ch05_02_args {
	public static void main(String[] args) {
		//입력된 데이터 수 확인
		if(args.length != 2) {
			System.out.println("java MainStringArrayArgument num1 num2");
			//프로그램 강제종료
			System.exit(0);
		}
		
		//데이터 얻기
		String strNum1 = args[0];
		String strNum2 = args[1];
		
		//문자열 정수로 변환
		int num1 = Integer.parseInt(strNum1);
		int num2 = Integer.parseInt(strNum2);
		
		int result = num1 + num2;
		System.out.println(num1 + " + " + num2 + " = " + result);
	}
}
