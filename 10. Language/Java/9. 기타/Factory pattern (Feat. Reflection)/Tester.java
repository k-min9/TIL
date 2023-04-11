import java.util.HashMap;
import java.util.List;

public class Tester {

  public static void main(String[] args) {
    HashMap<String, String> tmpDB = new HashMap<String, String>();
    tmpDB.put("typeA", "InfoKor");
    tmpDB.put("typeB", "InfoEng");
  
    String keyword = "생성된 클래스에 입력할 입력값";
    Class cls = Class.forName("패키지주소."+tmpDB.get("typeA"));
    InfoFactory obj = (InfoFactory)cls.getDeclaredConstructor().newInstance();
    List<String> result = obj.getInfoData(keyword);

    // 키워드만 바꿔줘도 다른 결과가 나오는 것을 확인할 수 있다 >> 차후 로직의 인스턴스화가 가능
    Class cls = Class.forName("패키지주소."+tmpDB.get("typeB"));
    InfoFactory obj = (InfoFactory)cls.getDeclaredConstructor().newInstance();
    List<String> result = obj.getInfoData(keyword);
  }
}
