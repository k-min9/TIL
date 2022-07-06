package ch16;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class Ch16_03_StreamFromCollection {
	public static void main(String[] args) {
		List<Student> studentList = Arrays.asList(
			new Student("student1", 10),
			new Student("student2", 20),
			new Student("student3", 30)
		);
		
		//Stream<T>		
		Stream<Student> stream = studentList.stream();
		stream.forEach(s -> System.out.println(s.getName()));
	}
}

//학생 클래스 Ch16_02것 일단 사용