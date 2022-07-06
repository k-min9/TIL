package ch00;

public class Ch10_00_try_catch_finally {
	public static void main(String[] args) {
		String data1 = null;
		String data2 = null;	
		try { 
			int value1 = Integer.parseInt(data1);
			int value2 = Integer.parseInt(data2);
			int result = value1 + value2;
			System.out.println(data1 + "+" + data2 + "=" + result);
		} catch(NumberFormatException e) {
			System.out.println("숫자로 변환 불가");
		} finally {
			System.out.println("오류시 다시 실행");
		}
	}
}

