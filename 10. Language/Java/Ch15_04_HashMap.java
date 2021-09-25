package ch15;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class Ch15_04_HashMap {
	public static void main(String[] args) {
		//Map 생성
		Map<String, Integer> map = new HashMap<String, Integer>();
		
		//Map 저장
		map.put("student1", 85);
		map.put("student2", 90);
		map.put("student3", 80);
		map.put("student4", 95);
		System.out.println("총 인원: " + map.size());
		
		//Map 찾기(get)		
		System.out.println("\t student1 : " + map.get("student1"));
		System.out.println();
		
		//iterator 1
		Set<String> keySet = map.keySet();
		Iterator<String> keyIterator = keySet.iterator();
		while(keyIterator.hasNext()) {
		  String key = keyIterator.next();
		  Integer value = map.get(key);
		  System.out.println("\t" + key + " : " + value);
		}		
		System.out.println();	
		
		//Map 삭제
		map.remove("student1");
		System.out.println("총 인원: " + map.size());
		
		//iterator 2
		Set<Map.Entry<String, Integer>> entrySet = map.entrySet();
		Iterator<Map.Entry<String, Integer>> entryIterator = entrySet.iterator();
		while(entryIterator.hasNext()) {
		  Map.Entry<String, Integer> entry = entryIterator.next();
		  String key = entry.getKey();
		  Integer value = entry.getValue();
		  System.out.println("\t" + key + " : " + value);
		}
		System.out.println();
		
		//Map 초기화
		map.clear();
		System.out.println("총 인원: " + map.size());
	}
}

class Student {
	public int sno;
	public String name;
	
	public Student(int sno, String name) {
		this.sno = sno;
		this.name = name;
	}

	public boolean equals(Object obj) {
		if(obj instanceof Student) {
			Student student = (Student) obj;
			return (sno==student.sno) && (name.equals(student.name)) ;
		} else {
			return false;
		}
	}

	public int hashCode() {
		return sno + name.hashCode();
	}
}

