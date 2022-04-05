import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * 언어 : java
 * Hashmap 연습겸...
 */

/**
 * BOJ1755_Sv4_숫자놀이
 */
public class BOJ1755_Sv4_숫자놀이 {

  // 상수 (숫자-> 문자로 변환시 사용할 배열)
  static String numToString[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};

  public static void main(String[] args) throws Exception {
    // 입력
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    sc.close();

    // 계산
    char[] temp = new char[2];  // 두자리 숫자용
    String strTemp ="";
    String[] result = new String[M-N+1];
    Map<String, Integer> mapTemp = new HashMap<>();
    for (int i=N; i<=M; i++) {
      temp = String.valueOf(i).toCharArray(); // 숫자->문자
      strTemp = "";
      for (int j=0; j<temp.length; j++) {
        strTemp += numToString[temp[j]-'0'];
        strTemp += " ";
      }
      //변환값을 키로, 숫자를 value로
      mapTemp.put(strTemp, i);
      result[i-N] = strTemp;
    }

    // 알파벳 기준 오름차순 정렬후 출력
    Arrays.sort(result);
    int cnt = 0;
    for (String str: result) {
      System.out.print(mapTemp.get(str)+ " ");
      cnt++;
      if (cnt == 10) {
        cnt = 0;
        System.out.print("\n");
      }
    }
  }
}
