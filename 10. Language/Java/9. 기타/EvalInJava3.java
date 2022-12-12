/**
 * Double 에서 BigDecimal로 바꾸고 
 * 단순연산을 최적화하고
 * 다중 소괄호를 활성화하자.
 */
import java.util.ArrayList;
import java.util.HashMap;

import java.math.BigDecimal;

public abstract class EvalInJava3 {

    private static final String alphabetic = "abcdefghilmnopqrstuvzwykxy";
    private static final String numeric = "0123456789.";
    private static final String alphanumeric = alphabetic+numeric;
    private static final String operators = "*/+-"; // 계산 우선 순위 별 나열임. 함부로 변경하지 말 것

    public static void main(String[] args) throws NoSuchMethodException, IllegalAccessException, IllegalArgumentException {
        // 순수 연산
        System.out.println(solveNumericExpression("1+3*9"));

        // 기본 + 띄어쓰기 대응
        HashMap<String, Object> values = new HashMap<>();
        values.put("x", "4");
        System.out.println(solve("x-3", values));
        System.out.println(solve("x- 3", values));
        System.out.println(solve("x -3", values));
        System.out.println(solve("x - 3", values));
        System.out.println("---");

        // 다중 키
        HashMap<String, Object> values2 = new HashMap<>();
        values2.put("x", "4");
        values2.put("y", "6.2");
        values2.put("z", "-8.5");
        values2.put("a", "-200");
        System.out.println(solve("x * ((y - 1) * (y+10)) * (z-10)", values2));  // 꼭 모든 변수 다 쓸 필요도 없음       

        // 보조함수 체크중
        // System.out.println(Arrays.asList(usableMathMethods()));
    }

  public static Object solveNumericExpression (String expression) throws NoSuchMethodException, IllegalAccessException, IllegalArgumentException 
  {
      return solve(expression, new HashMap<>());
  }
  
  public static Object solve (String function, HashMap<String, Object> values) throws NoSuchMethodException, IllegalAccessException, IllegalArgumentException 
  {
  
      return solveBracketsFunction(function, function, values);
  }
  
  // 소, 중, 대괄호를 function의 형태로 hashmap에 넣고 괄호 없는 연산으로 변경
  // ex : a * (b+c) 를 a* x 로 변환하고 hashmap에 key : x, value b+c를 저장
  private static Object solveBracketsFunction (String function,String motherFunction,HashMap<String, Object> values) throws IllegalArgumentException {
  
      function = function.replace(" ", "");  // 띄어쓰기 삭제
      String openingBrackets = "({[";
      String closingBrackets = ")}]";
      int parenthesisIndex = 0;
      do {
          int position = 0;
          int openParenthesisBlockIndex = -1;
          String currentOpeningBracket = openingBrackets.charAt(parenthesisIndex)+"";
          String currentClosingBracket = closingBrackets.charAt(parenthesisIndex)+"";
          if (contOccouranceIn(currentOpeningBracket,function) != contOccouranceIn(currentClosingBracket,function)) {
              throw new IllegalArgumentException("Error: brackets are misused in the function "+function);
          }
          while (position < function.length()) {
              if (function.substring(position,position+1).equals(currentOpeningBracket)) {
                  openParenthesisBlockIndex = position;
              }else if (function.substring(position,position+1).equals(currentClosingBracket)) {
                  String newKey = getNewKey(values);
                  values.put(newKey, solveBracketsFunction(function.substring(openParenthesisBlockIndex+1,position),motherFunction, values));
                  function = function.substring(0, openParenthesisBlockIndex)
                            + newKey
                            + ((position == function.length()-1)?(""):(function.substring(position+1)));
                  position = -1;
              }
              position++;
          }
          parenthesisIndex++;
      } while (parenthesisIndex < openingBrackets.length());
      return solveBasicFunction(function,motherFunction, values);
  }
  
