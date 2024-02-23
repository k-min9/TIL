
# Animate anyone

- 개요 : 사진 한장과 영상 하나로 애니메이션을 만들어보자.
  - 512*768을 base로 영상을 pose 영상으로 만들고, 사진을 입힘
  - 출처 : <https://humanaigc.github.io/animate-anyone/>
    - paper만 보고 구현한 프로젝트 : <https://github.com/MooreThreads/Moore-AnimateAnyone>
- 설치 : cuda 필수
  - pip -r requirements.txt
  - pip install torch==2.0.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
- 순서
  1. 영상 -> pose로 : vid2pose를 밖으로 뺐음
      - python vid2pose.py --video_path ./videos/walk_left.mp4
  2. animation.yaml에 test_cases 변경
  3. 사진 -> 영상으로
      - python -m scripts.pose2vid --config ./configs/prompts/animation.yaml -W 512 -H 784 -L 64

## 감상

- 갈길이 멀어보인다...