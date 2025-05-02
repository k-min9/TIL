'''
메인모니터(1280X720)에 인식되는 눈모양('eye.png')을 클릭하게 하는 코드
두더지 잡기 등에 활용

1. 스크립트 실행
2. F8로 Toggle

pip install opencv-python (잘 안될경우 pip install opencv-python==4.5.5.64)
pip install pyscreeze==0.1.29
pip install pyautogui keyboard
'''

import pyautogui
import keyboard

running, isHolding = True, True
startStopKey = "f8"

print("Starting Moler@1.0.0")
print(f"{startStopKey} - Start / Stop")
print("-" * 20)
print("🟩 Running" if running else "🛑 Stopped")

while True:
    if keyboard.is_pressed(startStopKey) == True:
        if isHolding == False:
            isHolding = True
            print ("\033[A                             \033[A")
            print("🛑 Stopped" if running else "🟩 Running")
            running = not running
    else:
        isHolding = False

    if running:
        location = pyautogui.locateOnScreen(
            image="img/eye.png",
            confidence=0.8,
            region=[350,280,620,570]
        )

        if location:
            pyautogui.click(location)