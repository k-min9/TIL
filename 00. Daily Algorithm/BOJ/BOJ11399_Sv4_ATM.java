import java.util.Arrays;
import java.util.Scanner;

/**
 * BOJ11399_Sv4_ATM
 */
public class BOJ11399_Sv4_ATM {

  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int[] arr = new int[N];
    for (int i = 0; i < N; i++) {
      arr[i] = sc.nextInt();
    }

    Arrays.sort(arr);

    int now = 0;
    int answer = 0;

    for (int i = 0; i < N; i++) {
      answer += now + arr[i];
      now += arr[i];
    }

    System.out.println(answer);
    sc.close();

  }
}