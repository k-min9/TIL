# SD

- 개념, 개요를 생략하고 설정을 어떻게 하였는지 + 감상 이야기

## 240216

- 움직이는 영상 만들기
  - 기본이 되는 사진을 하나 뽑음
  - ControlNet1 : 손이 늘어나거나 왼발 오른발 나선 부분이 바뀌거나 함
    - openpose 0.8
    - ip-adapter 0.4 : 기본적으로 쓰는게 나음. 복장/얼굴의 일관성이 높아짐
  - Controlnet2 : 거의 움직이지 않거나, 심하게 깨지면서 움직임
    - depth 0.4 prompt 중시
    - ip-adapter 0.4
  - Controlnet3 : 인간의 형상이 아니거나 망가지거나...
    - canny 0.2 prompt 중시
    - ip-adapter 0.4
- 결론 : comfyui쪽을 알아보는게 나아보이는데...?
