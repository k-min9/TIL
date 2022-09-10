import java.util.Scanner;

/**
 * BOJ10809_Bz5_알파벳찾기
 * charAt, indexOf ... 
 */
public class BOJ10809_Bz5_알파벳찾기 {

  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);
    String S = sc.next();

    int[] answers = new int[26];
    // Arrays.fill(arr, -1); 와 동일
    for (int i = 0; i < answers.length; i++) {
      answers[i] = -1;
    }
    
    for (int i = 0; i < S.length(); i++) {
      char ch = S.charAt(i);
      if(answers[ch - 'a'] == -1) answers[ch - 'a'] = i; 
    }

    for(int answer : answers) {
      System.out.print(answer + " ");
    }
    sc.close();
  }
}