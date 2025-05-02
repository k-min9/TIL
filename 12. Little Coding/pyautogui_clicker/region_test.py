# script.py에서 메인모니터(1280X720)에 인식되는 범위를 확인하기 위한 Test코드
import pyautogui

pyautogui.screenshot(
    imageFilename="img/region_test.png",
    region=[350,280,620,570]
)
