'''
a.py를 기동해보자.
'''
import tkinter as tk
import subprocess

def run_a_py():
    input_str = input_entry.get()
    try:
        output = subprocess.check_output(["python", "a.py"], input=input_str, text=True)
        result_label.config(text=output)
    except subprocess.CalledProcessError as e:
        result_label.config(text="Error: " + str(e))

# Tkinter 창 생성
app = tk.Tk()
app.title("My Program")

# 입력을 받을 텍스트 상자 생성
input_entry = tk.Entry(app)
input_entry.pack()

# 버튼 생성
run_a_button = tk.Button(app, text="Run a.py", command=run_a_py)
run_a_button.pack()

# 결과 출력을 위한 Label 생성
result_label = tk.Label(app, text="", wraplength=300)
result_label.pack()

# Tkinter 이벤트 루프 시작
app.mainloop()
