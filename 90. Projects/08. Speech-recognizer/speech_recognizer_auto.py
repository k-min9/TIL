'''
1. 자동 인식 기능 모드

pip install SpeechRecognition
pip install PyAudio
pip install git+https://github.com/openai/whisper.git soundfile
= 여기까지 1.2GB

pip install pyinstaller
pyinstaller main.py --onefile // --noconsole
'''
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("말하세요...")
        audio = recognizer.listen(source)

    try:
        print("음성을 텍스트로 변환 중...")
        text = recognizer.recognize_whisper(audio, language="en")  # 여기서 'whisper'를 사용
        # text = recognizer.recognize_whisper(audio, language="ja")  # 여기서 'whisper'를 사용
        # text = recognizer.recognize_whisper(audio, language="en")  # 여기서 'whisper'를 사용
        print("인식된 텍스트: {}".format(text))
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print("음성 인식 엔진에 오류가 발생했습니다. 에러: {}".format(e))

if __name__ == "__main__":
    while True:
        recognize_speech()
