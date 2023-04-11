# Factory Pattern

- 개요 : 간단한 클래스 생성 팩토리를 만들어보자
- 방식
  - 1. Factory가 될 Interface 생성
  - 2. Interface를 상속하여 함수를 정의할 클래스 생성
  - 3. 클래스의 위치를 참조하여 인스턴스를 만들고 해당 함수 작동
- 참조 : Reflection. 구체적인 클래스의 타입을 알지 못해도 클래스의 변수 및 메소드 등에 접근하게 해줌
  - Class.forName()이 클래스 이름만 알면 클래스를 제어할 수 있게 도와주는 Reflection API
