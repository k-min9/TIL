# 베이스 이미지 선택
FROM python:3.7.16

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y cmake
COPY requirements.txt .
RUN pip install -r requirements.txt

# 소스 코드 복사
COPY . .

# 작업 디렉토리 변경하여 빌드
WORKDIR /app/monotonic_align
RUN python setup.py build_ext --inplace

# 작업 디렉토리 원래 위치로 변경
WORKDIR /app

# 컨테이너 실행 명령
CMD [ "python", "app.py" ]
