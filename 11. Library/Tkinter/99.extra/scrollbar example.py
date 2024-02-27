import tkinter as tk
from tkinter import ttk

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Frame Example")

# 스크롤바가 있는 캔버스 생성
canvas = tk.Canvas(root, width=100, height=100, bg='yellow')
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# 내용 추가
for i in range(50):
    ttk.Label(scrollable_frame, text=f"Label {i}").pack()

# 스크롤바와 캔버스 배치
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# 프레임 크기 변경 시 스크롤범위 설정
scrollable_frame.bind("<Configure>", on_frame_configure)

root.mainloop()
