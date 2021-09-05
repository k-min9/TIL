package ch14;

public class Ch14_01_LambdaYesParaYesReturn { 
	public static void main(String[] args) {
		MyFunctionalInterface2 fi;
		
		//return 값이 중괄호 안에 있어야한다.
		fi = (x, y) -> {
			int result = x + y;
			return result;
		};
		System.out.println(fi.method(2, 5));
		
		fi = (x, y) -> { return x + y; };
		System.out.println(fi.method(2, 5));
		
		//return 문만 있을 경우 괄호와 return 생략 가능
		fi = (x, y) -> x + y;
		System.out.println(fi.method(2, 5));
		
		//return 문만 있을 경우 괄호와 return 생략 가능
		fi = (x, y) -> sum(x, y);
		System.out.println(fi.method(2, 5));
	}
	
	public static int sum(int x, int y) {
		return (x + y);
	}
}

// x와 y 두개의 parameter를 갖는 함수를 가지는 interface
@FunctionalInterface
interface MyFunctionalInterface2 {
	public int method(int x, int y);
}











