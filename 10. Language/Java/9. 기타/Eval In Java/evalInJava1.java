import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

/**
 * java는 eval 함수가 없다.
 * 방법 1 : ScriptManager을 이용하여 js의 eval을 사용하기
 * 문제 : 소스코드 복잡시 성능문제 발생
 */
public class evalInJava1 {

  public static void main(String[] args) {
    
    try {
      ScriptEngineManager sem = new ScriptEngineManager();
      ScriptEngine se = sem.getEngineByName("JavaScript");

      // 문자열 비교
      String exp = "'a' == 'a'";
      System.out.println(se.eval(exp));

      // 불린변수 및 괄호 사용 
      String exp2 = "('a' == 'a') && false";
      System.out.println(se.eval(exp2));

      // 가변 및 변수
      List<String> varsList = new ArrayList<String>();
      varsList.add("b = true");
      varsList.add("c = false");
      varsList.add("d = true");
      for (String var : varsList) {
        se.eval(var);
      } 
      System.out.println(se.eval("b==c"));
      System.out.println(se.eval("b==d"));
      System.out.println(se.eval("b&&(c||d)"));

      // 변수 java틱하게 넣기
      ConcurrentHashMap<String, Object> vars = new ConcurrentHashMap<>();
      vars.put("x", true);
      vars.put("y", returnFalse());
      vars.put("z", returnTrue());
      for (ConcurrentHashMap.Entry<String, Object> var : vars.entrySet()) {
        se.put(var.getKey().toString(), var.getValue());
      }

      String formula = "x&&(y||z)";
      System.out.println(se.eval(formula));

      se.eval("rule1 = " + formula);
      System.out.println(se.get("rule1"));

      String formula2 = "y";
      System.out.println(se.eval(formula + "&&" + formula2));


    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private static boolean returnTrue() {
    return true;
  }

  private static boolean returnFalse() {
    return false;
  }
}