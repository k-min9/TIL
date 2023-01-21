# Flutter

## 초급편

### 01. Hello, World

- 개요 : 첫 프로젝트를 만들어보자.
- Widget Tree : Widget들의 부모, 자식관계를 나타내는 Tree
  - Widget : 클래스의 일종

### 02. Splash Screen

- 개요 : 처음 앱을 시작하면 켜지는 로딩화면
- 체크사항
  - Asset 추가하기 : 이미지 추가하기
  - StatelessWidget 생성하기
    - 사용자 정의 Widget
  - Column 위젯
  - CircularProgressIndicator 위젯
  - Image 위젯

1. Asset 추가하기
   1. pubspec.yaml 열기
   2. flutter:에  'assets: - asset/img/' 추가
   3. 우측상단 Pub get 눌러 변경사항 적용
2. StatelessWidget 생성
   1. class 클래스이름 extends StatelessWidget 로 상속
   2. Widget build(BuildContext context)를 무조건 override해야 됨
      - Material에 직접 적은 코드와는 다르게, build 내부의 변경값은 Hotreload 됨
   3. 클래스화 하고 싶은 소스를 복사 붙여넣고 기존 값에서 불러오게 함
3. Column 위젯 사용하기 : 새로로 정렬하는 위젯
   1. Column안에 넣는 것은 child가 아닌 children(배열)
   2. 정렬(Alignment)
      - mainAxisAlignment  : 주축
        - MainAxisAlignment.center등의 Enum으로 설정 : start, end, spaceBetween...
      - CrossAxisAlignment : 크로스 축
        - 주축과는 다르게 구성 children이 차지하는 사이즈만 차지함
          - width : MediaQuery.of(context).size.width(기기 가로 길이)로 늘릴 수 있음
          - start, end 등의 Align도 있고, stretch로 늘린 width에 맞게 늘릴 수도 있음
      - MainAxisSize : 주축이 최대 size를 차지하는 default 크기를 조절할 수 있음
   3. 로딩바 넣기 : 원형 로딩바 예시

      ```Dart
      CircularProgressIndicator(
              color: Colors.white,
            ),
      ```

   4. 배경색에 hex 코드 적용해보기 : [backgroundColor: Color(0xFF84C2EA)]
4. 폴더 나누기
   1. lib에 새로운 폴더 만들기
   2. dart 파일 만들고 옮길 클래스 내용 옮기기
   3. 기존 파일에서 'import:[프로젝트name]/[새로운폴더]/[만든dart파일이름]'
      - 프로젝트name은 pubspec.yaml에서도 확인 가능
      - 사용 위젯에 Alt+Enter로 자동 import도 가능
5. SafeArea와 Container
     - Container : 위젯을 담는 틀
     - SafeArea : 범위 밖으로 삐져나가는 것을 막음.
       - bottom : false 등 여러 parameter 있음
6. Expanded와 Flexible
     - 주의 : Row와 Column 내에서만 사용할 수 있음
     - Expanded : 남아있는 공간을 최대한 채워라
       - Flex : 숫자를 입력(기본값1). Expanded간 비율을 조절할 수 있음
     - Flexible : 지정된 공간을 차지하고 남는 공간을 버림
       - Flex : 숫자를 입력(기본값1). 버리는 공간의 비율을 조절할 수 있음

### 기타 Tip

- Alt+Enter 애용하자.
- Reformat Code with 'dart format' : 코드 자동 정리
- Setting > Keymap에서 원하는 동작에 단축키를 등록할 수 있음
- MaterialApp에 debugShowCheckedModeBanner: false 입력시 디버그 모드 표시 사라짐
