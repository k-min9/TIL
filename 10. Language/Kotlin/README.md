# Kotlin

안드로이드 및 웹 개발에서 Java를 대체할 목적으로 JetBrains에서 개발된 언어
최신의 패러다임을 적용하고, Java의 몇 몇 약점을 개선함
기존 Java 머신과 호환되게 만들어짐.

- 참조 강좌 링크 : [Dimo의 Kotlin 강의](https://www.youtube.com/watch?v=8RIsukgeUVw&list=PLQdnHjXZyYadiw5aV3p6DwUdXV2bZuhlN)
- 웹 컴파일러 사이트 : <https://play.kotlinlang.org>
  
## 변수

var : 일반적인 변수, 읽기 쓰기가 가능  
val : 선언시 초기화 하고 변경 불가  
(할당 변경이 안되는 것이지, 내부 속성은 변경할 수 있음)  
const : 상수, 한 번 선언 후 절대 변경 불가. 기본자료형만 생성 가능  
반드시 companion object 안에 선언되어 객체와 상관없이 클래스 연관 고정값으로 쓰임  
의례적으로 CONST_A 같이 대문자와 언더바만 사용  

property : class 내에 선언  
Local variable : 그 외에 scope 내에 선언  

특징 : 기본 변수로 null을 허용하지 않음 => NPE를 원천적으로 차단  

- 사용하기 전까지만 선언하면 됨
- null을 허용하는 nullable 변수 선언은 자료형 뒤에 ?를 붙여준다.

선언 예시  

``` Kotlin
  var a:Int = 123
  var b:Int? = null 
```

## 변수 제어

Kotlin은 선언 시 값을 할당해 줘야 컴파일이 가능 하지만, 그러지 못하는 경우가 있다.

- 이때 lateinit를 써서 변수만 선언하고, 초기값의 할당을 나중에 할 수 있도록 설정 가능

사용법 : lateinit var a:Int  
제한사항 : 할당전까지 변수 사용 불가(에러 발생), 기본 자료형에는 사용 불가  
초기화 여부 확인 : ::a.isInitialized로 체크 가능  

- 지연대리자속성 : 변수 사용시점까지 초기화를 늦춰줌, 코드 실행 초기화

사용법 : val a: Int by lazy{7}  // 7 부분은 람다함수로 여러 문장 가능

## 기본 자료형

- 숫자형
  - 정수형 : Byte(8bit), Short(16), Int(32), Long(64, L붙이기)
  - 실수형 : Float(32, f붙이기), Double(64, 기본값)
  - 기타 : 2진수(0b), 16진수(0x)
- 문자형
  - Char : 문자 하나(2 byte), 작은 따옴표로 감싸고, 특수 문자(\t ...) 지원
  - 문자열 : 따옴표로 감싼 범위 전부, 따옴표 세개일 경우 줄 바꿈이나 특수문자까지 문자열로 사용
    - 자주 쓰는 함수 : .length, .toLowerCase(), .split, .joinToString(""), .substring
    - 빈 문자열 체크 : .isNullOrEmpty(), isNullOrBlank() // 공백문자(" ")까지 체크
    - 포함 여부 : startsWith("java"), endsWith(".kt"), contains("line")
- 논리형
  - Boolean : true, false
- Any : 어떠한 자료형과 호환되는 최상위 자료형

## 형변환과 배열

- 형변환 : to + 변환될 자료형()
  - Kotlin은 명시적 형변환만을 지원한다. (암시적 형변환은 지원하지 않음)

``` Kotlin
  var a:Int = 54321
  var b:Long = a.toLong()
```

- 배열 : 한 번 선언되면 크기 변경이 되지 않지만, 빠른 입출력이 가능

``` Kotlin
  var intArr = arrayOf(1, 2, 3, 4, 5)
  var nullArr = arrayOfNulls<Int>(5)  // null로 채워진 특정한 크기의 배열

  intArr[2] = 8  // 3이 8로 바뀜
  println(intArr[4])  // 5가 출력됨
```

## 함수, 타입 추론

fun 으로 시작

- 형태 : fun 이름(parameter):자료형 {}

``` Kotlin
fun main() {
  println(add(5,6,7))
}

fun add(a:Int, b:Int, c:Int):Int {  // 반환형이 Int라는 선언
  return a + b + c
}

// 단일 표현식 함수형
fun add(a:Int, b:Int, c:Int) = a + b + c
```

타입추론 : ':자료형' 처럼 명시해주지 않고 알아서 추론해준다.

## 조건문

- if ~ else ~
- When : 다른 문의 Switch와 유사 (부등호 사용은 불가, 여러 조건 만족시 가장 먼저 부합되는 것 실행)

``` Kotlin
when(a) {
  1 -> println("정수 1입니다")
  2 -> "정수 2입니다"  // 이렇게 적을 경우 값을 반환. var result = when... 으로 할당 가능
  is Long -> println("Long 타입입니다")
  else -> println("어떠한 조건도 만족하지 않습니다")
}

```

- 비교 연산:
  - 부등호, ==, ! 는 동일
  - is 연산자 : 좌측 변수가 우측 자료형에 호환되는지 bool값 리턴 (a is Int)

## 반복문

- 조건형 반복문 : while, do ... while
- 범위형 반복문 : for

  ``` Kotlin
    for(i in 0..9)  // 0에서 9까지 반복
    for(i in 0..9 step 3)  // 0, 3, 6. 9로 반복
    for(i in 9 downTo 0)  // 9에서 0까지 1씩 감소하며 반복
    for(i in 'a'..'e') // a부터 e까지 반복하며 증가
  ```

## 흐름제어

- return, break는 동일
- 이중 반복문 등에서

  ``` Kotlin
  loop@for(i in 1..10) {
    for (j in 1..10) {
      if (i == 1 && j == 2) break@loop
    }
  }
  ```

  레이블+@ 기호를 앞에 달고 break에 @+레이블 이름을 달면 한 번 에 빠져나올 수 있다.

## 클래스

- 선언 : class [클래스명] (파라미터)
- 인스턴스 내용 : ${인스턴스명.파라미터명}
- 클래스 내 함수 사용 : 인스턴스명.함수()
- 생성자 : init
  - 기본 생성자 : 클래스를 만들때 기본으로 선언 - init
  - 보조 생성자 : 기본값 부여 등 필요에 따라 추가적으로 선언 - constructor

  ``` Kotlin
  fun main() {
    var a = Person("강민구", 1990)  // init 사용

    var b = Person("강민구")  // constructor 사용
  }

  class Person (var name:String, val birthYear:Int) {
    init {
      println("${this.birthYear}년생 {$this.name}님이 생성되었습니다.")
    }

    // this 잊지말고 쓰고 그 이후에 parameter 집어 넣기
    constructor (name:String) : this(name, 1997) {  
      println("init의 birthyear에 1997이 input 되었습니다!")
    }
  }
  ```

- 상속 : Kotlin은 기본 상속 금지
  - 상속 하는 쪽 : open class로 열어둘 수 있음 ; open class Animal(name:String, age:Int, type:String)
  - 상속 받는 쪽 : :상속받을 클래스 명 ; ~~:Animal(name, age, "개")
    - 내부 함수 선언하여 전용 함수 만들기 가능
    - override로 함수를 재선언하여 재구현할 수 있음

- 추상화 : abstract를 붙은 class. override로 구현부를 만들어 구현해야 함
  - kotlin의 인터페이스는 추상함수와 일반함수를 다 가질 수 있음.
    - open, abstract 선언 생략 가능
    - 여러 개의 인터페이스 상속 가능

- data class : 데이터를 다루는데 최적화된 클래스
  - equals, hashcode, toString, copy, component1,2.... 같은 5가지 기능을 기본 제공

- Enum class : 열거형, 상수를 나타내는데 최적화 된 클래스

## 프로젝트 구조

- 프로젝트 : 여러 파일로 구성하여 작업할 수 있게하는 틀
- 모듈 : 하나의 프로젝트는 여러개의 모듈
- 패키지 : 파일과 폴더의 소속. 자바와 달리 폴더구조와 패키지 명을 일치시키지 않아도 됨
- 접근 제한자
  - 패키지 스코프 : public, internal(같은 모듈), private(같은 파일)
  - 클래스 스코프 : public, private(같은 모듈), protected(자신과 상속받은 범위)

## 고차함수 (high-order function)

함수를 마치 클래스에서 만들어 낸 인스턴스처럼 취급  
패러미터 처럼 취급하거나 결과값을 받아올 수 있음  

- 함수의 형식 : (패러미터 자료형, ...) -> 반환형 자료형
- 람다함수 : 그 자체가 고차함수, 별도의 연산자 없이 변수에 담을 수 있음
  - 여러 구문 수행 가능, 마지막 구문이 반환됨
  - 패러미터 없으면 () ->, 패러미터 하나면 생략 가능하고 it로 호출 가능
- 스코프 함수 : 함수형 언어의 특징을 좀 더 편리하게 사용할 수 있도록 기본 제공
  - apply, run, with, also, let

``` Kotilin

fun main() {

  넘겨받을함수(::부를함수)

  // 람다함수
  val c = {str:String -> print("$str")}

}


fun 넘겨받을함수 (function: (String) -> Unit) {
  ...내용
}
```

## 오브젝트

싱글톤 패턴, 최초 사용시 자동 생성 후 공용 사용  
companion object : 인스턴스 내에 공용하는 static 같은 object  

## 이벤트

옵저버 : 이벤트의 발생을 감시하는 감시자, listner  
이벤트 : 시스템 또는 루틴에 의해 발생하는 동작  

구조 예시 : class EventPrinter > Interface EventListener < class Counter

``` Kotlin
fun main() {
    EventPrinter().start()
}

interface EventListener {
    fun onEvent(count: Int)
}

class Counter(var listener: EventListener) {
    fun count() {
        for (i in 1..100) {
            if (i % 5 == 0) listener.onEvent(i)
        }
    }
}

class EventPrinter: EventListener {
    override fun onEvent(count: Int) {
        print("${count}-")
    }
    
    fun start() {
        val counter = Counter(this)
        counter.count()
    }
}

```

익명 객체 : EventPrinter가 EventListner를 상속받아 구현하지 않고,  
임시로 만든 별도의 EventListner 객체를 '즉시 생성'하어 넘겨 주게 구현  

## Collection

데이터를 모아 관리하자

- List : 여러개의 데이터를 원하는 순서로 넣어서 관리
  - 종류
    - List : 생성시 넣은 객체를 대체, 추가, 삭제할 수 없음
    - MutableList : 가능함
      - 추가(add), 삭제(remove, removeAt), 정렬(sort), 섞기(shuffle)
  - for (num in nums) 등으로 사용 가능
  - 선언 : var a = listOf("사과", "배", "딸기"), var b = mutableListOf(6,3,1)

- Set : 중복이 허용되지 않는 Collection
  - 종류 : 마찬가지로 Mutable로 구분

- Map : key-value 형태의 Collection
  - 종류 : 마찬가지로 Mutable로 구분
  (mutableMapOf("key" to "value", "key2" to "value2", ...))
    - 추가(put), 삭제(remove)
  - for (entry in nums) 로 사용 가능. 해당 값은 &#36;{entry.key}, &#36;{entry.value}로 참조

## Collection 함수

수월한 collection 조작을 위한 함수  
collection에 일반 함수나 람다 함수를 사용하여 for 문 없이도 순회하며 참조하거나 변경  
함수 뒤에 {}의 내용물을 실행하고, it는 반복되고 있는 현재 내용물을 가리킴  

- .forEach : collection 내용물을 하나하나 반복
- .filter : collection 내용물을 필터링해서 반환
- .map : collection 내용물 일괄적으로 변경함
- .any, .all, .none, .count
- .firstOrNull, .lastOrNull : 첫번째, 마지막 객체를 반환하거나 없으면 null을 반환
- associateBy : 아이템에서 key를 추출하여 map으로 변환
- groupBy : key가 같은 아이템끼리 배열로 묶어 map으로 변환
- partition : 아이템에 조건을 걸어 true, false 값을 가지는 두 개의 collection으로 나눔
- flatMap : 아이템마다 만들어진 collection을 합쳐서 반환
- getOrElse : 해당 위치에 아이템이 있으면 반환하고 없으면 지정 기본값 반환
- zip : 두 collection을 1:1 대응 pair로 만들어 반환 (수가 다를 경우, 작은 쪽을 따라감)

## 코루틴

비동기로 여러개의 루틴을 동시에 처리, 메인 루틴가 실행/종료를 제어하고 별개로 진행

- 지원범위
  - GlobalScope: 프로그램 어디서나 제어, 동작이 가능한 기본 범위
  - CoroutineScope : 특정한 목적의 Dispatcher를 지정하여 제어 및 동작이 가능한 범위
    - Dispatcher : 코루틴스코프 제작시 적용가능
      - Default : 기본적인 백그라운드
      - IO : I/O 최적화 동작
      - Main : 메인(UI) 스레드에서 동작
- 반환값 여부
  - launch : 없음. job 객체
  - async : 있음. Deffered 객체
- 코루틴은 프로그램 종료시 함께 종료되기 때문에 코로틴 종료를 기다려야 한다.
  - runBlocking {} 블럭을 사용  // 안드로이드는 이 대기 시간이 길어지면 앱 강제 종료
  - 대기
    - delay(milisecond: Long) : 밀리세컨드 단위로 루틴을 잠시 대기
    - Job.join() : Job의 실행이 끝날때까지 대기
    - Deferred.await() : Deferred의 실행이 끝날때까지 대기하고 값을 반환
  - 취소 : cancel()
  - 기타 : TimeoutOrNull(밀리세컨드), 시간내 실행 못할 경우 null 반환

``` Kotlin
import kotlinx.corotines.*  // 임포트 필요

val scope = CoroutineScope(Dispathcer.Default)
val coroutineA = scope.launch {}
val coroutineB = scope.async {}
```

## 리스트 뷰

어댑터(Adapter) : 데이터를 받아 해당 내용을 뷰(ex. list_item.xml)로 생성해주는 객체

- 순서
  - 기본 BaseAdapter를 상속 받은 후 override (implements members)
  - adapter에 해당 item을 getView로 등록

  ``` Kotlin
  override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
    var converView = convertView

    if (converView == null) {
        converView = LayoutInflater.from(parent?.context).inflate(R.layout.listview_item, parent, false)
    }

    val title = converView!!.findViewById<TextView>(R.id.listviewItem)
    val content = converView!!.findViewById<TextView>(R.id.listviewItem2)
    title.text = List[position].title
    content.text = List[position].content
    // List[0] - > ListViewModel("a","b") 이런 느낌으로 업그레이드 해둘 수 있다. (액티비티쪽 조정도 필요)

    return converView!!
  }
  ```

  - 액티비티와 리스트뷰를 연결

  ``` Kotlin
  val list_item = mutableListOf<ListViewModel>()

  list_item.add(ListViewModel("a" , "b"))
  list_item.add(ListViewModel("c" , "d"))
  list_item.add(ListViewModel("e" , "f"))

  val listview = findViewById<ListView>(R.id.mainListview)

  val listAdapter = ListViewAdapter(list_item)
  listview.adapter = listAdapter
  ```

## 기타

- as : 변수를 호환되는 자료형으로 변환 (b as Cola)
- is : 변수가 호환되는지 체크 후 조건문 내부에서만 변환. if 조건문 내부에서만 사용 가능
- 제너릭 : 캐스팅 연산은 프로그램 속도의 저하로 이어짐, 컴파일 시점에 타입을 설정해둠
- null safe operator(?.) : NPE 발생시 그 이후 문장이 실행되지 않음
- elvis operator(?:"대체객체") : NPE 발생시 대체객체 값을 넣어줌
- 동일성 : 내용 동일성(&#61;&#61;), 객체 동일성(&#61;&#61;&#61;)
- default argument : argument에 기본값을 넣어 줌
- named parameter : 패러미터이름을 넣으면 해당 위치에 그 내용을 넣을 수 있음
- vararg : 갯수가 지정되지 않은 패러미터
- Infix : 연산자처럼 쓸 수 있는 함수
- FontFamily : res>font 등의 폴더를 만들고 집어넣은 후, "@font/폰트이름.ttf" (폰트 이름 소문자추천)
- ? : null 가능, !! : null 절대 불가
- onBackPressed : 뒤로가기 버튼 이벤트 (액티비티)
- Handler().postDelayed({isDoube=false}, 2000) : 2초 지나면 false로 바꿔라
- 랜덤한 값 뽑기 : sentenceList.random() (해당 리스트는 mutableListOf<>() 으로 선언)
- LayoutInflater는 XML에 정의된 Resource를 View 객체로 반환 출처
