package ch11;

import java.util.Objects;

public class Ch11_06_methodisNULL {
	public static void main(String[] args) {		
		String str1 = "홍길동";
		String str2 = null;
		
		//비어있니, 안비어있니
		System.out.println(Objects.isNull(str2));
		System.out.println(Objects.nonNull(str2));
		
		//정상출력
		System.out.println(Objects.requireNonNull(str1));
		//none 반환타입이 총 세 종류
		try {
			String name = Objects.requireNonNull(str2);
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
		
		try {
			String name = Objects.requireNonNull(str2, "이름 없음");
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
		
		try {
			// () -> 람다식임
			String name = Objects.requireNonNull(str2, ()->"이름이 없다니까요");
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
