# Android RE

## 개요

- 안드로이드의 유니티 게임은 해킹이슈로 mono보다 IL2CPP로 빌드하는 경우가 많다.
- IL2CPP라는 말대로 IL코드를 IL2CPP.exe에 의해 C++ 코드로 변환하고, 네이티브 라이브러리(so)파일을 생성하는 방식
  - 이번 소규모 프로젝트에서 많이 만날 파일은 'libil2cpp.so'
- 준비물 : libil2cpp.so와 metadata
  - libil2cpp.so의 위치 : apk 내부
  - metadata의 위치 : android/data 폴더 내부

## 기반 데이터(Assets) 확보

- 코드와 구조를 파악해도, 그것이 적용될 내용물이 없으면 의미가 없음
  - 내용물에 접근 할 수 있는지 Assets를 확인해보자
- 대부분의 데이터는 Android의 data 폴더에 있는 경우가 많다.
  - data 폴더 구조 예시
    - Unity, Spine, WebGL 관련 이하, Assets 폴더
    - 음성, 영상, 그림 관련 이하, Media 폴더
    - 스크립트, 수치, 테이블 관련 이하, Table 폴더
    - 구조나 내용물에 대한 Metadata를 담은 hash,json식 Catalog
- 주의사항 : 상업활동이나 공개목적이 아닌 개인의 학습, 연구에 대해서 막는 곳은 거의 없지만 문제 없는지 약관 등을 확인해보자.

## AssetStudio

- 우선 Assets 폴더의 내용물을 볼때 가장 접근이 쉬운것이 AssetStudio이다.  
  <https://github.com/Perfare/AssetStudio/releases>
- 해당 프로그램에 Assets 폴더의 내용물을 Load File을 한 후에
- Export > All Assets로 저장할 폴더를 넣으면 내용물을 볼 수 있다.
- 관련 참고 프로젝트 : <https://arca.live/b/bluearchive/40797379>
  - 이걸 WebGL이나 안드로이드 버전으로 만들 경우, 일반 App에도 해당 Asset을 사용할 수 있음

## IL2CPP Dumper

- 게임의 실질적인 정보를 담고 있는 libl2cpp.so를 언패킹하여 덤핑(복사)해보자.
- 이때 사용하는 툴이 fridump 등 여럿있지만 IL2CPP Dumper를 사용하겠다.  
<https://github.com/Perfare/Il2CppDumper/releases>
- 실행시 각각 metadata와 libil2cpp.so의 위치를 입력해주면, DummyDll폴더를 생성해준다.
  - 내부는 핵심 로직부터 사용 라이브러리까지 확인가능한 모든 함수 이름과 input, output을 알 수 있는 dll 파일들로 구성되어있다.

## ILSPY, DNSPY, DOTPEEK

- IL2CPP Dumper로 추출한 Dll들은 그 자체로는 읽을 수 없다.
- 이때 형식에 맞춰 Dll들을 읽고 Decompiling 해주는 프로그램이 ILSPY, DNSPY, DOTPEEK(무려 JetBrains산) 등등이다.
  - 툴들이 거의 다 비슷하게 dll을 읽고 export해주는 기능이 있음
- 이번에는 그 중에서 ILSpy를 사용해보겠다. self contained는 무설치로 GUI를 제공해서 편하다.
<https://github.com/icsharpcode/ILSpy/releases>

1. ILSpy.exe 기동
2. Open으로 dll열기
3. 저장할 폴더를 하나 만든 후, Save Code로 해당 Dll을 디컴파일링한 내용을 저장

## IDA, Ghidra

- 디컴파일링 된 파일로 확인할 수 있는 건 cs파일 이름과 구성 변수와 메소드 이름, in, out 정보 정도다.
- cs 파일 내에 아래와 같은 내용이 가득하다고 보면 된다.

  ```cs
  [Token(Token = "0x1000001")]
  [Address(RVA = "0x2000001", Offset = "0x2000001", VA = "0x2000001")]
  public static string getShop(string text)
  {
    return null;
  }
  ```
