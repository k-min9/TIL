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
