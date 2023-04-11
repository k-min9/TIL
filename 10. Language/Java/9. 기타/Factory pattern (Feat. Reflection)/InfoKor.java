import java.util.Arrays;
import java.util.List;

public class InfoKor implements InfoFactory{

  @Override
  public List<String> getInfoData(String keyword) {
    return Arrays.asList("사과", "바나나", "멜론");
  }
}
