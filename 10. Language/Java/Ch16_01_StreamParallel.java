//Stream은 내부 반복자를 사용하므로 병렬처리가 쉽다. >> 효율적 요소 반복
package ch16;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class Ch16_01_StreamParallel {	
	public static void main(String[] args) {
		List<String> list = Arrays.asList(
				"student1",
				"student2",
				"student3",
				"student4",
				"student5");
		
		//순차 처리(s -> Ch16_01_StreamParallel.print(s)와 동일)
		Stream<String> stream = list.stream();
		stream.forEach(Ch16_01_StreamParallel :: print);
		
		System.out.println("======");
		
		//병렬 처리, ForkJoinPool(스레드풀)
		Stream<String> parallelStream = list.parallelStream();
		parallelStream.forEach(Ch16_01_StreamParallel :: print);
	}
	
	public static void print(String str) {
		System.out.println(str+ " : " + Thread.currentThread().getName());
	}	
}
