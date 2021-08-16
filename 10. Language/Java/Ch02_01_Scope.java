
public class Ch02_01_Scope {
	public static void main(String[] args) {
		int v1 = 15;
		if(v1>10) {
			int v2;
			v2 = v1 - 10;
			System.out.println(v2);
			v1 = v1 - 10;
		}
		System.out.println(v1);
		//작동 안함
		//System.out.println(v2);
	} 
}
