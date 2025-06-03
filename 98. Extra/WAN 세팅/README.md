# 개요

WAN 관련 세팅 해보자.

## 과정

0. 선행작업  
    [비주얼 스튜디오 빌드툴 설치](https://visualstudio.microsoft.com/ko/downloads/?q=build+tools) 후 cl.exe를 환경변수에 등록  
    변수 이름 : cl.exe  
    변수 값(예시) : C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.43.34808\bin\Hostx86\x64
1. 기본 comfyUI 포터블 파일 풀고 세팅
    python_3.12.7_include_libs 압축 해제 후 include와 libs 폴더를 python_embedded 안에 복사
    run_gpu.bat에 --fast --use-sage-attention 붙이기
2. 프로그램 켜서 torch, cuda 버전 확인 : 2.7.0+cu128
3. custom_nodes의 ComfyUI-Manager 복사 내지 추가
기존 models 복사
4. [SageAttention을 위한 triton 설치](https://arca.live/b/aiart/134569090?target=all&keyword=sageattention&p=1)  

    ```bash
    ./python.exe -m pip install -U triton-windows  
    git clone `https://github.com/thu-ml/SageAttention.git`  
    ./python.exe -s -m pip install -e SageAttention  
    ```

5. Profit 구동!
