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

- 세팅
  1. git clone
  2. 클론 폴더에서 venv 설정 : python -m venv venv
  3. venv 사용 : source venv/Scripts/activate
  4. python 버전 설정 : virtualenv venv --python=3.6.7
      - 설치는 별도로 되어있어야 함
  5. 라이브러리 설치 : pip install -r requirements.txt
      - torch, torchvision을 리눅스가 아닌 윈도우 환경에서 설치하기 위해서는 <https://pytorch.org>에 직접 방문해서  

        ``` shell
        pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
        ```

        등의 명령어를 받아와야한다.
  6. espeak 설치 : 문자열을 음성으로 변조시키는 프로그램. cleaned 전처리에 필요
      - <https://espeak.sourceforge.io/download.html>에서 설치
      - 제어판>시스템>고급시스템설정>환경변수>시스템변수>Path를 Edit>espeak.exe가 되게 설치파일 링크
      - 재부팅
  7. 데이터셋 만들기 : filelists/ljs_audio_text_train_filelist.txt 및 3종 작성
      - |
  8. 전처리 : 데이터셋 txt 파일을 cleaned 파일로 변경.
  예시>

      ```shell
      python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_train_filelist.txt
      python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_val_filelist.txt
      python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_test_filelist.txt

      --text_cleaners 'korean_cleaners'로 특정 클리너 지정할 수도 있음.
      ```

  9. 학습 : python train_latest.py -c configs/ljs_mb_istft_vits.json -m ljs_mb_istft_vits
