import java.util.List;

/**
 * InfoFactory
 * 기본이 되는 인터페이스 생성
 */
public interface InfoFactory {

  public List<String> getInfoData(String keyword);
}