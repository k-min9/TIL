import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

/**
 * DBDummyGenerator
 */
public class DBDummyGenerator {

  private static HashMap<String, Object> choicesMap = new HashMap<>();
  private static List<String> choicesList = new ArrayList<>();  // 선택지 이름들
  private static List<HashMap<String, Object>> insertDatas = new ArrayList<HashMap<String, Object>>();

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String tableName = "테이블이름";

    int tableDepth = 0;

    // 조합용 기초자료
    /////////////////////////////////////////////////////////
    choicesMap.put("키값", Arrays.asList("01", "02"));
    choicesMap.put("입력자번호", Arrays.asList("99999"));
    choicesMap.put("입력일시", Arrays.asList("1959-01-01-00 00.00.00000"));
    /////////////////////////////////////////////////////////

  }

}