
public class Ch03_00_BitOperator {
	public static void main(String[] args) {
		int v1 = 10;
		int v2 = ~v1;
		//-x = ~x + 1
		int v3 = ~v1 + 1;
		//to binary string
		System.out.println(toBinaryString(v1) + " : " + v1 + ")");
		System.out.println(toBinaryString(v2) + " : " + v2 + ")");
		System.out.println(toBinaryString(v3) + " : " + v3 + ")");
		//줄 변경 이렇게 하는 듯
		System.out.println();
		
		//원래도 리턴은 문자열
		System.out.println(Integer.toBinaryString(v1) + " : " + v3 + ")");
	}
	
	public static String toBinaryString(int value) {
		String str = Integer.toBinaryString(value);
		//length만큼 앞에 붙이기
		while(str.length() < 32) {
			str = "0" + str;
		}
		return str;
	}
}
