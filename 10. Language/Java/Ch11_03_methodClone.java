package ch11;

import java.util.Arrays;

//얕은 복제 : 클래스내의 배열 같은 참조값을 제외하고는 제대로 원하는 복제가 이루어진다.
public class Ch11_03_methodClone {
	public static void main(String[] args) {
		//원본
		Member2 original = new Member2("blue", "홍길동", "12345", 25, true);
		
		//얕은복제 + 패스워드 변경
		Member2 cloned = original.getMember();
		cloned.password = "67890";
		
		System.out.println("[복제]");
		System.out.println("id: " + cloned.id);
		System.out.println("name: " + cloned.name);
		System.out.println("password: " + cloned.password);
		System.out.println("age: " + cloned.age);
		System.out.println("adult: " + cloned.adult);
		
		System.out.println();
		
		System.out.println("[원본]");
		System.out.println("id: " + original.id);
		System.out.println("name: " + original.name);
		System.out.println("password: " + original.password);
		System.out.println("age: " + original.age);
		System.out.println("adult: " + original.adult);
	}
}

//cloneable을 표시해줘서 명시적으로 클론 가능함을 표기
class Member2 implements Cloneable {
	public String id;
	public String name;
	public String password;
	public int age;
	public boolean adult;
	
	Member2(String id,  String name, String password, int age, boolean adult ) {
		this.id = id;
		this.name = name;
		this.password = password;
		this.age = age;
		this.adult = adult;
	}
	
	Member2 getMember() {
		Member2 cloned = null;
		try {
			//method clone의 반환값은 object라 casting이 필요
			cloned = (Member2) clone();
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
		}
		return cloned;
	}
}


//깊은 복제시 아래와 같은 clone 메소드 재정의가 필요
//@Override
//protected Object clone() throws CloneNotSupportedException {
//	Member cloned = (Member) super.clone();
//	cloned.scores = Arrays.copyOf(this.scores, this.scores.length);
//	cloned.car = new Car(this.car.model);
//	return cloned;
//}