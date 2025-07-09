from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading
import ctypes
import platform
import os
import signal


class IconTrayApp:
    def __init__(self, flask_port=5000):
        self.flask_port = flask_port
        self.icon = None
        self.console_visible = True

        if platform.system() == "Windows":
            self.kernel32 = ctypes.windll.kernel32
            self.user32 = ctypes.windll.user32
            self.console_window = self.kernel32.GetConsoleWindow()
            self.SW_HIDE = 0
            self.SW_SHOW = 5
        else:
            self.kernel32 = None
            self.user32 = None
            self.console_window = None

    def show_console(self):
        """콘솔 창을 표시"""
        if self.console_window and not self.console_visible:
            self.user32.ShowWindow(self.console_window, self.SW_SHOW)
            self.console_visible = True

    def hide_console(self):
        """콘솔 창을 숨김"""
        if self.console_window and self.console_visible:
            self.user32.ShowWindow(self.console_window, self.SW_HIDE)
            self.console_visible = False

    def toggle_console(self):
        """콘솔 창의 표시/숨김 상태를 토글"""
        if self.console_visible:
            self.hide_console()
        else:
            self.show_console()

    def create_image(self, width=64, height=64, color1="blue", color2="white"):
        """트레이 아이콘 이미지 생성"""
        image = Image.new("RGB", (width, height), color1)
        draw = ImageDraw.Draw(image)
        draw.rectangle((width // 4, height // 4, 3 * width // 4, 3 * height // 4), fill=color2)
        return image

    def run_tray(self):
        """트레이 아이콘 실행"""
        def open_home(icon, item):
            """기본 브라우저에서 Flask 홈 열기"""
            import webbrowser
            webbrowser.open(f"http://127.0.0.1:{self.flask_port}/")

        def quit_app(icon, item):
            """애플리케이션 종료"""
            icon.stop()  # 트레이 아이콘 종료
            os.kill(os.getpid(), signal.SIGTERM)  # Flask 서버 종료

        # 트레이 메뉴 정의
        menu = Menu(
            MenuItem("Toggle Console", lambda icon, item: self.toggle_console()),
            MenuItem("Open Home", open_home),
            MenuItem("Quit", quit_app)
        )

        # 트레이 아이콘 생성 및 실행
        self.icon = Icon("Flask Server", self.create_image(), menu=menu)
        self.icon.run()

    def start_in_thread(self):
        """트레이 아이콘을 별도 스레드에서 실행"""
        tray_thread = threading.Thread(target=self.run_tray, daemon=True)
        tray_thread.start()