  private static Object solveBasicFunction (String function, String motherFunction, HashMap<String, Object> values) throws IllegalArgumentException{
  
    //   function = function.replace(" ", ""); // 띄어쓰기 삭제 이미 실행
      int position;
      int operatorIndex = 0;
      String currentOperator;
      do {
          currentOperator = operators.substring(operatorIndex, operatorIndex+1);
          // 1순위 op
          if (currentOperator.equals("*")) {
              currentOperator+="/";
              operatorIndex++;
          // 2순위 op
          } else if (currentOperator.equals("+")) {
              currentOperator+="-";
              operatorIndex++;
          }
          operatorIndex++;

          position = 0; //current operation의 position
          while (position < function.length()) {
            // 오류 체크
            //   if ((position == 0 && !(""+function.charAt(position)).equals("-") && !(""+function.charAt(position)).equals("+") && operators.contains(""+function.charAt(position))) ||
            //       (position == function.length()-1 && operators.contains(""+function.charAt(position)))){
            //       throw new IllegalArgumentException("Operators are misused in the function");
            //   }
              if (currentOperator.contains(function.substring(position, position+1)) & position != 0) {
                  int firstTermBeginIndex = position;

                  while (firstTermBeginIndex > 0) {
                      if ((alphanumeric.contains(""+function.charAt(firstTermBeginIndex))) & (operators.contains(""+function.charAt(firstTermBeginIndex-1)))){
                          break;
                      }
                      firstTermBeginIndex--;
                  }
                  if (firstTermBeginIndex != 0 && (function.charAt(firstTermBeginIndex-1) == '-' | function.charAt(firstTermBeginIndex-1) == '+')) {
                      if (firstTermBeginIndex == 1) {
                          firstTermBeginIndex--;
                      }else if (operators.contains(""+(function.charAt(firstTermBeginIndex-2)))){
                          firstTermBeginIndex--;
                      }
                  }
                  String firstTerm = function.substring(firstTermBeginIndex,position);

                  int secondTermLastIndex = position;
                  while (secondTermLastIndex < function.length()-1) {
                      if ((alphanumeric.contains(""+function.charAt(secondTermLastIndex))) & (operators.contains(""+function.charAt(secondTermLastIndex+1)))) {
                          break;
                      }
                      secondTermLastIndex++;
                  }
                  String secondTerm = function.substring(position+1,secondTermLastIndex+1);

                  Object result;
                  switch (function.substring(position,position+1)) {
                      case "*": result = (Object)(solveSingleValue(firstTerm,values).multiply(solveSingleValue(secondTerm,values))); break;
                      case "/": result = (Object)(solveSingleValue(firstTerm,values).divide(solveSingleValue(secondTerm,values))); break;
                      case "+": result = (Object)(solveSingleValue(firstTerm,values).add(solveSingleValue(secondTerm,values))); break;
                      case "-": result = (Object)(solveSingleValue(firstTerm,values).subtract(solveSingleValue(secondTerm,values))); break;
                      default: throw new IllegalArgumentException("Unknown operator: "+currentOperator);
                  }

                  // 소규모 계산 결과 저장
                  String newAttribute = getNewKey(values);
                  values.put(newAttribute, result);
                  function = function.substring(0,firstTermBeginIndex)+newAttribute+function.substring(secondTermLastIndex+1,function.length());
                  deleteValueIfPossible(firstTerm, values, motherFunction);
                  deleteValueIfPossible(secondTerm, values, motherFunction);
                  position = -1;
              }
              position++;
          }
      }while (operatorIndex < operators.length());
      return solveSingleValue(function, values);
  }
  
