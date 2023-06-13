# Image Editor

## 개요

react 환경에서 외부 editor을 이용하여 이미지를 편집하고 IPFS 서버에 업로드 하자

## Getting started

주요 툴로 TOAST-UI Image Editor을 사용

```Markdown
npm install --save @toast-ui/react-image-editor
npm install file-saver  // 파일 로컬 다운로드
npm install --save ipfs-http-client  // 파일 ipfs 업로드
```

로 설치

## IPFS(InterPlanetary File System)란?

탈중앙화 분산형 프로토콜이자,
분산 파일 시스템에서 데이터를 공유하고 저장하기 위한 peer-to-peer 네트워크
Web 3.0 시대를 여는 분산 스토리지로 데이터를 주변 사람들에게 저장하게 함

1. 특징

- 분산화 : 하나의 기관이 관리하는 것이 아닌 분산된 환경의 여러장소에서 다운로드
- 컨텐츠 어드레싱 : '어디에 위치해 있는지'가 아닌 '무엇이 있는지'를 나타내는 주소
  - 주소의 형태 : ipfs/변환된 해쉬값
- 참여 : IPFS는 적극적으로 참여할때에 잘 동작한다.
  - 보상 레이어로 '파일 코인'을 채택

2. 기대효과

- 탈중앙화 storage
- 데이터 분산 저장을 통한 안전성 및 보안 강화
- 저렴한 비용 및 빠른 속도 제공

## IPFS-HTTP-Client

ipfs-core에 merge되어 있는 부분 중에, 파일 업로드와 관리 관련 함수를 제공하는 라이브러리
기존 ipfs-api(deprecated)의 뒤를 잇는 라이브러리이다.

1. ipfs 객체 만들기. 이후, ipfs 관련 함수가 실행 가능해진다.

```Javascript
  const ipfsClient = require('ipfs-http-client')
  // ipfs-cluster-ctl로 올릴 호스트를 미리 준비해두자.
  const ipfs = ipfsClient.create({ host: '호스트 주소', port: '5001', protocol: 'http' })
```

2. 파일 업로드에 필요한 함수는 ipfs.add 뿐이다.
어떠한 형태의 data도 올릴수 있지만, 이미지의 형태로 보고 싶으면 blob의 형태로 올릴필요가 있다.

```Javascript
    try{
      const result = await ipfs.add(blob) 
      console.log("결과", result);
      console.log("주소", result.path)
    } catch(e){
      console.log("에러 : ", e)
    }
```

3. 리턴 값으로 해쉬 번호값이 온다. 해당 주소를 입력시, 이미지를 확인할 수 있다.

```Markdown
QmUwEVMbMCsW2ZJxVx2qXrvtJC6i4KVs9DCw6kgEQsVnVw
https://ipfs.io/ipfs/QmUwEVMbMCsW2ZJxVx2qXrvtJC6i4KVs9DCw6kgEQsVnVw
```

## TOAST Image Editor

NHN에서 제공하는 Fabric.js 기반 이미지 에디터

1. 에디터 자체 기능으로 flip, rotate, draw, icon, text, filter 등의 기능이 제공됨
(관련 자료 노션에 정리되어있습니다.)
2. 에디터의 캔버스를 제어하는 API가 제공됨
3. 해당 이미지를 조작하고 파일의 형태(base64)로 만드는 함수는 toDataURL();

## 트러블 슈팅

Q. 다운로드를 눌러도 다운로드 되지 않고, 새로운 blank 탭이 열림
A. 위에서 언급한 file-saver를 설치해주고,

```Javascript
const FileSaver = require('file-saver')
```

을 캔버스가 있는 컴포넌트에서 선언해주자.

Q. 팔레트(Color-picker) 모양이 깨짐
A. index.html에

```Html
    <!-- 팔레트 형태 고정 -->
    <link type="text/css" href="https://uicdn.toast.com/tui-color-picker/v2.2.3/tui-color-picker.css" rel="stylesheet">
```

를 넣어주자
