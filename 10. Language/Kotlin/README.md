# Kotlin

안드로이드 및 웹 개발에서 Java를 대체할 목적으로 JetBrains에서 개발된 언어
최신의 패러다임을 적용하고, Java의 몇 몇 약점을 개선함
기존 Java 머신과 호환되게 만들어짐.

- 웹 컴파일러 사이트 : <https://play.kotlinlang.org>
  
## 변수

var : 일반적인 변수, 읽기 쓰기가 가능
val : 선언시 초기화 하고 변경 불가

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

## 기본 자료형

- 숫자형
  - 정수형 : Byte(8bit), Short(16), Int(32), Long(64, L붙이기)
  - 실수형 : Float(32, f붙이기), Double(64, 기본값)
  - 기타 : 2진수(0b), 16진수(0x)
- 문자형
  - Char : 문자 하나(2 byte), 작은 따옴표로 감싸고, 특수 문자(\t ...) 지원
  - 문자열 : 따옴표로 감싼 범위 전부, 따옴표 세개일 경우 줄 바꿈이나 특수문자까지 문자열로 사용
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
