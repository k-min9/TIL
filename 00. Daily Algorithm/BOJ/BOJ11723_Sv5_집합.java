import java.util.*;

/**
 * N이 적으니 on off로 해도 된다. 근데 목적이 그게 아님
 * hashset을 이해해보자
 * add, remove, check 전부 O(1)
 */
public class BOJ11723_Sv5_집합 {
   
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      StringBuilder sb = new StringBuilder();
      int m = sc.nextInt();  // 연산 수
      Set<Integer> set = new HashSet<>(); // 중복 허용 X
      
      for (int i = 0; i < m; i++) {
         String cal = sc.next();
         int x = 0;
         
         switch (cal) {
            case "add" :
               x = sc.nextInt();
               set.add(x);
               break;   
            case "remove" :
               x = sc.nextInt();
               set.remove(x);
               break;
            case "check" :
               x = sc.nextInt();
               if (set.contains(x))
                  sb.append("1\n");
               else
                  sb.append("0\n");
               break;
            case "toggle" :
               x = sc.nextInt();
               if (set.contains(x))
                  set.remove(x);
               else
                  set.add(x);
               break;   
            case "all" :
               for (int k = 0; k < 20; k++) {
                  set.add(k + 1);
               }
               break;
            case "empty" :
               set.clear();
               break;               
         }
      }

      System.out.print(sb.toString());
      sc.close();
   }
}