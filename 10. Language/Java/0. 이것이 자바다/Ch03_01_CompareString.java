
public class Ch03_01_CompareString {
	public static void main(String[] args) {
		
		//1과 2는 같은 곳을 참조한다. new로 만든 3은 그렇지 않다.
		String strVar1 = "강민구";
		String strVar2 = "강민구";
		String strVar3 = new String("강민구");

		System.out.println( strVar1 == strVar2);
		System.out.println( strVar1 == strVar3);
		System.out.println();
		//값을 비교하는 메소드
		System.out.println( strVar1.equals(strVar2));
		System.out.println( strVar1.equals(strVar3));
	}
}
