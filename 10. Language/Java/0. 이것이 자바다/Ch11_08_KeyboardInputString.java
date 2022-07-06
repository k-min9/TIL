package ch11;

import java.io.IOException;

public class Ch11_08_KeyboardInputString {
	public static void main(String[] args) throws IOException {
		byte[] bytes = new byte[100];
		
		//입력 받기
		System.out.print("입력: ");
		int readByteNo = System.in.read(bytes);

		// 캐리지리턴(\r), 라인피드(\n) 두개는 필요 없어서 뺀다.
		String str = new String(bytes, 0, readByteNo-2);
		System.out.println(str);
	}
}
