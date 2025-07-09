'''
pyinstaller --onefile flask_with_tray.py
'''
from flask import Flask
from util_tray import IconTrayApp
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask and System Tray!"

if __name__ == '__main__':
    # Windows 환경에서만 트레이 아이콘 실행
    if platform.system() == "Windows":
        tray = IconTrayApp(flask_port=5000)
        tray.start_in_thread()

    # Flask 서버 실행
    print("Starting Flask server...")
    app.run(debug=False, use_reloader=False)
