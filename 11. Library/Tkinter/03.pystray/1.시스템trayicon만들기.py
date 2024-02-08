'''
pystray를 통해 시스템 트레이 아이콘을 만들 수 있음
tkinter과 같이 써야 하기 때문에 run이 아니라 run_detached를 써야 함.

pip install pystray
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