  private static BigDecimal solveSingleValue (String singleValue, HashMap<String, Object> values) throws IllegalArgumentException{
  
      if (isBigDecimal(singleValue)) {
          return new BigDecimal(singleValue);
      }else if (firstContainsOnlySecond(singleValue, alphabetic)){
          return getBdValueFromMap(singleValue, values);
      }else if (firstContainsOnlySecond(singleValue, alphanumeric+"-+")) {
          String[] composition = splitByLettersAndNumbers(singleValue);
          if (composition.length != 2) {
              throw new IllegalArgumentException("Wrong expression: "+singleValue);
          }else {
              if (composition[0].equals("-")) {
                  composition[0] = "-1";
              }else if (composition[1].equals("-")) {
                  composition[1] = "-1";
              }else if (composition[0].equals("+")) {
                  composition[0] = "+1";
              }else if (composition[1].equals("+")) {
                  composition[1] = "+1";
              }
              if (isBigDecimal(composition[0])) {               
                return new BigDecimal(composition[0]).multiply(getBdValueFromMap(composition[1], values));
              } else if (isBigDecimal(composition[1])){
                return new BigDecimal(composition[1]).multiply(getBdValueFromMap(composition[0], values));
              } else {
                  throw new IllegalArgumentException("Wrong expression: "+singleValue);
              }
          }
      }else {
          throw new IllegalArgumentException("Wrong expression: " + singleValue);
      }
  }
  
  private static BigDecimal getBdValueFromMap (String variable, HashMap<String, Object> values) throws IllegalArgumentException
  { 
      Object val = values.get(variable);
      BigDecimal ret = null;
      if (val == null) {
          throw new IllegalArgumentException("Unknown variable: "+variable);
      } else {
        if (val instanceof String) {
            ret = new BigDecimal((String) val);
        } else if (val instanceof BigDecimal) {
            ret = (BigDecimal) val;
        }        
      }
      return ret;
  }
  
  private static boolean firstContainsOnlySecond(String firstString, String secondString) {
      for (int j = 0 ; j < firstString.length() ; j++) {
          if (!secondString.contains(firstString.substring(j, j+1))) {
              return false;
          }
      }
      return true;
  }
  
  // 해쉬맵에 괄호 내 계산을 input
  private static String getNewKey (HashMap<String, Object> hashMap) {
  
      String alpha = "abcdefghilmnopqrstuvzyjkx";
      for (int j = 0 ; j < alpha.length() ; j++) {
          String k = alpha.substring(j,j+1);
          if (!hashMap.containsKey(k)) {
              return k;
          }
      }

      // 정 없으면 문자열 두개 조합
      for (int j = 0 ; j < alpha.length() ; j++) {
          for (int i = 0 ; i < alpha.length() ; i++) {
              String k = alpha.substring(j,j+1)+alpha.substring(i,i+1);
              if (!hashMap.containsKey(k)) {
                  return k;
              }
          }
      }
      throw new NullPointerException();
  }

    // 데이터 타입 확인
  private static boolean isBigDecimal (String number) {
    try {
        new BigDecimal(number);
        return true;
    } catch (Exception ex) {
        return false;
    }
}
  
  private static String[] splitByLettersAndNumbers (String val) {
      if (!firstContainsOnlySecond(val, alphanumeric+"+-")) {
          throw new IllegalArgumentException("Wrong passed value: <<"+val+">>");
      }
      ArrayList<String> response = new ArrayList<>();
      String searchingFor;
      int lastIndex = 0;
      if (firstContainsOnlySecond(""+val.charAt(0), numeric+"+-")) {
          searchingFor = alphabetic;
      }else {
          searchingFor = numeric+"+-";
      }
      for (int j = 0 ; j < val.length() ; j++) {
          if (searchingFor.contains(val.charAt(j)+"")) {
              response.add(val.substring(lastIndex, j));
              lastIndex = j;
              if (searchingFor.equals(numeric+"+-")) {
                  searchingFor = alphabetic;
              }else {
                  searchingFor = numeric+"+-";
              }
          }
      }
      response.add(val.substring(lastIndex,val.length()));
      return response.toArray(new String[response.size()]);
  }
  
  private static void deleteValueIfPossible (String val, HashMap<String, Object> values, String function) {
      if (values.get(val) != null & function != null) {
          if (!function.contains(val)) {
              values.remove(val);
          }
      }
  }
  
  // howManyOfThatString에 속한 inThatString 개수 : 괄호 갯수 판별에 사용
  private static int contOccouranceIn (String howManyOfThatString, String inThatString) {
      return inThatString.length() - inThatString.replace(howManyOfThatString, "").length();
  }

}