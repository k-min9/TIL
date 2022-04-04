import java.util.Scanner;

/**
 * BOJ2588_Bz4_곱셈
 */
public class BOJ2588_Bz4_곱셈 {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int n1 = in.nextInt();
    int n2 = in.nextInt();
    in.close();

    int answer1 = n1 * (n2 % 10);
    int answer2 = n1 * (n2/10 % 10);
    int answer3 = n1 * (n2 / 100);
    int answer4 = n1 * n2;

    System.out.println(answer1);
    System.out.println(answer2);
    System.out.println(answer3);
    System.out.println(answer4);
    
  }
}