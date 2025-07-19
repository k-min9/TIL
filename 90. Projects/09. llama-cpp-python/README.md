# Test

## 환경

py -3.9 -m venv venv

pip install llama-cpp-python \
  --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
pip install pyinstaller

pyinstaller high_level_api_inference.py --onefile

## 트러블슈팅

- pyinstaller 이슈
  - _base_path = pathlib.Path(os.path.abspath(os.path.dirname(__file__))) 변경해야함
    - _base_path = pathlib.Path(os.path.abspath('.')) 하고, 맨 위에 llama.dll 두게 설정
