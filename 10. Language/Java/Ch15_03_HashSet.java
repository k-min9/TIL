package ch15;

import java.util.*;

public class Ch15_03_HashSet {
	public static void main(String[] args) {
		Set<String> set = new HashSet<String>();
		
		set.add("Java");
		set.add("JDBC");
		set.add("Servlet/JSP");
		set.add("Java");
		set.add("iBATIS");
		
		int size = set.size();
		System.out.println("객체 수: " + size);
		
		Iterator<String> iterator = set.iterator(); // 반복자 세팅
		//반복문 3(근데 이거 쓸거면 그냥 향상된 for이 낫다.)
		while(iterator.hasNext()) {
			String element = iterator.next();
			System.out.println(element);
		}
		
		System.out.println("====");
		
		set.remove("JDBC");
		set.remove("iBATIS");

		//반복문 2
		for(String element : set) {
			System.out.println(element);
		}
		
		set.clear();		
		if(set.isEmpty()) { System.out.println("비어있음"); }
	}
}


class Member {
	public String name;
	public int age;
	
	public Member(String name, int age) {
		this.name = name;
		this.age = age;
	}

	public boolean equals(Object obj) {
		if(obj instanceof Member) {
			Member member = (Member) obj;
			return member.name.equals(name) && (member.age==age) ;
		} else {
			return false;
		}
	}

	public int hashCode() {
		return name.hashCode() + age;
	}
}
