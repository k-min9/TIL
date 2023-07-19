@echo off
chcp 65001 > nul
REM 한글 설정임

set /p input_string=ID를 입력해주세요 : 

git config --global user.name "%input_string%"
git config --global user.email "%input_string%@kbinsure.co.kr"
git config --global core.autocrlf true
git config --global core.filemode false

echo Git 설정 완료
pause