package ch00;

public class Ch09_00_NestedClass {
	public static void main(String[] args) {
		A a = new A();
		
		//인스턴스 내부 클래스 선언
		A.B b = a.new B();
		b.method();
		
		//정적 내부 클래스 선언
		A.C c = new A.C();
		c.method();
		

	}
}

class A {
	int field1;
	void method1() {System.out.println("메소드1"); }
	
	static int field2;
	static void method2() {System.out.println("메소드2"); }
	
	class B {
		void method() {
			//모든 필드와 메소드에 접근 가능
			field1 = 10;
			method1();

			field2 = 10;
			method2();
		}
	}
	
	static class C {
		void method() {
			//인스턴스 필드와 메소드는 접근 못함
			//field1 = 10;
			//method1();

			field2 = 10;
			method2();
		}
	}	
}
