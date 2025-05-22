@echo off
setlocal enabledelayedexpansion

REM 현재 날짜 및 시간을 가져오기
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set datetime=%%a
set year=!datetime:~0,4!
set month=!datetime:~4,2!
set day=!datetime:~6,2!
set hour=!datetime:~8,2!
set minute=!datetime:~10,2!
set second=!datetime:~12,2!

REM 로그 파일 이름 생성
set logFile=log_!year!!month!!day!_!hour!!minute!!second!.txt

REM main.exe 실행 및 로그 기록
main.exe >> %logFile% 2>&1

echo 로그가 %logFile% 파일에 저장되었습니다.
pause
