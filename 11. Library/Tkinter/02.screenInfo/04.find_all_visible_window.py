'''
다른 창과 interact 하고 싶으면 현재 활성화 된 모든 window의 정보가 필요하다.
screeninfo로 모든 visible_window를 가져온다음에 uwp와 백그라운드앱(모니터 꽉 참)을 제거하면 표시 순서대로 나온다.
'''

import win32gui
from screeninfo import get_monitors

def get_current_monitor(window):
    monitors = get_monitors()
    for monitor in monitors:
        if (monitor.x <= window[1][0] < monitor.x + monitor.width) and \
           (monitor.y <= window[1][1] < monitor.y + monitor.height):
            return monitor
    return None

def is_uwp_app(class_name):
    # 판단하려는 UWP 앱 클래스 이름을 여기에 추가
    uwp_app_class_names = ["Windows.UI.Core.CoreWindow"]#, "ApplicationFrameWindow"]
    return class_name in uwp_app_class_names

def get_visible_windows():
    windows = []
    def enum_windows_callback(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):   
            window_rect = win32gui.GetWindowRect(hwnd)
            window_name = win32gui.GetWindowText(hwnd)
            window_class = win32gui.GetClassName(hwnd)
            window_hwnd = hwnd
            if window_name and window_rect and window_class:
                windows.append((window_name, window_rect, window_class, window_hwnd))
        return True

    win32gui.EnumWindows(enum_windows_callback, None)
    return windows

def find_windows_on_monitors():
    windows_on_monitors = []
    visible_windows = get_visible_windows()
    uwp_app_set = set()

    z_order = 0
    for window in visible_windows:
        monitor = get_current_monitor(window)
        if monitor is not None and window[1] != (monitor.x, monitor.y, monitor.width, monitor.height):
            if is_uwp_app(window[2]):
                uwp_app_set.add(window[0])

            z_order += 1
            windows_on_monitors.append({"name": window[0], "rect": window[1], "class": window[2], "monitor": monitor.name, "z_order": z_order})

    print(uwp_app_set)
    windows_on_monitors_filter = list()
    for window in windows_on_monitors:
        if not (window['name'] in uwp_app_set):
            windows_on_monitors_filter.append(window)

    return windows_on_monitors_filter

if __name__ == "__main__":
    windows_on_monitors = find_windows_on_monitors()

    for window in windows_on_monitors:
        print(f"Name: {window['name']}, Rect: {window['rect']}, class: {window['class']}, Monitor: {window['monitor']}, Order: {window['z_order']}")
