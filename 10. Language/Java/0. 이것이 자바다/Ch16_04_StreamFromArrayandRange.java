package ch16;

import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Ch16_04_StreamFromArrayandRange {
	public static void main(String[] args) {
		//String[] 은 strStream 사용
		String[] strArray = { "student2", "student1", "student3"};
		Stream<String> strStream = Arrays.stream(strArray);
		strStream.forEach(a -> System.out.print(a + ","));
		System.out.println();
		
		//int[] 은 intStream 사용
		int[] intArray = { 1, 2, 3, 4, 5 };
		IntStream intStream = Arrays.stream(intArray);
		intStream.forEach(a -> System.out.print(a + ","));
		System.out.println();
				
		//intRange도 intStream 사용
		IntStream stream = IntStream.rangeClosed(1,  10);
		stream.forEach(a -> System.out.print(a + ","));
	}
	
}
