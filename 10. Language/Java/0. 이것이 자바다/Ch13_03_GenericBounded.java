package ch13;

public class Ch13_03_GenericBounded {
	public static void main(String[] args) {
		//the type Util is not applicable for the arguments (String, String) 경고 뜸
		//String str = Util.compare("a", "b");
		
		int result1 = Util2.compare(10, 20);
		System.out.println(result1);
		
		int result2 = Util2.compare(4.5, 3);
		System.out.println(result2);
	}
}

class Util2 {
	//generic 속에 extends Number을 적으면 그 하윗값인 Byte, short, long 등만 들어올수있다.
	public static <T extends Number> int compare(T t1, T t2) {
		double v1 = t1.doubleValue(); 
		double v2 = t2.doubleValue();
		return Double.compare(v1, v2);
	}
}
