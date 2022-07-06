package ch14;

public class Ch14_00_LambdaNoParaNoReturn { 
	public static void main(String[] args) {
		MyFunctionalInterface fi;
		
		//(매개변수) -> {실행코드}
		fi= () -> { 
			String str = "method call1";
			System.out.println(str);
		};
		fi.method();
		
		fi = () -> { System.out.println("method call2"); };
		fi.method();
		
		//매개변수가 하나일 경우와, 실행문이 하나 일경우는 각각 괄호 생략 가능
		fi = () -> System.out.println("method call3");
		fi.method();
	}
}

//인터페이스에 람다식을 대입한다.
@FunctionalInterface
interface MyFunctionalInterface {
    public void method();
}











