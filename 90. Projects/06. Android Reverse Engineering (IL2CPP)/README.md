# Android RE

## 개요

- 안드로이드의 유니티 게임은 해킹이슈로 mono보다 IL2CPP로 빌드하는 경우가 많다.
- IL2CPP라는 말대로 IL코드를 IL2CPP.exe에 의해 C++ 코드로 변환하고, 네이티브 라이브러리(so)파일을 생성하는 방식
  - 이번 소규모 프로젝트에서 많이 만날 파일은 'libil2cpp.so'
- 준비물 : libil2cpp.so와 metadata
  - libil2cpp.so의 위치 : apk 내부
  - metadata의 위치 : android폴더 assets 내부
