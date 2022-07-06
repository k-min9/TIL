
//이진트리 기반 Set 컬렉션
package ch15;

import java.util.TreeSet;

public class Ch15_06_TreeSet {
	public static void main(String[] args) {
		TreeSet<Integer> scores = new TreeSet<Integer>();
		scores.add(87);
		scores.add(98);
		scores.add(75);
		scores.add(95);
		scores.add(80);
		
		Integer score = null;
		
		score = scores.first();
		System.out.println("가장 낮은 점수: " + score);
		
		score = scores.last();
		System.out.println("가장 높은 점수: " + score + "\n");
		
		score = scores.lower(95);
		System.out.println("95점 아래: " + score);
		
		score = scores.higher(95);
		System.out.println("95점 위: " + score + "\n");		
		
		score = scores.floor(95);
		System.out.println("95점이거나 아래: " + score);
		
		score = scores.ceiling(85);
		System.out.println("85점 이거나 위: " + score + "\n");
		
		while(!scores.isEmpty()) {
			score = scores.pollFirst(); // 제일 낮은 객체를 꺼내오고 컬렉션에서 제거 함
			System.out.println(score + "(남은 객체 수: " + scores.size() + ")");
		}
	}
}
