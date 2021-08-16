package ch00;

public class Ch05_04_for_iterator {
	public static void main(String[] args) {
		int[] scores = { 95, 71, 84, 93, 87 };
		
		int sum = 0;
		// scores 부분이 계속 돌면서 작동함
		for (int score : scores) {
			sum = sum + score;
		}
		System.out.println("총합 = " + sum);
		
		double avg = (double) sum / scores.length;
		System.out.println("평균 = " + avg);
	} 
}
