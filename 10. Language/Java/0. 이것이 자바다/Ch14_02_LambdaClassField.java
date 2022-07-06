package ch14;

public class Ch14_02_LambdaClassField {
	public static void main(String... args) {
		UsingThis usingThis = new UsingThis();
		UsingThis.Inner inner = usingThis.new Inner();
		inner.method();
	}
}

class UsingThis {
	public int outterField = 10;

	class Inner {
		int innerField = 20;

		void method() {
			//람다식(Ch14_00 유용)
			MyFunctionalInterface3 fi= () -> {
				System.out.println("outterField: " + outterField);
				//Using this 이후의 this로 바깥 객체의 참조가 가능
				System.out.println("outterField: " + UsingThis.this.outterField + "\n");
				
				System.out.println("innerField: " + innerField);
				//그냥 this만 쓸 경우 람다식을 실행한 객체(inner)를 참조한다.
				System.out.println("innerField: " + this.innerField + "\n");
			};
			fi.method();
		}
	}
}

@FunctionalInterface
interface MyFunctionalInterface3 {
    public void method();
}