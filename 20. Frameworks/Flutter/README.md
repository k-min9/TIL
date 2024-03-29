# Flutter

## 초급편

### 01. Hello, World

- 개요 : 첫 프로젝트를 만들어보자.

<details>
<summary>상세</summary>

- Widget Tree : Widget들의 부모, 자식관계를 나타내는 Tree
  - Widget : 클래스의 일종. 불변객체
- 작업공간
  - lib > main.dart
  - MaterialApp > home:Scaffold 의 간단한 구조 만들어보기

</details>

### 02. Splash Screen

- 개요 : 처음 앱을 시작하면 켜지는 로딩화면
- 체크사항
  - Asset 추가하기 : 이미지 추가하기
  - StatelessWidget 생성하기 : 상태를 관리할 수 없는 Widget
    - 사용자 정의 Widget
    - Build가 작동
    - StatefulWidget : 상태(State)를 관리할 수 있음
      - CreateState/setState가 작동
  - Column 위젯
  - CircularProgressIndicator 위젯
  - Image 위젯

<details>
<summary>상세</summary>

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

</details>

### 03. Web View

- 개요 : Web 사이트를 앱에다가 패키징
- 체크사항
  - WebView
  - AppBar : App의 상단 디자인
  - pub.dev : 외부 패키지 활용

<details>
<summary>상세</summary>

1. 프로젝트에 Webview 패키지 추가하기
   1. <https://pub.dev/> 사이트 접속
   2. Webview 검색후 Likes, Pub, Popularity를 참고해서 선택
      - 업로더가 flutter.dev이면 Flutter 제작팀이 올린 공식 오픈소스
   3. 들어간 후 이름을 copy 하고, 프로젝트의 pubspec.yaml의 dependencies에 입력
   4. 사이트로 돌아가 README의 사용법 외에도 필요한 설정 등 확인하여 적용
2. WebView 써보기
   - 사용 속성
     - 주소입력 : initialUrl: 'https://github.com/k-min9/TIL'
     - js활성화 : javascriptMode: JavascriptMode.unrestricted
3. Appbar 추가
   1. Appbar에 backgroundColor, title 등 속성 넣기
   2. actions에 IconButton으로 누르면 home으로 돌아가는 버튼을 만들어보자
4. Controller : WebView를 프로그램적으로 조종해보자
   1. onWebViewCreated event 생성시 controller 설정
   (WebViewController controller) {this.controller = controller;}
   2. 3.2.에서 미리 만든 IconButton 누를때 이 controller을 이용하여 Webview를 제어할 수 있음  
   (controller!.loadUrl(homeUrl);)  

</details>

### 04. Image Carousel

<프로젝트 생략>

- 개요 : 스와이프로 이미지 전환이 되고, 4초마다 다음 이미지를 보여주는 전자액자
- 체크사항
  - PageView : 스와이프 기능, 좌,우 스크롤
  - Timer : 시간마다 지정 함수 실행
  - StatefulWidget, LifeCycle

<details>
<summary>상세</summary>

1. PageView 위젯 사용
   1. asset에 이미지 넣고 pubspec.yaml 등록
   2. Pageview 사용하여 이미지 등록 + BoxFit.cover로 규격 맞추기

      ```Dart
         body: PageView(
         controller: controller,  // PageController 생성시 여기 붙음
         children: [1, 2, 3, 4, 5]
               .map(
               (e) => Image.asset(
                  'asset/img/image_$e.jpeg',
                  fit: BoxFit.cover,
               ),
               )
               .toList(),
            )
      ```

