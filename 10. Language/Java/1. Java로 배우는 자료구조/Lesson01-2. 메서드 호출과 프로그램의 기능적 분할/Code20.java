package Section02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * 
 * @author M9
 * 외부 파일로 부터 이름과 전화번호 쌍을 받은 후 이름 알파벳 순서로 정렬하기
 *
 */
public class Code20 {
	
	// 클래스 전체에서 사용될 데이터는 클래스의 멤버로 만드는 것이 좋다.
	static String[] name;
	static String[] number;
	static int count = 0;
	
	public static void main(String[] args) throws FileNotFoundException {
		String fileName = "Code19_input.txt";
		Scanner sc = new Scanner(new File(fileName));	// 파일 프로젝트 최상단에 둘 것
		
		name = new String[100];
		number = new String[100];
		
		while (sc.hasNext()) {
			name[count] = sc.next();
			number[count] = sc.next();
			count++;
		}		
		sc.close();
		
		bubbleSort();
		
		for (int i = 0; i < count; i++) {
			System.out.println("이름 : " + name[i] + ", 번호 : " + number[i]);
		}
	}
	
	public static void bubbleSort() {
		for (int i = count-1; i>0; i--) {
			for (int j = 0; j < i; j++) {
				// java에서의 문자열 순서 비교 (대소문자 구별 없이 옵션)
				if (name[j].compareToIgnoreCase(name[j+1])>0) {
					// swap 이름
					String tmpName = name[j];
					name[j] = name[j+1];
					name[j+1] = tmpName;
					
					// swap 번호
					String tmpNumber = number[j];
					number[j] = number[j+1];
					number[j+1] = tmpNumber;
				}
				
			}
			
		}
	}
}