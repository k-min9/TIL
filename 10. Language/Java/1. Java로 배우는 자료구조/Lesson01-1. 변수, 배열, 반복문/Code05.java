// 배열의 선언과 할당
public class Code05 {
	public static void main(String[] args) {
		
		int[] grades;
	
		grades = new int[5];
		
		grades[0] = 100;
		grades[2] = 72;
		
		System.out.println(grades[1]);
		System.out.println(grades[2]);
		System.out.println("---");
		
		/**
		 * 반복문		
		 */
		for (int i = 0; i < grades.length; i++) {
			System.out.println("Grades " + (i+1) + " : " + grades[i]);
		}
		
		System.out.println("---");		
		int i = 0;
		while (i < grades.length) {
			System.out.println("Grades " + (i+1) + " : " + grades[i]);
			i++;
		}
	}
}
