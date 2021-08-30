package ch13;
//강한 타입 체크, 타입 변환을 최소화 하고, 성능을 향상한다.
public class Ch13_00_Generic {
	public static void main(String[] args) {
		//box 클래스 내부 T가 죄다 string으로 변한다.
		Box<String> box1 = new Box<String>();
		box1.set("hello");
		String str = box1.get();
		System.out.println(str);

		Box<Integer> box2 = new Box<Integer>();
		box2.set(6);
		int value = box2.get();
		System.out.println(value);
	}
}

class Box<T> {
	private T t;
	public T get() { return t; }
	public void set(T t) { this.t = t; }
}