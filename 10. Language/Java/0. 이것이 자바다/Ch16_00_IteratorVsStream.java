//스트림 : 함수적 스타일로 처리
package ch16;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Stream;

public class Ch16_00_IteratorVsStream {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("사람 1", "사람 2", "사람 3");
		
		//Iterator (길다)
		Iterator<String> iterator = list.iterator();
		while(iterator.hasNext()) {
			String name = iterator.next();
			System.out.println(name);
		}
		
		System.out.println("=========");
		
		//Stream (단순)
		Stream<String> stream = list.stream();
		stream.forEach( name -> System.out.println(name) );
	}
}
