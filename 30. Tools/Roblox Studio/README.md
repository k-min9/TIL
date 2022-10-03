# 로블록스

- 개요 : 무료 서버, 멀티 플랫폼, 결제 모듈
- 언어 : LUA
- 도구 : Loblox Studio
- 문서
  - docs : <https://create.roblox.com/docs>
  - Devhub : <https://developer.roblox.com/en-us/>

## 로블록스 스튜디오

- UI (보기(View)에서 활성화 가능)
  - 도구상자 : 좌측에서 Template 생성
  - 탐색기(Explorer)
    - WorkSpace : 상위 개체(Object, 객체 아님 ㅎㅎ) 위치. 각종 물건 세팅
      - Scripts : LUA 스크립트
    - ServerStorage : 보관함, 실행시 이곳의 스크립트가 작동하지 않음
      - 유니티로 따지면 Prefab 보관에 적합
      - 클라이언트로 복사되지 않아서 스크립트나 맵 도용을 막을 수 있음
  - 속성(Properties) : 객체의 속성(특징, 상태)을 보여줌
  - 출력(Output) : 스크립트 결과/에러 등을 표시하는 콘솔
- 용어
  - Spawn : 캐릭터 생성 위치
- 단축키
  - F5 : 일반 실행
  - F8 : 플레이어 스폰 없이 스크립트 실행
  - Ctrl + / : 주석
  - Ctrl + F : 검색
  - Ctrl + Shift + F : 전체 검색
- Command bar : 실행 중, 게임 중에 한 줄 스크립트를 즉시 실행 가능

## LUA

- 특징
  - 함수 선언 및 호출 순서가 엄청 중요! 기본적으로 맨 위에서 선언하자.
  - 자바스크립트 급으로 컴파일 에러 능력이 없다. 특히 자료형 관련.
- 내용
  - local을 조건문 내부에서만 선언하여 쓸 수 있음
    - local 변수 = a or b : a가 있으면 a 없으면 b
      ex) local chara = player.Character or Player.CharacterAdded:Wait()
  - 전역 변수처럼 쓸 수 있는 value 제공
  - table : 배열 + dictionary
    - 배열 : local arr = {1234, "string", true, model.Part1}
      - 인덱스가 0이 아니라 1부터 시작
      - .insert : 추가 / .remove : 제거
      - #배열명 : 배열 크기
    - dictionary : key와 value로 이루어짐
    ex) local dic = {name="1", ["level"]=99, isChara=true}
  - null이 아니라 nil
  - ~= : 반대, 조건문에서 다른지 chk
  - float, number, double casting 부담 없이 써도 됨
  - 문자열 합치기 ..
    - "2".."7" ->"27"
    - "2" + "7" -> 9
  - and, or, not : 논리연산자
  - table : Lua의 유일한 자료구조
  - 주석은 한 줄은 bar 두개 (--), 여러줄은 대괄호 사용(--[[]])
- 개체 : 대소문자에 유의할 것!
  - workspace : 일반적으로 시작하는 상위 개체
    - <객체위치.객체내용>이나 <객체위치["하위객체"].객체내용>등으로 접근
    - 객체위치["하위객체"]사용해야 되는 경우
      - 숫자로 시작하는 객체 이름을 적을때 사용
      - 띄어쓰기가 있는 경우
      - 개체가 한국어로 되어있는 경우
  - game : game 관련 서비스 개체. 최상위 개체 (workspace의 Parent)
    - 예시
      - game:GetService("RunService")
        - GetService는 Workspace에 보이지 않는 서비스도 호출 가능
      - game.Players:GetPlayers()
    - Service
      - MarketplaceService : 게임 내 판매 관련 함수
      - ContextActionService : 플레이어 키보드, 마우스 조작 관련 함수
      - Debris : 시간 차 삭제 등의 함수를 제공
  - script : Script 본체. script.Parent.Color 등으로 조절 가능
  - .new : 꽤 많은 특수형태(Instance, Color, Vector3...)에 입력으로 쓸 수 있음
- 함수
  - 함수 block, 반복문, 제어문 전부 end로 끝남
    - 무한 반복 추천 : while wait() do ~ end
    - 배열 반복 : for i, v in ipairs(반복대상) do ~ end
    - dictionary 반복 : for i, v in pairs(반복대상) do ~ end
  - math : 수학 연산 관련 함수 제공
  - wait(x) : x초 대기
  - FindForChild : 하위 객체 접근용. 없어도 error가 아닌 nil값이 나옴
    - 비슷한 함수 : FindFirstAncestor, FindFirstChildOfClass, FindFirstChildWhichisA
  - WaitForChild : 서버는 맵 로딩을 기다림. 단, LocalScript들은 그렇지 않음
    - 지금 당장은 없어도 객체가 생성될때까지 기다려줌
  - Destroy : 파괴
  - Clone : 복사
    - 그 후 생성물.Parent = workspace 등으로 이동해줘야함
    - Prefab 마냥 Instance.new 쪽이 효율적이지만 복합체면 이쪽이 좋다.
  - MoveTo : Part와는 다르게 position이 없는 모델의 위치 지정 함수.
    - PrimaryPart를 기준으로 좌표를 잡음, 비어있을 경우 bounding box의 중앙
