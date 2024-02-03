'''
같은 작업표시줄이지만 애초에 모니터에 따라 좌표도 다르고, 
각각의 클래스명도 다르다. 우선 찾아보자.
작동 후 > 음수 좌표가 발견된다. 이래서야 쓰기 힘들다. : 모니터에 대한 정보를 screeninfo 라이브러리로 쉽게 접근할 수 있다.
'''
import win32gui
import re

def enum_handler(hwnd, lParam):
    # Get the class name and window rect of the current window
    class_name = win32gui.GetClassName(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    
    # Check if the class name matches the pattern
    if re.match(r'^Shell_(Secondary)?TrayWnd$', class_name):
        # Print or process the information as needed
        print(f"Class Name: {class_name}, Handle: {hwnd}, Rect: {rect}")

    return True

# Enumerate all top-level windows
win32gui.EnumWindows(enum_handler, None)
