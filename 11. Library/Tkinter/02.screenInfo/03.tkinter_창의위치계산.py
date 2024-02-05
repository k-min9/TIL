'''
tkinter 창의 현재 모니터 위치와 재계산
이제 양 모니터의 윈도우창 정보와 tkinter의 창 정보를 알고 있으니 같은 함수로 계산할 수 있다.
땡큐 screeninfo!
'''
import tkinter as tk
from screeninfo import get_monitors

def get_current_monitor_info(window):
    monitors = get_monitors()
    for monitor in monitors:
        if (monitor.x <= window.winfo_x() < monitor.x + monitor.width) and \
           (monitor.y <= window.winfo_y() < monitor.y + monitor.height):
            return monitor

    # 만약 어떤 모니터에도 속해있지 않으면 None 반환
    return None

def update_info_periodically(window):
    current_monitor = get_current_monitor_info(window)
    if current_monitor:
        # 모니터 상대적인 위치 계산
        relative_x = window.winfo_x() - current_monitor.x
        relative_y = window.winfo_y() - current_monitor.y

        print(f"현재 창은 {current_monitor.name} 모니터에 속해있습니다.")
        print(f"{current_monitor.name} 모니터의 가로 길이: {current_monitor.width}")
        print(f"{current_monitor.name} 모니터의 세로 길이: {current_monitor.height}")
        print(f"현재 창의 위치 (모니터 상대적인 위치): x={relative_x}, y={relative_y}")
        print("\n")

    window.after(100, lambda: update_info_periodically(window))  # 0.1초마다 호출

# tkinter 윈도우 생성
root = tk.Tk()

# 윈도우 크기 설정
root.geometry("300x200")

# 주기적으로 창 정보 업데이트
update_info_periodically(root)

# tkinter 이벤트 루프 실행
root.mainloop()
