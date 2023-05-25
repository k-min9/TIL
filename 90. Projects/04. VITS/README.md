# VITS(Vision-Infused Text-to-Speech)

- 개요 : 음성 합성 기술, 텍스트를 입력으로 받아들여 해당 텍스트를 읽는 자연음성을 생성
- 단계
  - 데이터 수집
  - 음성 데이터 전처리
  - 모델 학습
  - 음성 학습

참고할 오픈소스 프로젝트 : <https://github.com/MasayaKawamura/MB-iSTFT-VITS>

## 용어

- DDSP(Differentiable Digital Signal Processing) : 오디오 처리를 위한 딥러닝 프레임워크
- SVC(Support Vector Classification) : 지원 벡터 머신. 지도학습분류 알고리즘
- Diff-Svc(Diffusion Singing Voice Conversion) : 확산(Diffusion) 모델을 활용한 노래 음성 변환 기술
- MB-iSTFT-VITS : 멀티밴드-역단기푸리에변환을 활용한 신호 합성으로 경량화된 엔드 투 엔드 텍스트 음성 변환 모델

## 과정

- 현재 체크
  - 데이터셋 만들기 : filelists/ljs_audio_text_train_filelist.txt 및 3종 작성
  - 전처리 : 데이터셋 txt 파일을 cleaned 파일로 변경. python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_train_filelist.txt
    - --text_cleaners 'korean_cleaners'로 특정 클리너 지정할 수도 있음.
