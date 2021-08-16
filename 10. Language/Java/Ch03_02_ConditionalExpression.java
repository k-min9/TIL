
public class Ch03_02_ConditionalExpression {
	public static void main(String[] args) {
		int score = 85;
		// (조건)? then : else
		char grade = (score > 90) ? 'A' : ( (score > 80) ? 'B' : 'C' );
		System.out.println(score + "점은 " + grade + "등급입니다.");
	}
}
