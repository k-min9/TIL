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



## 설치

### windows10에 DockerDesktop 설치 (Install Docker Desktop on Windows)

WSL2(Windows Subsystem for Linux v.2)윈도우는 윈도우 환경에서 리눅스 커널을 실행할 수 있게 아예 서브시스템을 만들었음

-> 가상머신보다 빠름

1. 가상화 설정 (BIOS 에서 SVM을 enable로 변경)
2. 리눅스 커널 업데이트하고 넣기
3. 커널 안에서 Docker 실행



## 명령어

- docker search [이미지명] : Hub에 컨테이너가 있는지 확인
- docker pull [이미지명]:version : 이미지 다운 받기 (ex- docker pull nginx)

- docker images : 현재 이미지 확인
- docker rmi [이미지명] : 이미지 삭제



- docker run -d --name web -p 80:80 [이미지명]:latest : 실행 예시 - 해당 이미지를 80포트로 이름을 붙여서 실행

- docker ps : 현재 실행중인 컨테이너 확인

- docker rm -f [컨테이너명] : 컨테이너 삭제

- 



```
-f : 강제 종료 후 삭제 옵션
```

