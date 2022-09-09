import java.util.Scanner;

/**
 * BOJ2884_Bz3_알람시계
 */
public class BOJ2884_Bz3_알람시계 {

  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);
    int H = sc.nextInt();
    int M = sc.nextInt();

    if (M>=45) {
      M -= 45;
    } else {
      H += 23;
      H %= 24;  // 자바는 음수 나머지가 허용 됨
      M += 15;
    }

    System.out.println(H + " " + M);

    sc.close();

  }
}

// 45분 일찍이라니 악마다;;