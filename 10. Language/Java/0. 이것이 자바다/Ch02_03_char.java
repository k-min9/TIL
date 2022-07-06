
public class Ch02_03_char {
	public static void main(String[] args) {
		//문자직접 저장, 10진수 저장, 16진수 저장
		char c1 = 'A';          	
		char c2 = 65;          
		char c3 = '\u0041';    
		
		char c4 = '가';         	
		char c5 = 44032;      	
		char c6 = '\uac00';    
		
		//char 타입 변수를 int 타입 변수에 저장하면 유닛코드를 알 수 있음
		int uniCode = c1;
		
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
		System.out.println(c4);
		System.out.println(c5);
		System.out.println(c6);
		System.out.println(uniCode);
	} 
}
