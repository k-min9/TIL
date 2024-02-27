'''
var을 선언하여 int만 작성 가능하게 만들었음
'''
import tkinter as tk

def on_entry_change(*args):
    # Entry 값이 변경될 때 호출되는 콜백 함수
    try:
        int(int_var.get())
    except:
        # 변환에 성공하면 IntVar에 반영
        int_var.set(42)

root = tk.Tk()

# IntVar를 생성하고 초기값을 정수로 지정합니다.
int_var = tk.IntVar(value=42)

# Entry 위젯을 생성하고 IntVar와 연결합니다.
entry_widget = tk.Entry(root, textvariable=int_var)
entry_widget.pack()

# Entry 값이 변경될 때 호출될 콜백 함수를 연결합니다.
int_var.trace_add("write", on_entry_change)

root.mainloop()

