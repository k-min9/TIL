//Thread Safe인 HashMap

package ch15;

import java.util.*;

public class Ch15_05_HashTable {
	public static void main(String[] args) {
		Map<String, String> map = new Hashtable<String, String>();

		map.put("spring", "12");
		map.put("summer", "123");
		map.put("fall", "1234");
		map.put("winter", "12345");
		
		Scanner scanner = new Scanner(System.in);
		
		while(true) {
			System.out.println("아이디와 비밀번호를 입력해 주세요");
			System.out.print("아이디: ");
			String id = scanner.nextLine(); //입력한 아이디 읽기
			
			System.out.print("비밀번호: ");
			String password = scanner.nextLine(); // 입력한 비밀번호 읽기
			System.out.println();
			
			if(map.containsKey(id)) {//아이디 존재 확인
				if(map.get(id).equals(password)) {//비밀번호 일치 확인
					System.out.println("로그인 완료");
					break;
				} else {
					System.out.println("비밀번호 일치하지 않습니다.");
				}				
			} else {
				System.out.println("존재하지 않는 아이디입니다.");
			}
		}
	}
}
