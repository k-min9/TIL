import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;

/**
 * BigDecimal : 
 * 실수의 정확한 연산이 필요할 때 사용
 * 부동 소수점에 따른 미묘한 근사치를 용서할 수 없는
 * 
 * 금융업이라던가 숫자가 조금이라도 차이나면 안되는 시점에 사용하자
 * 
 * 원리
 * 내부적으로 배열을 사용하여 데이터를 분리하여 저장
 * 
 * 구성
 * IntValue : BigInteger로 구성되어, 정수부분을 저장
 * scale : 소수점 위치를 저장하는 지수
 * precision : 왼쪽 0 이 아닌곳부터 시작해서 오른쪽 0이 아닌곳까지의 총 자리수
 * 
 */
public class Bigdecimal {

  public static void main(String[] args) {

    BigDecimal n1 = new BigDecimal("27.125");  // decimal의 D는 대문자임
    BigDecimal n2 = new BigDecimal("55.5555");
    BigDecimal n3 = new BigDecimal(10000);

    // 연산 : 모든 연산이 메서드 호출
    n1 = n1.add(n2);
    System.out.println("더하기 : " + n1);
    System.out.println("빼기 : " + n1.subtract(n2));
    System.out.println("곱하기 : " + n1.multiply(n2));
    System.out.println("나누기 : " + n1.divide(n3));
    System.out.println("나누기 소수 네째자리까지 내림 : " + n1.divide(n3, 4, RoundingMode.DOWN));
    System.out.println("나머지 : " + n1.remainder(n2));
    System.out.println("큰값 : " + n1.max(n2));
    System.out.println("작은값 : " + n1.min(n2));

    // 반올림, 내림
    System.out.println("둘째자리 반올림 : " + n1.setScale(2, RoundingMode.HALF_UP));
    System.out.println("둘째자리 올림 : " + n1.setScale(2, RoundingMode.UP));

    // 형변환
    System.out.println("문자열 : " + n1.toString());
    System.out.println("정수 : " + n1.intValue());
    System.out.println("실수 : " + n1.floatValue());
    
    // 연산
    System.out.println("비교 : " + n1.compareTo(n2));
    System.out.println("동일 : " + n1.equals(n2));

    // 다른 선언
    System.out.println("선언 0 : " + BigDecimal.ZERO);
    System.out.println("선언 1 : " + BigDecimal.ONE);


    // 기타
    System.out.println("엄청 긴 정수 : " + new BigInteger("123456789012345678901234567890"));  // 기껏해야 19자리까지나 표현이되는 long보다 많은 표현이 가능



  }
}