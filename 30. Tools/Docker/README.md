# Docker

## 개요

리눅스의 컨테이너 기술을 이용하여 애플리케이션을 묶어서 실행, 배포 할 수 있게 해주는 오픈소스 SW 중 하나, 거의 표준

### 장점 / 쓰는 이유

- 개발, 테스트, 서비스 서버 등 다양한 환경을 쉽게 관리

- 어디서든 구동 가능한 환경 구축

- 확장과 축소가 쉬움

- MSA(Micro Service Architecture), Devops에 적합

### 가상머신과 차이

- 상대적으로 오버헤드가 적음
- OS의 중복 설치가 필요 없고, 호스트의 OS 자원을 쓰므로 월등히 빠름
- 이미지(실행파일)가 작고 관리가 쉬우며 배포가 쉬워짐

### 이미지와 컨테이너

- 컨테이너 : 독립적 Application 프로세스 (cpu, memory, Id 등을 각각 보유)
- 컨테이너 이미지 : Application들이 실행될 수 있도록 모아진 이미지들의 조합

- 서버 구성에 필요한 파일들의 모음
- 라이브러리, 실행 파일, 설정 파일 등을 포함
- 배포 단위로 저장소에 push / pull 가능
- 컨테이너(프로세스)는 이미지(실행파일)을 실행한 형태
- Hub.docker.com : 수많은 컨테이너들이 저장된 웹상의 공간

### 레지스트리

- 컨테이너 보관 창고 / hub.docker.com : 각종 이미지들에 대한 사용 설명서도 첨부 되어 있음
- 개인 레포지토리는 레지스트리의 하위 속성
- 그것과 별개로 레지스트리 운영을 도와주는 registry라는 이름의 컨테이너도 있음 -> private registry 만들때 사용

### 볼륨

- 컨테이너가 만들어주는 데이터를 영구적으로 보존
- 데이터 보존, readonly service 지원, 데이터 간 공유를 지원

## 설치

### windows10에 DockerDesktop 설치 (Install Docker Desktop on Windows)

WSL2(Windows Subsystem for Linux v.2)윈도우는 윈도우 환경에서 리눅스 커널을 실행할 수 있게 아예 서브시스템을 만들었음

-> 가상머신보다 빠름

1. 가상화 설정 (BIOS 에서 SVM을 enable로 변경)
2. 리눅스 커널 업데이트하고 넣기
3. 커널 안에서 Docker 실행

### Dockerfile 만들고 컨테이너 빌드하기

Dockerfile : 쉽고, 간단, 명확한 구문을 가진 textfile로 컨테이너 이미지를 생성할 수 있는 명령어의 집합

Dockerfile 지시어로 작성

```Markdown
# 이렇게 주석 작성
FROM 베이스 이미지, 무조건 맨 위에 있어야 함
COPY 호스트의 파일을 컨테이너로 복사
EXPORT 서비스할 포트
ENTRYPOINT : CMD와 함께 사용하면서 command 지정 시 사용 ; 명령어 역할
CMD 동작시 자동으로 실행할 서비스나 스크립트 지정 ; argument 역할
```

그 이후 docker build -t [이미지명]:tag 로 컨테이너를 만들 수 있음

## 통신

### eth0

- 입구가 되는 인터페이스
- 호스트의 포트는 단 하나

### Docker0 통신 구조

- 172.17.0.1을 가지고 게이트 역할을 하고, running시 IP 주소 할당

- bridge : 네트워크 간 연결을 지원
- --link : 컨테이너 간 연동

### Port-forwarding

- container port를 외부로 노출시켜 연결 허용

### User Defined bridge network

- 기본 Docker0에서 할당하는 주소 방식은 static하지 않기 때문에, 이 부분을 static하게 만들고 싶으면 bridge를 만들어 쓸 수 있음
- docker network create --driver bridge --subnet 192.168.100.0/24 --gateway 192.168.100.254 [bridge 이름]
- 이제부터 docker run 옵션에 --net [bridge이름]을 사용하여 static하게 ip set이 가능해짐

## 도커 컴포즈

- 여러 컨테이너를 일괄적으로 정의하고 실행할 수 있게 yaml 파일로 설정하는 툴

- 주의사항 : depends on - 컨테이너간의 종속성을 정의. 정의한 컨테이너가 먼저 동작되어야 한다.(db 먼저 실행해라 같은 것)

- docker-compose 명령어 (docker 명령어와 비슷)

  ```Markdown
  docker-compose config : 문법 체크
  docker-compose up -d : (-d : 백그라운드) 실행 요청
  docker-compose ps : 실행 상태 확인
  docker-compose scale mysql=2 : mysql 컨테이너 수를 2개로 늘려줘
  docker-compose down : 실행중인 컨테이너를 종료
  ```

## 웹 서버 실행 단계 (빌드 및 운영)

1. 서비스 디렉토리 생성
2. 빌드를 위한 dockerfile 생성

3. docker-compose.yml 생성
4. docer-compse 명령어

## 명령어 모음

- docker search [이미지명] : Hub에 컨테이너가 있는지 확인
- docker pull [이미지명]:version : 이미지 다운 받기 (ex- docker pull nginx)
- docker images : 현재 이미지 확인
- docker inspect [이미지명] : 해당 이미지 자세히 보기
- docker rmi [이미지명] : 이미지 삭제
- docker tag [이미지명]:[변경이미지명] : 이미지 이름 변경 ; 빌드시 [개인 아이디/[이미지명]]의 형태로 만들어야한다.

- docker create --name [컨테이너명] [이미지명] : 컨테이너 생성
- docker start [컨테이너명] : 컨테이너 실행
- docker stop [컨테이너명] : 컨테이너 정지

- docker run -d --name web -p 80:80 [이미지명]:latest : 실행 예시 - 해당 이미지를 80포트로 이름을 붙여서 실행
- docker ps : 현재 실행중인 컨테이너 확인
- docker inspect [컨테이너명] : 컨테이너 세부정보 확인
- docker rm -f [컨테이너명] : 컨테이너 삭제
- docker logs [컨테이너명] : 해당 컨테이너가 만들어낸 로그 출력
- docker top [컨테이너명] : 컨테이너에서 실행중인 프로세스 출력
- docker exec -it [컨테이너명]/bin/bash : 컨테이너에 직접 접속하여 배시 쉘 사용

- docker run -d -v [호스트 경로]:[컨테이너 mount path] (:[read write mode]) : 볼륨 마운트
- docker volume command : 볼륨과 관련된 커맨드 실행

- alias [단축어 명] = "[명령어]" : 자주 사용하는 명령어를 단축어로 등록

- docker login : 도커 로그인
- docker push [아이디]/[이미지명]:버전 : Hub 개인 Repository에 배포

쓰일법한 옵션

```Markdown
--help : 자세한 설명 뜸
-f : force / filter / follow(실시간) : 다양함
-d : 백그라운드 모드
-p : 포트
-a : 모든
-i : interactive
-t : terminal
--restart : 리스타트 정책
--no-trunc : 생략 없이 full name
```

## 참조

따배도 시리즈
