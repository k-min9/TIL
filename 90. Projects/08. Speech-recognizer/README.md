# Speech Recognizer

- 개요 : whisper을 기반으로 음성인식을 구현해보자.
- 방식
  - 계속 듣는 Auto 모드
  - 특정 키보드를 입력하는 Manual 모드
- 라이브러리
  - SpeechRecognition, PyAudio, soundfile (+keyboard)
  - 버전은 requirements.txt, 설치는 각각의 py 참조

## venv 변경내역

whisper/audio.py
filters_path = os.path.join(os.path.dirname(__file__), "assets", "mel_filters.npz")를
filters_path = os.path.join('./assets/mel_filters.npz') 로 변경

whisper/tokenizer.py
vocab_path = os.path.join(os.path.dirname(__file__), "assets", f"{name}.tiktoken")
vocab_path = f"./assets./{name}.tiktoken"

whisper/__init__.py 128~142 비활성화 하고 옮겨서 이렇게 해도 됨. name이 base임
checkpoint_file = './assets/base.pt'
alignment_heads = _ALIGNMENT_HEADS[name]