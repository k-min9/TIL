import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

/**
 * DB의 성격을 이해하고 적절한 샘플을 넣는 것을 보조한다.
 */
public class TableSampleGenerator {
  
  private static HashMap<String, Object> choicesMap = new HashMap<String, Object>(); // column이 가질 수 있는 경우의 수 모음

  private static HashSet<String> keysSet = new HashSet<String>();  // key인 column의 set
  private static List<String> keysList = new ArrayList<String>();  // key인 column의 List
  private static List<String> choicesList = new ArrayList<String>();  // key가 아닌 column의 List
  
  private static List<HashMap<String, Object>> insertDataNormal = new ArrayList<HashMap<String, Object>>();  // key 아닌 insertData
  private static List<HashMap<String, Object>> insertDataKey = new ArrayList<HashMap<String, Object>>();  // key관련 insertData
  private static List<HashMap<String, Object>> insertDatas = new ArrayList<HashMap<String, Object>>();  // 위 insertData를 합친 최종본

  public static void main(String[] args) throws SQLException, ClassNotFoundException {
    Scanner scanner = new Scanner(System.in);
    String tableName = "테이블 이름";

    int j = 0;  // loop용 더미 데이터

    /********************* 묻지 않고 choiceMap에 넣는 기초 데이터 일람 (우선 0순위)***********************/
    choicesMap.put("미리넣고싶은컬럼이름", Arrays.asList("값후보1", "값후보2", "값후보3"));
    choicesMap.put("생성자이름", Arrays.asList("k-min9"));
    choicesMap.put("생성자ID", Arrays.asList("mingu4969"));
    choicesMap.put("생성날짜", Arrays.asList("1999-01-01-00.00.00.0000"));
    choicesMap.put("수정자이름", Arrays.asList("k-min9"));
    choicesMap.put("수정자ID", Arrays.asList("mingu4969"));
    choicesMap.put("수정날짜", Arrays.asList("2019-01-01-00.00.00.0000"));
    /**************************************************************************************************/

    Class.forName("com.ibm.db2.jcc.DB2Driver");  // 사용하는 DB의 Driver 정보로 

    String url = "jdbc:db2://1.1.1.1:8010/테스트";
    String user = "kmin9";
    String password = "password1234";

    Connection conn = DriverManager.getConnection(url, user, password);

    try {
      DatabaseMetaData metaData = conn.getMetaData();
      ResultSet rs = metaData.getColumns(null, "스키마이름", tableName, null);
      ResultSet rsPk = metaData.getPrimaryKeys(null, "스키마이름", tableName);  // PK 구분을 위한 metadata를 구해서 set에 넣어둔다.
      while (rsPk.next()) {
        String pk = rsPk.getString("COLUMN_NAME");
        keysSet.add(pk);
      }

      initChoiceSetting(conn, rs, scanner, tableName);  // 입력값 입력 또는 보조 등으로 insertData 제작을 위한 combination 수행 전 후보군 생성

      // INSERT 쿼리 제작
      StringBuilder sb = new StringBuilder();
      sb.append("INSERT INTO 스키마.").append(tableName).append(" ()");
      for (int i = 0; i<keysList.size(); i++) {
        sb.append(keysList.get(i));
        if (i < keysList.size() -1) sb.append(", ");
      }
      sb.append(", ");
      for (int i = 0; i<choicesList.size(); i++) {
        sb.append(choicesList.get(i));
        if (i < choicesList.size() -1) sb.append(", ");
      }
      sb.append(") VALUES (");
      for (int i = 0; i < keysList.size(); i++) {
        sb.append("?");
        if (i < keysList.size() -1) sb.append(", ");
      }
      sb.append(", ");
      for (int i = 0; i < choicesList.size(); i++) {
        sb.append("?");
        if (i < choicesList.size() -1) sb.append(", ");
      }  
      sb.append(")");

      // insertData 만들기
      dfsKey(keysList, keysList.size(), 0, new HashMap<String, Object>());
      dfsNormal(choicesList, choicesList.size(), 0, new HashMap<String, Object>());
      insertDatas = mergeHashMapList(insertDataKey, insertDataNormal);

      // 선택전 예시 몇가지 보여주기
      System.out.println("예시 ==================================================================");
      j = 0;
      StringBuilder sb2 = new StringBuilder();
      for (HashMap<String, Object> insertData : insertDatas) {
        for (Map.Entry<String, Object> entry : insertData.entrySet()) {
          sb2.append(entry.getKey()).append(":").append(entry.getValue()).append(", ");
        }
        sb2.append(System.lineSeparator());
        j++;
        if(j>5) break;  // 일단 최대 5줄
      }
      System.out.println(sb2.toString());
      System.out.println("Enter를 눌러 계속 진행해 주세요... ======================================");

      String inputStr = scanner.nextLine();
      while(!(inputStr == null || "".equals(inputStr.trim()))) {
        inputStr = scanner.nextLine();
      }

      // insert 전 확인
      System.out.println(insertDatas.size() + "개의 값을 입력하시겠습니까? [y]입력으로 실행합니다.");
      inputStr = scanner.nextLine();

      // insert 수행
      if ("Y".equals(inputStr) || "y".equals(inputStr)) {
        for (HashMap<String, Object> insertData : insertDatas) {
          PreparedStatement pstmt = conn.prepareStatement(sb.toString());
          j = 1;
          for (String keyStr:keysList) {
            pstmt.setString(j, insertData.get(keyStr).toString());
            j++;
          }
          for (String choiceStr:choicesList) {
            pstmt.setString(j, insertData.get(choiceStr).toString());
            j++;
          }
          pstmt.executeUpdate();
          pstmt.close();
        }
        System.out.println("입력 완료");
      } else {
        System.out.println("입력 취소");
      }

      conn.close(); // 혹시... 몰라서...
      System.out.println("프로그램 종료");

    } catch (Exception e) {

    } finally {
      conn.close();
      System.out.println("연결 종료");
    }

  }

