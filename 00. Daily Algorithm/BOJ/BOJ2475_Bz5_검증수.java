import java.util.Scanner;

/**
 * BOJ2475_Bz5_검증수
 */
public class BOJ2475_Bz5_검증수 {

  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);

    int sum = 0;
    for (int i = 0; i < 5; i++) {
      int temp = sc.nextInt();
      sum += temp * temp;      
    }
    sc.close();

    System.out.println(sum%10);
  }
}
