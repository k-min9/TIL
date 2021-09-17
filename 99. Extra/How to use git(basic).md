# git Basic



## 기본적인 명령어

```
git init : 깃 시작
git remote add origin <URL> : 특정 URL의 깃허브, 깃래브 등과 지역 저장소를 연결, origin도 이름임 (origin/master)

git add . : 스테이지 위에 변경 내용을 올림
git commit -m '<commit message>' : 간단한 메세지를 추가
git push origin master : 원격 저장소에 올리기

git log : 로그 보기
git log --oneline : 로그를 약술 한 줄로 보기
(내용이 길어지면 q 눌러서 다음 화면으로 넘어갈 수 있음)

git status : 변경사항, 스테이지 등 볼 수 있음

git clone <URL> : 대상 원격 저장소 내용 전부 가져오기
git pull origin master : 원격 저장소 변경 내용 전부 가져오기
```



## git branch

브랜치 : 단순한 포인터

HEAD : 현재 내가 작업중인 커밋을 가르키는 포인터 (HEAD가 master에 있다 = master에서 작업 중)

통합 브랜치 : 언제든지 배포할 수 있는 브랜치

토픽(피처) 브랜치 : 단위 작업을 위한 브랜치



### 생성

```
git branch : 현재 브랜치 리스트 볼 수 있음
git branch <브랜치 이름> : 브랜치 생성
git switch <브랜치 이름> : 브랜치 이동
(어차피 세트로 오니까 branch, switch 합쳐서 'git switch -c <브랜치 이름>'으로 적을 수 도 있음)
git branch -d <브랜치 이름> : 브랜치 삭제
```

(앞으로 브랜치 이름을 b~로 통일하겠다)

이 상태로 커밋 시, 브랜치는 마스터와 같은 곳을 가르키는 포인터가 아니라 자라난 가지를 가르키는 포인터가 된다.

이제 새 브랜치에 add > commit > push 하면 마스터에는 존재하지 않고 브랜치에서만 형상관리가 된다.



### 병합1. Fast forward (마스터가 브랜치가 걸은 길을 걸음)

```
git switch master : 합쳐질 위치로 이동
git merge b1 : master가 b1을 흡수하겠다.
git log --oneline --graph : 브랜치 그래프까지 볼 수 있음
```

다 사용한 브랜치는 지워서 그래프를 깨끗하게 하자(머지 리퀘스트 기본값)

### 병합2. Auto Merge(마스터가 브랜치를 병합하면 자동으로 커밋됨)

### 병합3. Manual(Conflict) Merge

merge로 합칠때 ! 뜬 파일이 생기면서 자동 머지가 되지 않는 경우. 

무언가 잘못된게 아니라 당연히 나는 거다.

이유) 합치려는 브랜치 들의 작업내용이 충돌함

해결) 

Interactive mode : 선택 방법으로 삭제

(VSCode는 IDE차원에서 ! 파일의 HEAD(현재 작업)와 Incoming(병합 되려는 자료) 선택을 지원해준다.)

Edit inline : 직접 그 부분 작성하기



## 원격 저장소 (feat. 협업)

저장소 > settings > protected branches 에서 마스터 브랜치 푸쉬를 막을 수 있음

```
A와 B가 각각 브랜치 dev-a, dev-b를 만들고 작업중

1. add와 commit만 본인의 브랜치에 작업을 하고, 
2. push는 'git push origin dev-a'(현재 브랜치 이름과 동일해야 한다.)
3. 원격 저장소에서 merge request를 보낸다.(Assignee : 결재하는 사람)
4. 각각 git switch master > git pull origin master로 지역 저장소 내용을 최신화한다.
5. 직접 브랜치 지우기 'git branch -d dev-a'
```





