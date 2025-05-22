'''
2. Esc를 듣는 중에만 사용하는 Manual 모드
pip install keyboard
'''
# C:\Users\M9\.cache\whisper 에 pt 확인
import speech_recognition as sr
import keyboard
import threading

key = ''

def get_pressed_key():
    global key
    print("키를 입력하세요...")
    key = keyboard.read_event(suppress=True).name
    print(key)
    return key

def recognize_speech():
    global key
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        while not exit_signal.is_set():  # 스레드가 종료되지 않은 동안 반복
            # if keyboard.is_pressed("ctrl+space"):  # ctrl+space가 눌렸을 때
            if keyboard.is_pressed(key):  # ctrl+space가 눌렸을 때
                print("말하세요...")
                audio = recognizer.listen(source)

                try:
                    print("음성을 텍스트로 변환 중...")
                    text = recognizer.recognize_whisper(audio, language="ja")
                    print("인식된 텍스트: {}".format(text))
                except sr.UnknownValueError:
                    print("음성을 인식할 수 없습니다.")
                except sr.RequestError as e:
                    print("Google API 요청에 실패했습니다. 에러: {}".format(e))

if __name__ == "__main__":
    get_pressed_key()
    # 시작
    exit_signal = threading.Event()

    # 음성 인식 스레드 시작
    speech_thread = threading.Thread(target=recognize_speech)
    speech_thread.start()

    try:
        # 프로그램이 종료될 때까지 대기
        keyboard.wait("esc")
    except KeyboardInterrupt:
        pass
    finally:
        # 프로그램이 종료되면 음성 인식 스레드 종료
        exit_signal.set()
        speech_thread.join()
