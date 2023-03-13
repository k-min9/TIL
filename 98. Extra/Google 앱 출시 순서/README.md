# Google 앱 출시

## 개요

- 앱을 출시하기 위한 신청 과정을 정리해보자

## 기본

1. android\app\src\main\res\AndroidManfest.xml(이하 menifest)에서 세팅
   1. 앱 이름/아이콘 설정

## 아이콘

1. 1024*1024 사이즈 이미지 준비
2. 앱을 사이즈 별로 변환
   - 앱 아이콘 변환 : <https://www.appicon.co/>
     - 기본 : ic_launcher
   - 변환 png를 jpg로 명명하고 다시 png로 변환 : <https://jpg2png.com/ko/>
3. 변환 jpg 삭제하고 덮어 씌우기
4. android\app\src\main\res에 덮어 씌우기

## 광고

## 앱 설정

- 공통
  - 구글 플레이 콘솔 : <https://play.google.com/console>
- 개인정보 처리방침 등록
  1. <https://sites.google.com/new>에서 새 사이트 시작
  2. 기존 글 내지 [개인정보포털](https://www.privacy.go.kr/front/main/main.do) 참고하여 개인정보 처리방침 작성
  3. 주소를 등록
