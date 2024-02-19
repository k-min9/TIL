import subprocess

# main.exe 경로 설정
main_exe_path = "./main.exe"

# subprocess.Popen을 사용하여 main.exe를 관리자 권한으로 실행
subprocess.Popen([main_exe_path, "/user:Administrator"])