  /**
   * insertData 제작을 위한 combination 수행 전 후보군 생성
   * keysList, choicesList 식별 및 choiceMap 조립
   */
  private static void initChoiceSetting(Connection conn, ResultSet rs, Scanner scanner, String tableName) throws SQLException {

    while (rs.next()) {
      // rs에서 정보 추출
      String columnName = rs.getString("COLUMN_NAME");
      String dataType = rs.getString("TYPE_NAME");
      int ColumnSize = rs.getInt("COLUMN_SIZE");
      boolean columnNullable = rs.getBoolean("NULLABLE"); // 고도화 여지 : 후보군에 null을 넣을 수 있지 않을까? SetNull을 위한 타입 저장용 자료구조가 필요하다!
      String columnRemarks = rs.getString("REMARKS");  // 일반적으로 remark에 table에 대한 한글 설명이 있음
      boolean isPk = keysSet.contains(columnName);  // 이 column이 key인지

      // keysList, choicesList 식별
      if (isPk) {
        keysList.add(columnName);
      } else {
        choicesList.add(columnName);
      }

      // 0 순위에 해당 내용에 관한 후보 및 정보가 mapping 되어 있으면 다음 column으로
      if (choicesMap.containsKey(columnName)) continue;

      // 후보군 입력 받기(출력형식 - FRUIT_NO:과일번호/TYPE:CHAR,size:3,nullable:false,pk:false)
      System.out.println(columnName+":"+columnRemarks+"/type:"+dataType+",size:"+ColumnSize+",nullable:"+columnNullable+",pk:"+isPk); 
      if (isPk) {
        System.out.println(columnName+"가 가질수 있는 값을 입력해주세요 (k 입력시 자동 채번모드) : ");  // PK column은 자동채번모드 지원
      } else {
        System.out.println(columnName+"가 가질수 있는 값을 입력해주세요 : ");
      }
      String inputStr = scanner.nextLine();

      // 입력이 없을 경우 그럴싸한 후보군 추가
      if (inputStr == null || "".equals(inputStr.trim())) {
        if (columnName.endsWith("_CLCD") || columnName.endsWith("_CFCD") || columnName.endsWith("_CD") || columnName.endsWith("_SEQ")) {
          choicesMap.put(columnName, Arrays.asList("01", "02"));  // 고도화 여지 : size도 가지고 있겠다 적절한 길이의 String을 만들 수 있던거 아닐까?
        } else if (columnName.endsWith("_NM")) {
          List<String> names = new ArrayList<String>();
          names.add(generateKorName());
          names.add(generateKorName());
          names.add(generateKorName());

          choicesMap.put(columnName, names);
        } else if (columnName.endsWith("_BGDT")) {
          choicesMap.put(columnName, Arrays.asList("2000-01-01"));
        } else if (columnName.endsWith("_ENDDT")) {
          choicesMap.put(columnName, Arrays.asList("2010-01-01"));
        } else {
          choicesMap.put(columnName, Arrays.asList("1", "2", "3"));
        }
      } else { // 입력이 있음
        if (isPk && "k".equals(inputStr.trim())) {  // 자동채번 모드
          String nextNum = getTableStrNumMax(conn, tableName, columnName);
          System.out.println("자동채번모드("+nextNum+" 에서 시작) : 채번할 key의 수를 입력하여 주세요(기본값 3).");
          inputStr = scanner.nextLine();
          int loopNum;  // 고도화 : 입력된다면 값이 숫자인지 validation이 있어야 함
          if (inputStr == null || "".equals(inputStr.trim())) {
            loopNum = 3;
          } else {
            loopNum = Integer.parseInt(inputStr);
          }

          List<String> values = new ArrayList<String>();
          for (int i = 0; i < loopNum; i++) {
            values.add(nextNum);
            nextNum = nextStrNum(nextNum);
          }
          choicesMap.put(columnName, values);
        } else { //평범히 입력한 후보군
          String[] inputArr = inputStr.split(" ");
          List<String> inputList = new ArrayList<String>();
          for (String str: inputArr) {  // 고도화 여지 : 자료구조 -> 자료구조 변동이 이렇게까지 불편한가...?
            inputList.add(str);
          }
          choicesMap.put(columnName, inputList);
        }
      }
    }
  }


