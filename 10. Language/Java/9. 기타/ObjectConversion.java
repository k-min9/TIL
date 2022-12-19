import java.math.BigDecimal;

public class ObjectConversion {
  public static void main(String[] args) {
    Object a = "PD001";
    Object b = "11";
    Object c = true;
    Object d  = 11;
    Object e  = new BigDecimal("11");
    // BigDecimal f = BigDecimal.valueOf(e);  // 요러면 에러남

    System.out.println(a instanceof String);
    System.out.println(b instanceof String);
    System.out.println(c instanceof String);
    System.out.println(d instanceof String);
    System.out.println(e instanceof String);

    System.out.println("Boolean ==========");
    System.out.println(a instanceof Boolean);
    System.out.println(b instanceof Boolean);
    System.out.println(c instanceof Boolean);
    System.out.println(d instanceof Boolean);
    System.out.println(e instanceof Boolean);

    System.out.println("BigDecimal ==========");
    System.out.println(a instanceof BigDecimal);
    System.out.println(b instanceof BigDecimal);
    System.out.println(c instanceof BigDecimal);
    System.out.println(d instanceof BigDecimal);
    System.out.println(e instanceof BigDecimal);
  }
}
