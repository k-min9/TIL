package Section02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
/**
 * 
 * @author M9
 * 외부 파일을 읽어서 이름과 전화번호를 분리
 */
public class Code19 {
	public static void main(String[] args) throws FileNotFoundException {
		
		String fileName = "Code19_input.txt";
		Scanner sc = new Scanner(new File(fileName));	// 파일 프로젝트 최상단에 둘 것
		
		String[] name = new String[100];
		String[] number = new String[100];
		
		int i = 0;		
		while (sc.hasNext()) {
			name[i] = sc.next();
			number[i] = sc.next();
			i++;
		}		
		sc.close();
		
		for (int j = 0; j < i; j++) {
			System.out.println("이름 : " + name[j] + ", 번호 : " + number[j]);
		}
	}

}
