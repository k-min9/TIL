import java.util.Scanner;

/*
 * 언어 : java
 * java 컴파일 관련 config 수정 후 멀쩡한지 체크하는 겸
 * setting.json에 "code-runner.executorMap": { "java": "cd $dir && javac $fileName -encoding utf-8 && java $fileNameWithoutExt" } 추가
 */

 /**
  * BOJ1259_Bz1_팰린드롬
  */
 public class BOJ1259_Bz1_팰린드롬 {
 
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    while (true) {
      String text = sc.next();
      if ("0".equals(text)) {
        sc.close();
        System.exit(0);
      }
      
      int N = text.length();

      String[] arr = new String[N];
      String[] arr2 = new String[N];

      // reverse 하기
      for (int i=0; i<N; i++) {
        arr[i] = text.substring(i, i+1);
        arr2[i] = text.substring(N-i-1, N-i);
      }

      int count = 0;
      for (int i=0; i<N; i++) {
        if(arr[i].equals(arr2[i])) count++;
      }

      if (count == N) {
        System.out.println("yes");
      } else {
        System.out.println("no");
      }
    }
  }
}
