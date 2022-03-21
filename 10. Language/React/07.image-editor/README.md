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