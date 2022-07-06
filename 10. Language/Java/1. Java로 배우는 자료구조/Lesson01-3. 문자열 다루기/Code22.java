package section03;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * 
 * @author M9
 * 파일에 해당 단어가 등장한 횟수를 출력
 * 명령어 리스트
 * read 파일이름 : 파일 읽기
 * find 단어 : 단어 존재 여부와 횟수 출력
 * saveas 파일이름 : 파일이름으로 인덱스 저장
 * exit : 나가기
 */
public class Code22 {
	
	static String[] words = new String[100000];  // 단어 목록 저장
	static int[] count = new int[100000];  // 단어 등장 횟수
	static int n;  // 저장된 단어 갯수
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.print("$ ");  // 프롬프트용
			String command = sc.next();
			if (command.equals("read")) {
				String fileName = sc.next();
				makeIndex(fileName);
			} else if (command.equals("find")) {
				String keyword = sc.next();
				int index = findWord(keyword);
				if (index != -1)
					System.out.println("등장 횟수 : " + count[index]+ "회");
				else {
					System.out.println("해당 단어는 등장하지 않았습니다.");
				}
			} else if (command.equals("saveas")) {
				String fileName = sc.next();
				saveAs(fileName);
			} else if (command.equals("exit")) {
				break;
			}
		}
		sc.close();
	}
	
	static void makeIndex(String fileName) throws FileNotFoundException {
		Scanner file = new Scanner(new File(fileName));
		while(file.hasNext()) {
			String word = file.next();
			addWord(word);
		}
		file.close();
	}
	
	static void addWord(String word) {
		int index = findWord(word);
		if (index >-1) {
			count[index]++;
		} else {
			words[n] = word;
			count[n] = 1;
			n++;
		}
	}
	
	/**
	 * @param keyword
	 * @return 있으면 배열 index 없으면 -1을 반환
	 */
	static int findWord(String keyword) {
		for (int i = 0; i < n; i++) {
			if (words[i].equals(keyword)) {
				return i;
			}
		}
		return -1;
	}
	
	static void saveAs(String fileName) throws IOException {
		PrintWriter out = new PrintWriter(new FileWriter(fileName));
		for (int i = 0; i < n; i++) {
			out.println(words[i] + " " + count[i]);
		}
		out.close();
	}

}
