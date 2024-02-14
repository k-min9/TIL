'''
심화 : 별개의 thread를 만들고 run_detached가 아닌 run을 쓰고,
거기에서 종료하는 방법으로 기능은 유지하되,
mac 이라던가 추가 설정이 필요 없다는 장점을 추가해보았다.
'''
import tkinter as tk
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

def on_tray_icon_click():
    tray_icon.stop()
    root.quit()

def action():
    print('1')

def action2():
    print('2')

# Tkinter 창 생성
root = tk.Tk()
root.title("System Tray Example")

# Tkinter 창 숨기기
root.iconify()

# System Tray 아이콘 생성
image = Image.open("./assets/png/input2.png")  # Replace with the path to your icon image
draw = ImageDraw.Draw(image)
menu_items = (item('Menu Item 1',  action),
              item('Menu Item 2', action2),
              item('Quit', on_tray_icon_click))
tray_icon = pystray.Icon("tray_icon", image, menu=menu_items)
tray_icon.run_detached()  # tkinter mainloop와 함께 돌아야 함

# Tkinter
root.wm_attributes('-topmost', True)
root.protocol('WM_DELETE_WINDOW', on_tray_icon_click)
root.mainloop()
