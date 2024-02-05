'''
pip install screeninfo 후,
모니터 정보를 활용하여 두번째 작업 표시줄의 정보를 재계산해보자.

주의 싱글 모니터일 경우, 두번째 작업표시줄이 없으므로, GetWindowRect가 0을 가져온다.
'''
import win32gui
from screeninfo import get_monitors

def find_secondary_tray_window_monitor():
    def is_secondary_tray_window(hwnd):
        return win32gui.GetClassName(hwnd) == "Shell_SecondaryTrayWnd"

    for monitor in get_monitors():
        window_handle = win32gui.FindWindowEx(0, 0, "Shell_SecondaryTrayWnd", None)
        while window_handle:
            rect = win32gui.GetWindowRect(window_handle)
            if monitor.x <= rect[0] < monitor.x + monitor.width and \
                    monitor.y <= rect[1] < monitor.y + monitor.height:
                # 재계산된 좌표
                rect_in_monitor_coordinates = (rect[0] - monitor.x, rect[1] - monitor.y, rect[2] - monitor.x, rect[3] - monitor.y)
                return monitor, rect_in_monitor_coordinates
            window_handle = win32gui.FindWindowEx(0, window_handle, "Shell_SecondaryTrayWnd", None)

    return None

monitor_with_secondary_tray, rect_of_secondary_tray = find_secondary_tray_window_monitor()
if monitor_with_secondary_tray:
    print(f"Secondary Tray Window found on Monitor: {monitor_with_secondary_tray.name}")
    print(f"Rect of Secondary Tray Window in Monitor Coordinates: {rect_of_secondary_tray}")
else:
    print("Secondary Tray Window not found on any monitor.")
