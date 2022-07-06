package ch15;

import java.util.*;

public class Ch15_00_ArrayList {
	public static void main(String[] args) {
		List<String> list = new ArrayList<String>();
		
		//String 객체 저장		
		list.add("Java");
		list.add("JDBC");
		list.add("Servlet/JSP");
		list.add(2, "Database"); //2번 인덱스에 삽입
		list.add("iBATIS");

		int size = list.size(); // 저장 객체 수
		System.out.println("총 객체 수: " + size);		
		System.out.println();
		
		String skill = list.get(2); // 2번 인덱스 객체
		System.out.println("2: " + skill);
		System.out.println();

		//반복문 예시
		for(int i=0; i<list.size(); i++) {
			String str = list.get(i);
			System.out.println(i + ":" + str);
		}
		System.out.println();
				
		//삭제 예시(인덱스, 객체 이름)
		list.remove(2);
		list.remove(2);
		list.remove("iBATIS");		
		
		//반복문 2
		for(String str : list) {
			System.out.println(str);
		}
		
		//초기화 Array.asList
		List<Integer> list2 = Arrays.asList(1, 2, 3);
		System.out.println(list2);
	}
}

