# VITS(Vision-Infused Text-to-Speech) on Windows

- 개요 : 음성 합성 기술, 텍스트를 입력으로 받아들여 해당 텍스트를 읽는 자연음성을 생성
- 단계
  - 데이터 수집
  - 음성 데이터 전처리
  - 모델 학습
  - 음성 학습

참고할 오픈소스 프로젝트 :  
<https://github.com/MasayaKawamura/MB-iSTFT-VITS>
<https://github.com/misakiudon/MB-iSTFT-VITS-multilingual>

## 용어

- DDSP(Differentiable Digital Signal Processing) : 오디오 처리를 위한 딥러닝 프레임워크
- SVC(Support Vector Classification) : 지원 벡터 머신. 지도학습분류 알고리즘
- Diff-Svc(Diffusion Singing Voice Conversion) : 확산(Diffusion) 모델을 활용한 노래 음성 변환 기술
- MB-iSTFT-VITS : 멀티밴드-역단기푸리에변환을 활용한 신호 합성으로 경량화된 엔드 투 엔드 텍스트 음성 변환 모델
- CUDA : 이걸를 지원하는 pytorch 설치
- GPU 통신 라이브러리 : 분산 학습과 데이터 병렬 처리를 위해 사용. Windows 공식 지원이 없음!
  - NCCL(NVIDIA Collective Communication Library) : 널리 알려져있지만 linux 환경에서만 사용 가능
  - Gloo : Windows 환경에서 PyTorch의 분산학습환경을 조성

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
        pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html --linux
        pip install torch torchvision

        // 기타 버전 맞추기
        pip install protobuf==3.20.*
        ```

        등의 명령어를 받아와야한다.
  6. espeak 설치 : 문자열을 음성으로 변조시키는 프로그램. cleaned 전처리에 필요
      - <https://espeak.sourceforge.io/download.html>에서 설치
      - 제어판>시스템>고급시스템설정>환경변수>시스템변수>Path를 Edit>espeak.exe가 되게 설치파일 링크
      - 재부팅
  7. 기타 Path 설정
      - cmake : D:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin
  8. monotonic_align 빌드  

      ``` shell
      -- venv 켜져있는 상태로 해야 현재 파이썬 버전에 맞는 코어가 생김
      cd monotonic_align
      mkdir monotonic_align
      python setup.py build_ext --inplace
      cd ..
      ```

  9. 음성 변조, 컨버팅 필요한지 확인

      ```shell
      python convert_to_22050.py --in_path audio_converter_input/ --out_path audio_converter_output/
      ```

  10. 데이터셋 만들기 : filelists/ljs_audio_text_train_filelist.txt 및 3종 작성
      - wav 파일 등 정해진 확장명 파일만 취급
      - train : val : test = 70% : 25% : 5% 예정
      - audio_to_text.py로 audio_converter_output를 바로 txt화 할 수 있음 : python audio_to_text.py
  11. 전처리 : 데이터셋 txt 파일을 cleaned 파일로 변경.
  예시>

      ```shell
      // argument 기본값 해둬서 그냥 파일명만 입력만 해도 됨, argument 변경 또는 추가시 입력
      python preprocess.py   
      python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_train_filelist.txt
      python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_val_filelist.txt
      python preprocess.py --text_index 1 --filelists filelists/ljs_audio_text_test_filelist.txt

      -- text_cleaners 'korean_cleaners'로 특정 클리너 지정할 수도 있음.
      python preprocess.py --text_index 1 --filelists filelists/filelist_train.txt filelists/filelist_val.txt --text_cleaners 'japanese_cleaners'
      ```

  12. 학습 : python train_latest.py -c <config> -m <folder>
      - 예시 : python train_latest.py -c configs/ljs_mb_istft_vits.json -m ljs_mb_istft_vits
  13. 출력 : log에 생성된 G_0.pth를 활용

## Audio To Text

- 개요 : wav 파일을 언제 하나하나 입력하고 타이핑하겠습니까. 외부 서비스 쓰면 되지
- Google Cloud Speech API를 사용하여 wav파일을 텍스트로 바꾸고 txt 파일로 정리하자
- 사용법
  1. GCP에서 Speech-To-Text API/서비스를 사용하자
  2. 사용자인증정보에서 해당 서비스계정을 만들자
  3. 서비스계정>키>키 추가로 json파일을 받고 credential.json 등 python이 인식할 수 있는 형태로 두자
  4. audio_to_text.py를 작성하고 sample_rate_hertz 헤르쯔와 language_code를 설정하자
  5. 필요하면 pip install pip install google-cloud-speech 하고 사용
  6. 한달 무료는 60분까지. 이후 분당 0.024 달러 약 한시간당 2천원의 사용료가 지불된다 조심!

## 기타

- pytorch.org에서 현재 자신이 사용하는 GPU와 cuda가 버전이 연동되는지 확인하고 설치해야한다.
  - 사용 : pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
- windows는 NCCL을 지원하지 않기 때문에 문제가 발생. gloo를 써야한다.
  - 환경변수를 PL_TORCH_DISTRIBUTED_BACKEND=gloo로 설정하거나
  - dist.init_process_group(backend='nccl'...)의 nccl을 전부 gloo로 바꿔서 해결할 수 있음
- [RuntimeError: CUDA out of memory]발생시 캐시나 gc를 청소해보고 그래도 안되면 batch 수를 줄여보자.
- 도움이 되는 한 줄 파이썬 체크

    ```shell
    python -c "import torch, gc; gc.collect(); torch.cuda.empty_cache();"  -- cuda memory 확보를 위한 캐쉬, gc 청소

    -- cuda 설정 확인 관련
    python -m torch.utils.collect_env
    python -c "import torch; print(torch.cuda.is_available())"    -- cuda와 pytorch 연동 확인
    python -c "import torch; print(torch.backends.cudnn.enabled)"
    python -c "import torch; print(torch.cuda.nccl.is_available(torch.randn(1).cuda()))"  -- nccl은 리눅스만 지원
    python -c "import torch; print(torch.cuda.nccl.version())"
    ```
