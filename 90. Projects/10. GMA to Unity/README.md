# Garry's mod to Unity

- 개요 : 2차창작 모델이 많은 Garry's mod(통칭 GMOD에서) 모델을 가져와보자.

## 파일 다운로드

1. Gmod의 창작마당(Workshop)에서 원하는 모델을 검색/선택한다.
2. 주소를 복사한다. <https://steamcommunity.com/sharedfiles/filedetails/?id=> 의 형태가 된다.
3. <https://steamworkshopdownloader.io/>에서 파일을 다운로드 할 수 있다.
4. 이때 SteamCMD가 필요하다. 구동후 login anonymous 입력해 놓자.
   1. 없을 경우 다운로드 하는 법까지 해당 사이트에서 안내해준다.
   2. 다운로드링크 : <https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD>
5. <https://steamworkshopdownloader.io/>에 주소를 입력해 나온 명령문을 SteamCMD에 입력하면, 특정위치에 파일을 저장하는데 성공했다는 안내문이 나온다.
6. 해당 경로로 이동하면 gma 파일이 있는 것을 확인할 수 있다.

## Gma 파일 언패킹

1. Gmad와 Crowbar이라는 tool이 대표적이지만, Gmad는 때때로 header가 고장난다는 보고가 있고 경험해봤기 때문에, crowbar로 진행하겠다.
   1. 인터넷 검색으로 쉽게 [다운로드](https://steamcommunity.com/groups/CrowbarTool) 할 수 있다. 작성시점 버전 0.74로 진행
2. Crowbar 열어 unpack으로 이동하거나, gma 파일을 crowbar.exe로 드래그 & 드롭하여 unpack하자.
3. 산출물은 mdl과 vtx 파일이다.
4. vtx는 VTXEdit을 통해 png로 바꾸고, mdl은 그대로 Crowbar로 Decompile하거나, Neosis를 이용하는 방법이 있다. 각각의 장단점이 있음

## VTF edit

1. vtf파일을 열고 png로 저장

## Decomipile-1. Neosis

1. Crowbar에서 unpack된 mdl을 Open File
   1. 여기서도 png 변환이 가능하다.
   2. 변환된 png를 여기서 mapping 해줄 수 있다.
2. 모델 확인 후 우클릭 export
3. 산출물은 fbx. 즉, 유니티에 넣을 수 있는 상태이다.
   1. fbx와 material로 쓸 png들을 한 폴더에 같이 넣어주면 일단 끝.

## Decomipile-2. Crowbar

1. unpack한 mdl을 decompile 메뉴에서 qc와 smd로 바꿀 수 있다.
   1. qc : 모델의 메쉬, 애니메이션, 히트박스, 물리 설정 등 모델 그 전체를 정의하는 스크립트 파일.
   2. physics : 'GMOD'에서의 충돌설정, ragdoll, 애니메이션 등의 정보가 담김
      1. 테스트 후 결론 : Blender 최초 로딩때는 필요하지만 Unity에서는 필요없음
   3. smd : 각종 refrence model들
2. Blender로 qc를 import하기
   1. qc, smd를 읽을 수 있게 Blender Source Tools 설치 <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>
3. 여분의 자료는 제거하고, smd의 역삼각 선택하여 shading 모드
4. 중간 object > view, select, add, Node 적혀있는 칸에서 add > texture > image texture 선택 해서 node 만들기
5. Image Texture의 color을 principled bsdf 의 base color과 연결
6. Image Texture에서 open 후 png열기
7. export > Fbx로 파일 빼고, fbx와 material로 쓸 png들을 한 폴더에 같이 넣어주면 일단 끝.