  /**
   * 후보군으로 사용할 수 있게 랜덤한 한글 이름을 조립하여 만들어줌 
   * -> 고도화 여지 : 아예 중복하지 않게 ArrayList로 만들어서 반환하는건 어땠을까??
   * -> combination이 아니라 한번만 사용하고 버리게 하는 로직을 어떻게 넣을지 고민할 필요가 있음
   */
  private static String generateKorName() {
    String[] words1 = {"빠른", "행복한", "멋진", "즐거운"};
    String[] words2 = {"사과", "바나나", "포도", "참외", "하마", "사자"};
    String[] words3 = {"이름"};

    Random random = new Random();
    StringBuilder sb = new StringBuilder();
    sb.append(words1[random.nextInt(words1.length)]);
    sb.append(words2[random.nextInt(words2.length)]);
    sb.append(words3[random.nextInt(words3.length)]);

    return sb.toString();
  }

  /*
   * String형 key의 MAX 식 채번
   */
  private static String getTableStrNumMax(Connection conn, String tableName, String pkColumnName) throws SQLException {
    Statement stmt = conn.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT NVL(MAX("+pkColumnName+"), '0') FROM 스키마." + tableName);

    String maxPk = "";
    if (rs.next()) {
      maxPk = rs.getString(1);
    }
    maxPk = nextStrNum(maxPk);

    return maxPk;
  }

    /*
   * int형 key의 MAX 식 채번 
   * 고도화 여지 -> 제네릭 쓰면 위 함수와 하나로 통일할 수 있지 않을까? 굳이?
   */
  // private static int getTableNumMax(Connection conn, String tableName, String pkColumnName) throws SQLException {
  //   Statement stmt = conn.createStatement();
  //   ResultSet rs = stmt.executeQuery("SELECT NVL(MAX("+pkColumnName+"), '0') FROM 스키마." + tableName);

  //   int maxPk = 0;
  //   if (rs.next()) {
  //     maxPk = rs.getInt(1);
  //   }
  //   maxPk = maxPk + 1;

  //   return maxPk;
  // }

  /**
   * String 형태의 숫자를 1 증가시키고 자리수 및 0을 유지
   * 00009 -> 00010. AS005 -> AS006
   * 숫자부분을 1 증가시키고 자리 수 및 0을 유지 (고도화 : 자리수가 커졌을때의 예외 설정하지 않았음)
   */
  private static String nextStrNum(String curNum) {
    StringBuilder sb = new StringBuilder();

    // 숫자부분 추출
    int numStartIdx = curNum.length();
    while (numStartIdx > 0 && Character.isDigit(curNum.charAt(numStartIdx -1))) {
      numStartIdx--;
    }

    String strPart = curNum.substring(0, numStartIdx);
    String numPart = curNum.substring(numStartIdx);
    int nextNum = Integer.parseInt(numPart) + 1;
    numPart = String.format("%0"+numPart.length()+"d", nextNum);

    sb.append(strPart);
    sb.append(numPart);
    
    return sb.toString();
  }

  /**
   * key인 column의 후보군 combination 제작
   */
  private static void dfsKey(List<String> keyList, int depth, int index, HashMap<String, Object> data) {
    if (depth == index) {
      insertDataKey.add(data);
      return;
    }

    List<String> choices = (List<String>)choicesMap.get(keyList.get(index));
    for (int i = 0; i< choices.size(); i++) {
      HashMap<String, Object> nextData = (HashMap<String, Object>)data.clone();
      nextData.put(keyList.get(index), choices.get(i));
      dfsKey(keyList, depth, index+1, nextData);
    }
  }

    /**
   * key가 아닌 column의 후보군 combination 제작
   */
  private static void dfsNormal(List<String> choiceList, int depth, int index, HashMap<String, Object> data) {
    if (depth == index) {
      insertDataNormal.add(data);
      return;
    }

    List<String> choices = (List<String>)choicesMap.get(choiceList.get(index));
    for (int i = 0; i< choices.size(); i++) {
      HashMap<String, Object> nextData = (HashMap<String, Object>)data.clone();
      nextData.put(choiceList.get(index), choices.get(i));
      dfsKey(choiceList, depth, index+1, nextData);
    }
  }

  /**
   * HashMap List merge하기
   */
  private static List<HashMap<String, Object>> mergeHashMapList(List<HashMap<String, Object>> list1, List<HashMap<String, Object>> list2) {
    List<HashMap<String, Object>> mergedList = new ArrayList<>();

    int listSize = Math.min(list1.size(), list2.size());
    for (int i = 0; i<listSize ; i++) {
      HashMap<String, Object> mergedHashMap = new HashMap<String, Object>();
      mergedHashMap.putAll(list1.get(i));
      mergedHashMap.putAll(list2.get(i));
      mergedList.add(mergedHashMap);
    }

    return mergedList;
  }
}
