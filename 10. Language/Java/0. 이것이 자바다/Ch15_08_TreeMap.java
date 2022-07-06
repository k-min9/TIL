package ch15;

import java.util.Map;
import java.util.TreeMap;

public class Ch15_08_TreeMap {
	public static void main(String[] args) {
		TreeMap<Integer,String> scores = new TreeMap<Integer,String>();
		scores.put(87, "student1");
		scores.put(98, "student2");
		scores.put(75, "student3");
		scores.put(95, "student4");
		scores.put(80, "student5");
		
		//treeset과의 차이점 키와 값이 저장된 map.entry를 저장 << 그 부분만 꺼내서 밑에 예제
		Map.Entry<Integer, String> entry = null;
		
		entry = scores.firstEntry();
		System.out.println("가장 낮음: " + entry.getKey() + "-" + entry.getValue());
		
		entry = scores.lastEntry();
		System.out.println("가장 높음: " + entry.getKey() + "-" + entry.getValue() + "\n");
		
		entry = scores.lowerEntry(95);
		System.out.println("95점 아래: " + entry.getKey() + "-" + entry.getValue());
		
		entry = scores.higherEntry(95);
		System.out.println("95점 위: " + entry.getKey() + "-" + entry.getValue() + "\n");
		
		entry = scores.floorEntry(95);
		System.out.println("95 이하: " + entry.getKey() + "-" + entry.getValue());
		
		entry = scores.ceilingEntry(85);
		System.out.println("85 이상: " + entry.getKey() + "-" + entry.getValue() + "\n");
		
		while(!scores.isEmpty()) {
			entry = scores.pollFirstEntry(); //pop과 유사
			System.out.println(entry.getKey() + "-" + entry.getValue() + "(남은 객체 수: " + scores.size() + ")");
		}
	}
}
