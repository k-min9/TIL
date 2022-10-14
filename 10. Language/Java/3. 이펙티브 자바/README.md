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

## 아이템 3. 생성자나 열거 타입으로 싱글턴임을 보증하라

- 배경 : 여러 인스턴스가 필요하지 않은 경우. 헷갈리지 않고 리소스도 줄이게 싱글턴을 사용.
- 방법 1. private 생성자(외부 생성 불가) + public static field(인스턴스를 여기서 생성)

  ```java
  public class A {
    public static final A INSTANCE = new A();

    private A() {}
  }
  ```

  - 문제점 1 : 인터페이스나 프록시를 쓸 수 없어서, 테스트시 full로 돌려야하는 불편함 발생
  - 문제점 2 : 리플렉션 사용시 싱글턴을 깰 수 있음
    - 대처 - static 변수로 flag를 만들어서 두번째 생성을 막을 수 있음
  - 문제점 3 : 역직렬화에도 취약함.
    - 대처 - readResolve시 INSTANCE를 반환하게 해서 역직렬화를 막아야 함
  - 문제점 4 : 문제점 2~3 때문에 코드가 점점 더러워짐
- 방법 2. private 생성자(외부 생성 불가) + 정적 팩토리 메서드

  ```java
  public class A {
    public static final A INSTANCE = new A();
    private A() {}

    public static A getInstance() {return INSTANCE;}
  }
  ```

  - 방법 1과 단점은 동일하지만 장점이 셋 있음
    - API등의 변경 없이 static factory의 변경 많으로 쉽게 싱글턴을 해제할 수 있음
    - 정적 팩토리 메서드를 제네릭으로 선언하면 각자 다른 타입으로 사용할 수 있음
    - A::getInstance를 supplier의 매개변수처럼 사용할 수 있다.
- 방법 3. 열거 타입을 사용

  ```java
  public enum A {
    INSTANCE;

    // 이하 로직
  }
  ```

- Extra / 완벽 공략
  - 메소드 참조 : 메소드 하나만 호출하는 람다 표현식을 쓰는 방법
  - 함수형 인터페이스 : @FunctionInterface. 1개의 추상 메소드를 갖는 인터페이스.
    - 람다식은 함수형 인터페이스로만 접근 됨
    - 종류가 많지만, Function, Supplier, Consumer, Predicate 네 개를 우선적으로 체크
  - 객체 직렬화 : 객체를 바이트스트림으로 상호변환하는 기술
    - 객체를 파일로 저장하거나 네트워크를 통해 다른 시스템에 전송
    - Serializable 인터페이스 구현
    - transient : 직렬화 하지 않을 필드 지정
    - serialVisionUID : Serializable시 자동 생성, Class의 필드 명 등이 바뀌면 숫자가 바뀌고, 역직렬화 되지 않는다.
      - 선언(private static final long serialVisionUID = 1L;)하여 기존 UID를 유지하면,
      바뀌기 전 직렬화 바이트 스트림으로도 역직렬화할 수 있음

## 아이템 4. 인스턴스화를 막으려면 private 생성자를 사용하라

- 배경 : 인스턴스화 / 살속등이 필요하지 않는 클래스도 있다.
  - 정적 메서드로만 이루어져 있다던가...
    - 우리는 이것을 유틸리티라고 부르기로 했어요
    예시) StringUtils

## 아이템 5. 자원을 직접 명시하지 말고 의존객체 주입을 사용하라

- 배경 : 인스턴스를 생성할 때 필요한 자원을 넘기는 방식
- 장점 : 클래스 유연성, 재사용성, 테스트 용이성
- 스프링 : Inversion of Control, Dependency Injection
  - 제어권 : 인스턴스를 만든다던가, 메서드를 호출한다던가, 의존성을 만든다던가 하는 일련의 활동들
  - IoC : 자기 코드에 대한 제어권을 외부가 쥐고 있음
    - ex) doGet doPost 같은 행위를 서블릿 컨테이너가 쥐고 있음
    - ex) 스프링 Bean을 스프링이 직접 만들고 의존성을 컨테이너에서 알아서 의존성을 주입함
    - 스프링 IoC 장점
      - 좋은 객체지향 프로그래밍, 응집도를 높히고 결합도를 낮춰 유연한 코드 작성을 할 수 있게 됨
      - 이미 오랜 기간 검증 됨
      - 스프링 컨테이너를 통해 인스턴스를 싱글톤 Scope로 사용하기 매우 편해짐
      - 객체(Bean) 라이프 사이클 관련 인터페이스를 제공한다.
        - ex) 스프링 AOP
  - DI 주입 세가지 방법
    - 생성자 주입 : [private final MyService myService;] + @RequiredArgsConstructor
      - 장점
        - 관계가 거의 변할일이 없는 상황에서 불변성 보장
        - 순수 자바 코드로 테스트가 가능함
        - final 키워드 덕에 의존성이 주입 되었는지 컴파일 단계에서 확인할 수 있다.
    - 필드 주입 : @Autowired [private Myservice myService;]
      - 문제점 : 외부 변경이 힘들어 테스트가 힘들고, DI 프레임워크 의존적
    - 수정자 주입 : [private Myservice myService;] 선언 후 Setter 메서드에 @Autowired
      - 문제점 : setter를 Public으로 열어둬야해서 멋대로 수정당할 수 있음

