# LINUX Shell

## 개요

리눅스가 운영체제인것은 알고 있지만, 배포나 도커에 쓰이는 리눅스 사용법과 shell 명령어를 익한다는 의미로 30.Tools에 분류하였다. 필요에 따라서 이동할 수 있다.



## LINUX에 대하여 몇가지만

- 모든 것은 파일 : 모든 행동이 파일을 읽고 쓰는 것 처럼
  
  - 파일 네임 스페이스 : 전역 네임 스페이스 사용 
    ex - /media/a.jpg

- shell : 사용자와 컴퓨터 하드웨어 또는 운영체제간 인터페이스
  
  - 리눅스의 기본 shell : bash(Bourne-Again Shell), 기타 sh, csh, ksh
    리눅스의 명령어를 배움 = bash 명령어를 배움

- 여러명이 동시에 접속하고 작업하는데 특화된 운영체제 
  다중사용 운용체제 -> 로그인 필요
  
  - root : 슈퍼관리자 ID -> 여러명 동시 작업하기도 하고, 이곳에서 실행한것은 복구가 힘듬
  
  

## 간단한 명령어

- whoami : 로그인 된 사용자 ID

- sudo : root 권한으로 실행하기

- ls : 모든 파일 보기 : d(폴더인지), 권한, 소유자, 파일 크기
  
  - ls -al : 숨김 파일까지 보기
  
  - . : 현재 폴더
  
  - .. : 상위 폴더

- pwd : 현재 디렉토리 위치

- cd : 디렉토리 이동

- chmod : 파일 권한 변경

- cat : 파일 보기

- rm : 파일 및 폴더 삭제 (-r : 하위까지 삭제,  -f:강제 삭제)

- grep : 검색 명령



## 리다이렉션과 파이프

- 리다이렉션 : 표준 스트림(stdin stram)의 흐름을 바꿈
  
  - <, > 를 사용
    
    - 응용프로그램 > 파일 : 파일에 해당 출력 결과를 집어 넣음
    
    - 응용프로그램 >> 파일 : 파일에 해당 출력 결과를 기존 밑에 집어 넣음

- 파이프 : 한 프로그램의 출력을 다른 프로그램의 입력으로 사용
  
  - |을 사용



## 프로세스

- 실행 중인 프로그램

- 리눅스는 기본적으로 다양한 프로세스가 실행됨
  
  - 유닉스 : 여러 프로그램이 유기적으로 각자의 일을 수행하면서 전체 시스템이 동작
  
  - 각각의 기능을 만들어서 연결해서 실행 (파이프 등 사용)

- 프로세스 실행방법
  
  - foreground : 일반 실행 방법. 해당 명령 실행 중 수행 종료까지 사용자는 다른 입력을 할 수 없음
  
  - background : 사용자 입력과 상관없이 실행되는 프로세스, 명령 뒤에 &를 붙이면 됨
    명령이 제대로 입력될 경우 작업번호와 process ID를 보여줌, 

- 프로세스 제어
  
  - 작업 취소 : Ctrl + C
  
  - 프로세스 확인 : -ps
  
  - 프로세스 중지 : kill % 작업번호 / kill pid     (강제 종료 옵션 -9)



## 하드 링크와 소프트 링크

- cp : 파일 복사 (-rf : 하위 폴더 포함)
  
  - cp A B : A파일을 B파일로 복사하고, 각각의 물리적 크기를 가짐

- 하드 링크ln A B) : 용량은 가지지 않지만 같은 파일을 가리킴 A를 지워도 B로 접근 가능

- 소프트 링크 : ln -s A B -> 바로가기 생성 : A를 지우면 B로 접근 불가



## 우분투 패키지 관리

- 리눅스에는 여러 배포판이 존재, 현재 도커 진행을 위해서만 쓸 것인데 우분투를 채택

- 우분투 패키지 인덱스 정보 업데이트 : sudo apt-get update

- 우분투 패키지 업그레이드(위험, 함부러 하지 말 것) : sudo apt-get upgrade 

- 패키치 설치 : sudo apt-get install 패키지명

- 패키지 삭제 : sudo apt-get remove 패키지명 (--purge : 설정파일 포함 옵션)



## VIM 에디터

- Vi improved : 전통적 유닉스 에디터(Vi: Visual Editor)에 자동화 시각화를 추가
  
  - 리눅스 설치 : sudo apt-get install vim
  
  - 이거 아니면 Emacs 사용

- 단순한 명령어
  
  - 새파일만들기 내지 들어가기 vi a.txt
  
  - 입력모드로 변경 : a, i(현 위치 시작), o 
  
  - 일반모드로 변경 : esc (일반 모드에서 x 누르면 한 문자 삭제)
  
  - 마무리 : <:w = 저장, :q = 종료, :wq = 저장 후 종료, :q! = 강제종료>



## Ubuntu 20.04 환경에서 Docker 설치

1. 최신 패키지 리스트 업데이트
   - sudo apt update
2. docker 다운로드를 위해 필요한 https 관련 패키지 설치 (띄어쓰기 기준 4개 설치)
   - sudo apt install apt-transport-https ca-certificates curl softwareproperties-common
3. docker repository 접근을 위한 GPG key 설정
   - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
4. docker repository 등록
   - sudo add-apt-repository "deb [arch=amd64]
     https://download.docker.com/linux/ubuntu focal stable"
   
   - 안 될 경우,
     sudo add-apt-repository "deb [arch=amd64]
     https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
5. 등록한 docker repository 까지 포함하여 최신 패키지 리스트 업데이트
   - sudo apt update
6. docker 설치 (버전확인 docker -v)
   - sudo apt install docker-ce
7. docker 실행 중임을 확인
   - sudo systemctl status docker 
     (24시간 돌아가야 하므로 systemctl이라는 데몬으로 지원)



## Tip : sudo 명령 없이 docker 명령어 제어

1. 현 사용자 ID를 docker group에 포함
   
   - sudo usermod -aG docker ${USER}
     (유저 ID집어 넣으라는게 아니라 진짜 이게 명령어)

2.  로그아웃(exit) 후 ssh -i ~~ 로 다시 접속시 그 이후 부터는 반영
    (반영 여부 확인 : id -nG 입력시 docker가 포함되어 있음)



## Ubntu 20.04 환경에서 Docker-compose 설치

1. Docker-compose 설치 (길어서 안될경우 집적 입력)
   $ 부분 처리 때문에 형식 다르게 표기
   
   ```
   sudo curl -L "https://github.com/docker/compose/releases/download/2.2.3/dockercompose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```
   
   버전 변경 할 경우, 최신 버전([Releases · docker/compose · GitHub](https://github.com/docker/compose/releases)) 확인 후 2.2.3 부분 교체!
   
   설치 확인 : docker-compose --version

2. 실행 권한 주기 (현재 docker-compose는 현재 설치 되지 않고 다운로드만 받은 상태)
   
   - sudo chmod +x /usr/local/bin/docker-compose
