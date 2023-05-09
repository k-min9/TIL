import java.util.Arrays;
import java.util.List;

/**
 * 직접 입력하는 것이 아니라 Enum을 이용해 규격화 하는 것이 가능
 */
public class EnumUtil {

  public enum tartgetInfo {
    Info001("안녕", "hello"),
    Info002("뭐", "What")
    ;

    private String wordKor;
    private String wordEng;

    tartgetInfo(String wordKor, String wordEng) {
      this.wordKor = wordKor;
      this.wordEng = wordEng;
    }

    public String getWordKor() {
      return wordKor;
    }

    public String getWordEng() {
      return wordEng;
    }
  }

  public static tartgetInfo getTargetInfo(String num) {
    tartgetInfo result = null;

    switch (num) {
      case "001": result = tartgetInfo.Info001; break;
      case "002": result = tartgetInfo.Info002; break;
      default: result = tartgetInfo.Info001; break;
    }

    return result;
  }

  /**
   * 실제 사용 예시 : 하드 코딩 없이 출력
   * @param args
   */
  public static void main(String[] args) {
    List<String> messageNums = Arrays.asList("001", "002");

    for (String messageNum : messageNums) {
      System.out.println(EnumUtil.getTargetInfo(messageNum).getWordKor() + " " + EnumUtil.getTargetInfo(messageNum).getWordEng());
    }
  }

}
