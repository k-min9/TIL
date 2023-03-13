import java.util.HashMap;

/**
 * 만들어진 DTO 실험버전
 */
public class Test {
  public static void main(String[] args) {
    HashMap<String, Object> myHashMap = new HashMap<String, Object>();
    myHashMap.put("name", "민구");

    // if (myHashMap instanceof MyDto) {
    //   System.out.println("yes");
    // } else {
    //   System.out.println("no");
    // }
    
    MyDto myDto = (MyDto) myHashMap;
    System.out.println(myDto.getName());

    myDto.put("name", "민구");
    myDto.put("name2", "민구");

  }
}
