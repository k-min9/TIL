package ch00;

public class Ch10_02_ExceptionThrow {
	public static void main(String[] args) {
		try {
			findClass();
		} catch(ClassNotFoundException e) {
			System.out.println("클래스없음 에러를 여기서 처리하는거임");
		}
	}
	
	//throw로 던질 경우
	public static void findClass() throws ClassNotFoundException {
		Class clazz = Class.forName("java.lang.String2");
	}
}

