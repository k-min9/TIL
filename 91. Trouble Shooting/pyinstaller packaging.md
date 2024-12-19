# Pyinstaller packaging 중 TS

- 개요
  - pyinstaller : py를 venv 포함 exe 파일로 빌드하는 라이브러리
    - venv 실행 중 실행하면 venv째 패키징해주지만 여기서 문제가 마구생긴다.
    - pyinstaller main.py --onefile --noconsole

## 경로 찾기

- 문제 : package_resource 관련 함수가 file을 찾을 수 없음
- 해결 : 해당 내용을 "./"로 시작하는 주소로 위치를 전부 변경
- 문제 : os.path.dirname(__file__) 계열 또한 위치를 찾지 못함
- 해결 : 동일, config_file_path = os.path.join(".", config_path) 라는 식으로 해결했지만 동일하다.

## torchscript와의 충돌

- 최대난제, torch 라이브러리가 참조해야 할 원본 source py를 못찾아 충돌
- 해결 : 오래된 이슈였음. github에서 몇 가지 해결법을 소개해 주어서 해결.
  - 범인은 @torch.jit.script. 어노테이션 torch 라이브러리 참조중 해당 어노테이션을 @torch.jit._script_if_tracing로 변경

## TIP

- 옵션에 no-console을 넣자. 오류시, 오류 메시지를 단락적으로 볼 수 있다.
- 변환된 exe를 바로 쓰지말고 bat를 만들어 실행하면 log를 남길 수 있다.
(여러 프로그램 동시 실행시 log로 쓸 txt 파일이름 그때 그때변경 필요)

  ```bat
  @echo off

  main.exe > log2.txt
  deactivate
  ```

  - 빌드 연습을 위해 venv째 통째로 복사를 해와도 설정이 기존 폴더의 venv를 참조할 수 있기때문에 민감한 경우나, venv 내의 수정이 필요한 경우, venv는 지우고 새로 설치하자.