## 아이템 6. 불필요한 객체 생성을 피해라

- 대표 예시
  - 문자열 : 동일한 객체라서 매번 새로 만들 필요가 없다.
    - new String("자바") 쓰지 말고 "자바" 쓰자
  - 정규식, Pattern : 생성비용이 비싸므로, 반복 생성보다는 캐싱하여 재사용하는 것이 좋음
  - 오토박싱/언박싱 : int -> Integer, long -> Long 으로 상호 변환 해주는 기술
    - 자동 변환을 해주는데 쓸데없이 premitive 타입과 Wrapper 타입을 왔다갔다하면 낭비
- 주의 : 불필요하게 낭비되고 생성되는 객체 생성을 피하라는거지 일반적인 객체 생성은 많이많이 해도 된다.
오히려 Static 넣고 코드 꼬이고 그런것보다 낫다.
- Extra / 완벽 공략
  - Deprecation : 사용 자제 권장 API, 전환 시간을 주고 언젠가는 사라질 기능
  - 정규 표현식 쓰이는 곳
    - String.Matches(regex)
    - String.split(regex)
      - 대안) Pattern.compile(regex).split(str)로 패턴 재활용 + 빠름
      - 참고로 regex가 한글자면 split이 더 빠름
    - String.replace(String regex, String replacement)
      - 대안) Pattern.compile(regex).matcher(str).replaceAll(repl)
  - 초기화 지연 기법 : Instance를 생성하는 시점을 그 Instance가 필요한 시점까지 최대한 늦춤 (아이템 83)
  - 방어적 복사 : 새로운 객체를 만들때는 기존의 복사로 만들지 말고 완전히 새로 만들어라 (아이템 50)

## 아이템 7. 다 쓴 객체 참조를 해제하라

- 배경 : 객체에 대한 레퍼런스가 남아있다면 해당 객체는 가비지 컬렉션의 대상이 되지 않는다.
- 개요 : 자기 메모리를 직접 관리하는 클래스라면 메모리 누수에 주의해야 한다.
  - ex) 스택, 캐시(해쉬 맵으로 구현), 리스너 또는 콜백
- 대안
  - 직접 참조 객체를 null 처리하기
  - 적절한 자료구조 사용하기 ex) WeakHashMap
  - 직접 LRU 캐시 등을 사용하여 넣고 빼주기
  - 주기적 클린업 작업
    - ex) ScheduledThreadPoolExecutor 활용, 백그라운드 스레드를 이용하여 가장 오래된것을 삭제하기
- Extra / 완벽 공략
  - NPE 발생 사유 : 메소드에서 null을 리턴하기 때문에 && null 체크를 하지 않았기 때문에
    - 메소드에서 적절한 값을 리턴할 수 없는 경우에 선택할 수 있는 대안 : Optional을 리턴하자
    - Optional은 리턴 값으로만 쓰자, 매개변수로 써도 의미 없고, Collection 감싸도 애초에 Collection에서 empty 체크 되고 의미가 없다.
    - Optional 쓸 경우 return null;이 아니라 return Optional.empty();
  - WeakHashMap : GC시 강하게 레퍼런스되는 곳이 없다면 해당 엔트리를 제거

## 아이템 8. finalizer, cleaner 사용하지 마라

- 개요 : 둘 다 객체 소멸 시 리소스 반환용 핸들러지만 쓰지 마라
- 이유
  - 즉시 수행이 보장되지 않음
  - 실행자체가 안 될 수 있음
  - 동작 중 예외 발생시 정리 작업이 처리되지 않을 수 있음
  - 심각한 성능 문제가 있음
  - finalizer는 보안 문제도 있음
