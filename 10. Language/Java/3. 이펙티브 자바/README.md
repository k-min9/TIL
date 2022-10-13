# 이펙티브 자바

- 개요 : 모든 자바 개발자의 필독서
- 배경 : 근데 이해하기 어렵다! 하나하나 풀어서 이해해보자
- 방식 : 책 + 인강

## 아이템 1. 생성자 대신에 Static Factory Method(정적 팩토리 메소드)를 고려해보자

- 개요 : Static Factory Method는 객체 생성의 역할을 하는 클래스 메서드
- 장점
  - 이름을 가질 수 있음
    - before : urgent와 prime으로 나누고 싶은데, 같은 인자가 들어와 이름 짓기 애매함.

      ```java
      public class Order {

        private Product product;
        private boolean prime;
        private boolean urgent;

        public Order(Product product, boolean prime) {
            this.product = product;
            this.prime = prime;
        }

        // 물론 작동도 안하지만 이런 느낌으로 꼬인다...
        public Order(Product product, boolean urgent) {
            this.product = product;
            this.urgent = urgent;
        }
      }
      ```

    - after : 이름을 지어 명확히 정의

      ```java
      public class Order {

        private boolean prime;
        private boolean urgent;
        private Product product;

        public static Order primeOrder(Product product) {
            Order order = new Order();
            order.prime = true;
            order.product = product;

            return order;
        }

        public static Order urgentOrder(Product product) {
            Order order = new Order();
            order.urgent = true;
            order.product = product;
            return order;
        }
      }
      ```

  - 호출할 때마다 새로운 객체를 생성할 필요가 없다.
    - 자주 사용하는 객체를 만들어 놓고 get함으로써 최적화를 꾀할 수 있다.
    - ex) Boolean.valueOf
  - 하위 자료형 객체를 반환할 수 있다.
    - 인터페이스 기반 개발 핵심 기술. 굳이 구현 클래스를 찾을 필요도 없고, 해당 클래스에 의존하지 않게 된다.
    - ex) Spring
  - 입력 매개변수에 따라 매번 다른 클래스의 객체를 반환할 수 있다.
    - 생성자와 다르게 하위 객체기만 하면 반환 타입이 그때그때 달라도 오케이
  - 정적 팩토리 메서드를 작성하는 시점에는 반환할 객체의 클래스가 존재하지 않아도 된다.
    - ex) JDBC
- 단점
  - Static Factory에 private를 사용하므로 상속받을 수 없게 된다.
    - 클래스 째 선언하면 되고, 오히려 장점으로 쓸 수 있음.
  - 정적 팩토리 메소드는 javadoc과 어울리지 않아 알아보기 힘들고, 문서 길이가 길어지게 한다.
    - 직접 입력하고 @see 등을 통해 명시해야 한다.
- Extra / 완벽 공략
  - Enum(열거타입) : 상수 목록을 담을 수 있는 데이터 타입. Type-Safety(중요!)를 보장한다.
  - Flyweight(가벼운 체급 패턴) : 객체를 가볍게 만들어 메모리 사용을 줄이는 패턴
    - 잘 변하지 않는 부분을 만들어두거나 cache해두어 최적화를 진행
  - 인터페이스에서도 default를 선언하여 인스턴스 용 메서드를 선언하고 사용할 수 있다.(자바 8 이상)
  - 리플렉션 : ClassLoader을 이용하여 읽어온 정보를 이용하여 값등을 사용할 수 있음
    - 해당 인스턴스를 선언하거나 만들지 않고도 인스턴스 메서드를 사용할 수 있음.

## 아이템 2. 생성자에 매개변수가 많다면 빌더를 고려하라

- 배경 : 입력 매개변수가 많고 이에 따라 생성자에 선택적 매개변수가 많을때
  - 대안 1 : 생성자 체이닝. 적은 변수를 사용한 생성자를 포괄하는 쪽이 this()로 호출한다.
  - 대안 2 : 자바빈즈 : 매개변수가 없는 생성자로 객체를 만든 후, Setter를 이용해 설정
    - Set을 빼먹거나 선언 중간에 사용해버리는 일관성 문제가 발생할 수 있다.
    - Setter를 사용하면 불변 객체로 사용할 수 없다.
- 빌더 : 생성자 체이닝, 자바 빈즈 방식의 장점을 전부 취득할 수 있음
- 구현
  - 선언

    ```java
    // 빌더 패턴을 적용하고 싶은 클래스 내 선언
    public static class Builder {
      // 필수값
      private final int servingSize;  
      private final int servings;

      // 선택 변수
      private int calories = 0;
      private int fat = 0;
      private int sodium = 0;
      private int carbohydrate = 0;

      // 필수 값으로 가져야 함
      public Builder(int servingSize, int servings) {
        this,servingSize = serginsSize;
        this.servings = servings;
      }

      public Builder fat(int val) {
        fat = val;
        return this;
      }

      public Builder sodium(int val) {
        sodium = val;
        return this;
      }

      public Builder carbohydrate(int val) {
        carbohydrate = val;
        return this;
      }

      public NutritionFacts build() {
        return new NutritionFacts(this);
    }
    ```

  - 사용

    ```java
    NutritionFacts cocaCola = new Builder(240, 8)
            .calories(100)
            .sodium(35)
            .carbohydrate(27).build();
    ```

  - 단점
    - 객체 코드가 복잡하고 길어짐
      - Lombok의 @Builder를 쓰면 간결해지지만, 필수값 지정을 할 수 없음
  - 기타
    - @AllArgsConstructor(access == AccessLevel.PRIVATE)를 설정해두면 Builder에 의한 생성만 강제할 수 있음.
    - 계층형 빌더 : Abstact Class에서 Builder를 재귀 하는 Builder를 선언하여 하위 클래스가 구현
      - protected abstract T self();로 하위 메서드를 사용할 수 있게 됨
- Extra / 완벽 공략
  - 자바 빈즈 : Java로 작성된 소프트웨어 컴포넌트. JSP와 연관이 높음
  - illegalException : 잘못된 인수가 들어갈때 발생하는 Exception.
    - 기본 Unchecked(런타임) Exception이지만, Checked(컴파일) Exception처럼 명시적으로 throws 할 수 있음
    - checked Exception은 try ~ catch 해야해서 귀찮지만, 에러가 발생했을때의 대처법을 넣고 싶을때는 중요하다.
