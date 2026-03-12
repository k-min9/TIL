import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * SortExample
 */
public class SortExample {

  public static void main(String[] args) {
    // 입력
    String numsStrList = "500, 2000, 90, 0";
    String[] numStrs = numsStrList.split(",");

    List<BigDecimal> nums = new ArrayList<>();
    for (String numStr: numStrs) {
      nums.add(new BigDecimal(numStr.trim()));
    } 

    // sort
    Collections.sort(nums);

    // 확인
    for (BigDecimal num:nums) {
      System.out.println(num.toString());
    }

  }
}