- 예시
  - AutoCloseable 인터페이스

    ```java
    // Closeable 상속!
    public class AutoClosableIsGood implements Closeable {

        private BufferedReader reader;

        public AutoClosableIsGood(String path) {
            try {
                this.reader = new BufferedReader(new FileReader(path));
            } catch (FileNotFoundException e) {
                throw new IllegalArgumentException(path);
            }
        }

        @Override
        public void close() {
            try {
                reader.close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }
    ```

  - try-with-resource

    ```java
    public class App {

        public static void main(String[] args) {
            try(AutoClosableIsGood good = new AutoClosableIsGood("")) {
                // 블록 처리 후 알아서 반납이 됨
            }
        }
    }
    ```

- 결론
  - 반납할 자원이 있는 Class는 AutoCloseable을 구현하고 클라이언트에서 close하거나 try-with-resource를 사용하자.
  - cleaner은 등록한 AutoCloseable을 사용하지 않을때의 안전망 정도로만 쓰자.

## 아이템 9. try-finally보다 try-with-resource를 써라

- 배경 : try-finally는 더 이상 최선의 방법이 아니게 됨
- 개요 : try-with-resource가 더 효율적이고 짧고 분명하며 예외도 뚜렷. 장점밖에 없음. 이거 써라.
- 장점(추가) : 에러가 발생할때 try-finally는 최종 발생한 에러만 보여주지만, try-with-resource는 try 내부 에러도 볼 수 있음
- Extra / 완벽 공략
  - finally 사용시, finally문 마다 close를 하나 만 넣어줘야 close하다가 문제가 발생해도 다른 close를 시도해줄 수 있다.

## 아이템 10 ~ 14

- 개요 : Object 객체의 대표적인 Overrinding 요소인 equals, hashCode, toString, clone, Comparable에 대해 알아보자

## 아이템 10. equals는 일반 규약을 지켜 재정의하라

- 전제 : 필요 없을때는 재정의 안하는게 최선이다
  - 인스턴스가 본질적으로 고유할때 (싱글턴, Enum)
  - 논리적 동치성을 검사할 필요가 없을 때
    - (=이 50 달러와 저 50달러는 같다 수준이면 필요 없음)
  - 상위 클래스에서 재정의한 equals가 하위 클래스에 충분히 적용 가능할 때
  - 클래스가 private라 애초에 equals 부를일이 없을 때
- 규약 : 어떻게 정의해야 하는가?
  - 반사성 : A.equals(A) == true
  - 대칭성 : A.equals(B) == B.equals(A)
  - 추이성 : A와 B가 같고, B와 C가 같으면 A와 C가 같다.
  - 일관성 : A가 불변객체면 A.equals(B)의 값은 항상 같아야 한다.
  - null 아님 : A.equals(null) == false
- 구현
  - 직접
    - == 연산자를 사용해 자기 자신의 참조인지 확인한다.
    - instanceof 연산자로 올바른 타입인지 확인한다.
    - 입력된 값을 올바른 타입으로 형변환 한다.
    - 입력 객체와 자기 자신의 대응되는 핵심 필드가 일치하는지 확인한다.
  - 주어진 방식
    - AutoValue
    - Lombok
    - 인텔리제이등 IDE가 직접 생성해줌
- 주의
  - equals를 재정의 할 때 hashCode도 반드시 재정의
- Extra / 완벽 공략
  - StackOverflowError : 더 이상 스택 프레임을 쌓을 수 없는 상태
    - 스택 : Thread마다 쓸 수 있는 공간. 메소드 호출시, 스택에 스택 프레임이 쌓임
      - 스택 프레임 : 메소드 매개변수, 실행 후 돌아갈 곳, 힙 관련 레퍼런스 등의 정보가 담김
    - 무한 루프 등이나 재귀 함수면 잘 쌓임
      - equals간의 호출 호출 호출로 무한 루프 조심!
  - 리스코프 치환 원칙 : 하위 클래스가 상위 클래스를 대체해도 소프트웨어의 기능을 깨뜨리지 말아야한다.

## 아이템 11. equals를 재정의 하려면 hashCode도 같이 구현하라

- hashCode : 해시 알고리즘에 의하여 객체에 대한 고유의 정수값을 반환하는 함수
  - 객체를 식별할 수 있고, equals 등 객체등을 비교하는 비용을 낮출 수 있음.
  - 두 객체에 대한 equals가 같다면, hashCode의 값도 같아야 한다
  - 캐싱을 사용해 불변 클래스의 해시 코드 계산 비용을 줄일 수 있다. (아예 변수 하나를 지정해버림)
- 주의
  - 지연 초기화 기법(위에서 말한 캐싱 기법)을 사용할 때 스레드 안전성을 신경써야 한다.
  - 성능 때문에 핵심 필드를 해시코드 계산할 때 빼면 안 된다.
  - 해시코드 계산 규칙을 API에 노출하지 않는 것이 좋다.
- 권장
  - 성능 편의상 Lombok의 @EqualsAndHashCode를 추천