2. Timer 사용하기
   1. dart:async패키지를 불러오고 타이머 선언 : Timer? timer;
   2. timer = Timer.periodic(Duration(seconds: 4), (timer) {원하는 동작}
   3. memoryleak을 막기 위해 dispose 구현

      ```Dart
         @override
         void dispose() {
            if (timer != null) {
               timer!.cancel();  // 타이머 취소로 메모리 확보
            }
            super.dispose();
         }
      ```

3. PageController : Pageview를 위한 전용 Controller를 만들어야 함
   1. Build쪽 Pageview controller에 알아서 붙음

      ```Dart
         @override
         void dispose() {
            controller.dispose();
            if (timer != null) {
               timer!.cancel();  // 타이머 취소로 메모리 확보
            }
            super.dispose();
         }
      ```

   2. 이후 알아서 controller 제어

      ```Dart
         controller.animateToPage(
         nextPage,
         duration: Duration(milliseconds: 400),
         curve: Curves.linear,
         );
      ```

   3. controller도 잊지 않고 dispose에 설정 : controller.dispose();
4. DateTime 및 Duration
   - DateTime : 날짜
   - Duration : 기간

</details>

### 05. 특정날짜로부터 X일

- 개요 : 특정 일로부터 몇일이 지났는지 확인하기
- 체크사항
  - Font(글꼴) 적용하기
  - DatePicker : 날짜 고르기
  - 날짜 연산
  - 테마 적용하기 : Widget에 직접 Style을 넣지 말고 Default 디자인 사용

<details>
<summary>상세</summary>

1. 폰트-Asset
   1. 폰트 고르기 : Google Font에서 무료 Font 많음
   2. 폰트 asset>font에 넣고, pubspec.yaml에 등록

      ```Yaml
      fonts:
         - family: parisienne
            fonts:
            - asset: asset/font/Parisienne-Regular.ttf

         - family: sunflower
            fonts:
            - asset: asset/font/Sunflower-Light.ttf
            - asset: asset/font/Sunflower-Medium.ttf
               weight: 500 # 글꼴 두께
            - asset: asset/font/Sunflower-Bold.ttf
               weight: 700
      ```

   3. Text내에 text:TextStyle 설정
2. DatePicker 사용하기
   1. cupertino.dart 패키지 부르기 : IOS틱한 디자인 지원
   2. onPress 이벤트에 showCupertinoDialog 함수를 사용
      1. 이때 barrierDismissible: true 설정시 밖 화면 클릭으로 창 닫힘
   3. CupertinoDatePicker에 적절한 입력  
   (mode: CupertinoDatePickerMode.date, onDateTimeChanged:...)  
   4. onDateTimeChanged: (DateTime date){} 함수에 date 갱신
3. 테마 적용하기 : 글꼴을 분류해서 적용해보자
   1. main.dart에 theme:ThemeData()를 넣자.
   2. 자유롭게 이름을 짓고, build쪽에 final theme = Theme.of(context);
   3. 기존 style에서 style: textTheme.headline1 이런식으로 사용

</details>

### 06. 랜덤 숫자 생성기

<프로젝트 생략>

- 개요 : 랜덤한 숫자를 만들어보자.
- 체크사항
  - Navigation : 화면 이동
  - Button
  - Slider
  - 난수생성

<details>
<summary>상세</summary>

1. 난수 생성
   1. math 라이브러리 import
   2. 코드 작성

      ```Dart
      final rand = Random();

      final Set<int> newNumbers = {};

      // 중복 없이
      while (newNumbers.length != 3) {
         final number = rand.nextInt(maxNumber);

         newNumbers.add(number);
      }

      setState(() {
         randomNumbers = newNumbers.toList();
      });
      ```

2. Navigation으로 화면 이동
   1. Navigator.of(context).push() : route 스택에 이동할 곳을 넣음

      ```Dart
      // pop시 parameter을 돌려 받는 값
      final int? result = await Navigator.of(context).push<int>(
         MaterialPageRoute(
         builder: (BuildContext context) {
            return SettingsScreen(
               maxNumber: maxNumber,
               );
            },
         ),
      );
      ```

   2. Navigator.of(context).pop(전달 param) : route 스택에서 현 위치를 뺌 = 뒤로가기
3. Slider : SliderWidget 사용

      ```Dart
      Slider(
            value: maxNumber,
            min: 1000,
            max: 100000,
            onChanged: (double val) {
               setState(() {
                  maxNumber = val;
               })
            },
         ),
      ```

</details>

### 07. 동영상 플레이어

<프로젝트 생략> : 별 것 없음

- 개요 : 영상 플레이어
- 체크사항
  - video_player 플러그인
  - image_player 플러그인
  - Stack 위젯
  - AspectRatio 위젯

<details>
<summary>상세</summary>

1. 권한 부여
   1. IOS : ios>Runner>info.plist에 권한 및 description 추가
   2. android : 인터넷 Permission 필요 (http 영상 사용할때와 비슷)
2. imagePicker : Xfile 형태의 파일을 받아서 사용

</details>

### 08. 지도거리 앱

- 개요 : 지도에 마커를 새기고 거리가 가까우면 원 색이 변함
- 체크사항
  - Google Maps 지도 사용하기
  - 지도에 마커 표시하기
  - 지도에 동그마리 표시하기
  - 현재 위치 표시하고 위도, 경도 구하기
  - 위도, 경도간 거리 구하기

<details>
<summary>상세</summary>

1. 사용할 플러그인
   1. google_maps_flutter : 공식 구글 맵 아웃소스
   2. geolocator : 현재 위치 계산
      1. 권한 설정하기 : 정밀한 위치, 백그라운드 실행
2. 구글맵 API 키 받기
   1. google_map_flutter 링크 타고 가서 Get Started
   2. 기타 Google 제품 > Google Maps Platform
   3. 사용설정 API에서 Maps SDK for iOS와 Android 확인
   4. API 키는 사용자 인증정보에서 확인 가능
   5. 이후 pub.dev의 설명서 대로 세팅
3. 앱 권한 관리하기
   1. 위치 권한 관련 함수 제작

      ```Dart
      Future<String> checkPermission() async {
         final isLocationEnabled = await Geolocator.isLocationServiceEnabled();

         if (!isLocationEnabled) {
            return '위치 서비스를 활성화 해주세요.';
         }

         LocationPermission checkedPermission = await Geolocator.checkPermission();

         if (checkedPermission == LocationPermission.denied) {
            checkedPermission = await Geolocator.requestPermission();

            if (checkedPermission == LocationPermission.denied) {
            return '위치 권한을 허가해주세요.';
            }
         }

         // 영원히 앱에서 요청을 허가할 수 없음. 직접 세팅에서 해야 함
         if (checkedPermission == LocationPermission.deniedForever) {
            return '앱의 위치 권한을 세팅에서 허가해주세요.';
         }

         return '위치 권한이 허가 되었습니다.';
      }
      ```

   2. FutureBuilder 위젯을 사용.  
   future에 함수를 등록하고, 위 함수의 return이 해당 위젯 빌더의 snapshot에 담김
   3. future가 변경될때마다 build가 실행되므로 해당 내용을 반영
4. 지도 설정
   1. Circle을 이용해서 중심으로부터 일정 거리를 가지는 원 표시
   2. 타겟의 위치를 표시해 줄 Marker를 만들기
5. StreamBuilder를 이용해 지도에서의 위치 변경을 반영함
   1. stream이 변경시 아래의 builder가 실행되고 snapshot에 stream값이 담김
6. MapController을 만들어 이벤트 제어
   1. 최상단에 구글 맵 컨트롤러 생성
   2. 구글 맵 생성시 state로 저장하는 함수 생성
   3. 렌더링하는 쪽에서 onMapCreated: [함수이름]으로 함수 호출
   4. 렌더링되는 StatelessWidget쪽에서 맵 변수로 받음

</details>

### 배포

1. apk 파일 만들기
   1. Build > Flutter > Build APK

### 기타 Tip

- Alt+Enter 애용하자.
- Reformat Code with 'dart format' : 코드 자동 정리
- Setting > Keymap에서 원하는 동작에 단축키를 등록할 수 있음
- MaterialApp에 debugShowCheckedModeBanner: false 입력시 디버그 모드 표시 사라짐
- PlatformException 에러 발생시 console에 flutter clean 입력하고 재실행
- https가 아닌 http를 부르면 별도의 설정이 필요하다는 사실만 기억해 두자.
- SystemChrome으로 제어 기존 UI 제어 가능  
  - ex) SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.dark);
- Widget을 const로 지정해두면 build 함수에 따른 재실행을 막을 수 있음
