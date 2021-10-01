// 스트림 사용시 최종단계(반복, 카운팅, 평균, 총합) 수행 전에,
// 중간 단계에서 매핑, 필터링, 정렬 등을 수행할 수 있다.
package ch16;

import java.util.Arrays;
import java.util.List;

public class Ch16_02_StreamMappingFilteringSorting {
	public static void main(String[] args) {
		List<Student> studentList = Arrays.asList(
				new Student("student1", 10),
				new Student("student2", 20),
				new Student("student3", 30)
		);		
			
		double avg = studentList.stream()
			//중간처리(매핑)
			.mapToInt(Student :: getScore)
			//최종처리(평균)
			.average()
			.getAsDouble();
		
		System.out.println("평균값: " + avg);
	}
}

class Student {
	private String name;
	private int score;
	
	public Student (String name, int score) {
		this.name = name;
		this.score = score;
	}

	public String getName() { return name; }
	public int getScore() { return score; }
}

