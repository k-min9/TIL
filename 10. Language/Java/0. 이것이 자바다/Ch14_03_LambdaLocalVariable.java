package ch14;

public class Ch14_03_LambdaLocalVariable {
	public static void main(String... args) {
		UsingLocalVariable ulv = new UsingLocalVariable();
		ulv.method(20);
	}
}

class UsingLocalVariable {
	void method(int arg) {  //arg는 final 특성을 가짐
		int localVar = 40; 	//localVar는 final 특성을 가짐
		
		//arg = 31;  		//final 특성으로 수정 불가
		//localVar = 41; 	//final 특성으로 수정 불가
        
		//람다식 내부에서 읽는 것은 허용되지만, 람다식 내부 외부에서 변경은 불가능
		MyFunctionalInterface fi= () -> {
			//로컬 변수 읽기
			System.out.println("arg: " + arg); 
			System.out.println("localVar: " + localVar + "\n");
		};
		fi.method();
	}
}


//생략 가능하지만 추상 메소드 2개 선언 등을 고려해서 언제나 쓰자
@FunctionalInterface
interface MyFunctionalInterface4 {
    public void method();
}
