
public class Ch02_06_casting {
	public static void main(String[] args) {	
		//강제 casting (char)
		//int intValue = 44032;
		int intValue = 103029770;
		char charValue = (char) intValue;
		System.out.println(charValue);
		
		long longValue = 500;
		intValue = (int) longValue;
		System.out.println(intValue);
		
		double doubleValue = 3.14;
		intValue = (int) doubleValue;
		System.out.println(intValue);	
	} 
}