- eventListener : 호출하는 함수에는 매개변수 및 괄호를 넣지 말 것
  - Connect : 이벤트마다 함수 호출해주는 함수
    - Service.Heartbeat:Connect(함수) : 프레임마다 이벤트(함수) 실행
    - Service.Ended:Connect(함수) : 서비스 종료시 함수 실행
  - Wait : 이벤트가 발생할 때까지 기다려주는 함수
    - part.Touched:Wait()
  - ChildedAdded : 하위 Child 생성시
  - Changed : 속성이 변경되었을때, 반환값은 변경된 속성 이름
    - GetPropertyChangedSignal("속성이름") : "속성이름" 속성이 바뀌었을때만 호출, 반환 없음
  - game.Players.PayerAdded : 게임에 새 플레이어가 들어왔을때 발생
  - CharacterAdded : 캐릭터가 스폰되었을때 발생
- Bindable Event : 다른 스크립트의 함수나 이벤트를 매개변수와 함께 주고 받을 수 있음
  - 단, table["문자열"]이라던가 metatable등의 값은 매개변수로 전송되지 않음
  - 로컬 <> 서버간에는 통신할 수 없음
- 배포
  - 플레이어 구성 후, 비공개에서 공개로 전환
  - 저장 > 게시

## 자주 쓰이는 속성

- Name : 이름
- Health : 0이 되면 해당 캐릭터 kill
  - hunmanoid:TakeDamage() : 'humanoid.Health -= 감소값'과는 다르게 Forcefiled(무적상태)가 아닐때만 데미지를 줌
- Transparency : 투명도
- CanColide : 충돌 가능
- Anchored : 파트 위치 고정
- Enum : 해당 속성의 선택지 상위 개체. 그러니 문자열로 하드코딩하지 말 것!
- Data > Classname : Devhub에 검색하기 좋음
- CFrame : Position + 회전도, 스크립트로만 제어 가능, 위로 밀리지 않고 겹침
  - 더하기 연산시 Position과 동일한 연산에 회전도만 더함
  - 곱하기로 연산시 파트가 바라보는 방향으로 이동
    - part.CFrame * CFrame.Angles(math.rad(-30),0,0) : x축 30도 회전
  - GetPivot으로 Get하고, PivotTo로 Set
  - CFrame.lookAt(보는파트.position, 대상파트.position)으로 바라보기

## 멀티 환경

- 서버 구조 :서버와 클라이언트
  - 지금 내가 로블록스를 쓰려는 이유. 멀티 + 매치메이킹!
  - 중요한 연산은 서버에서, 아니거나 편의적인 것(GUI)은 클라이언트에서
  - 플레이어의 행동 내지 플레이어가 영향을 끼치는 행동은 클라이언트에서 연산하고 서버에서 보고하는 식이라 관련 핵에 취약하다.
  - ServerStorage, ServerScriptService 등은 클라이언트로 복사되지 않아서 스크립트나 맵 복사 및 도용을 막을 수 있음
- LocalScript : 클라이언트에서만 돌아가는 스크립트
  - 작동장소
    - ReplicatedFirst
    - StarterGui > PlayerGui
    - StarterPack > Backpack
    - StarterPlayerScripts > PlayerScripts
    - StarterCharacterScripts > 플레이어 캐릭터 모델
  - 특징
    - game.Players.LocalPlayer로 현재 Localscript가 돌아가는 플레이어를 사용할 수 있음
      - 참고로 game.Players:GetPlayerFromCharacter(모델)로 그 캐릭터의 플레이어 개체 반환
    - Local에서 Server의 내용물을 찾을때는 선로딩문제때문에 WaitForChild를 써야 함
      - ServerScript도 Clone이나 Instance.new로 생성된 개체를 다룰때는 써야한다.
- 리모트 이벤트
  - ReplicatedStorage에 RemoteEvent 생성
    - 서버 클라이언트 양쪽 모두 쓰는 개체는 여기서 제어하자
  - Bindable 이벤트와 같은 변수 제약을 가지고 있음
  - 로컬 -> 서버
    - 송신 : FireServer
    - 수신 : OnServerEvent:Connect
  - 서버 -> 로컬
    - 송신 : FireClient, FireAllClients
    - 수신 : OnClientEvent:Connect
- 테스트
  - 서버 환경, 클라이언트 환경, 양쪽 환경에서 볼 수 있음

## 바이러스 분별법

- 배경 : 마켓에서 바이러스가 숨겨진 Template이 있음
