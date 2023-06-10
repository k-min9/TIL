# Flask 배포

- 개요 : 배포 두 가지를 시도 함
- 결과 : 양쪽 다 성공.

## AWS EC2 배포

1. 폴더 복사 (venv등 안 복사되게 조심)
2. sudo apt update
3. sudo apt install python3-pip
4. sudo apt-get install cmake
5. pip install -r {path}requirements.txt
6. cd 폴더/monotonic_align/
7. python3 setup.py build_ext --inplace
8. cd ..
9. sudo nohup python3 app.py &

### Tip : Swap 파일로 용량 확보

sudo fallocate -l 8G /swapfile  
sudo chmod 600 /swapfile  
sudo mkswap /swapfile  
sudo swapon /swapfile  
후 실행

## Docker 배포

1. DockerFile 작성 (파일 참조)
2. docker build -t 이미지 이름 .
   - docker build -t vits .
3. [Docker Hub](https://hub.docker.com/) 로그인
4. docker login
5. docker tag 이미지_이름 Docker_사용자명/이미지_이름:태그
   - docker tag vits mingu4969/vits:1.0
6. docker push Docker_사용자명/이미지_이름:태그
   - docker push mingu4969/vits:1.0
   - private 설정은 Docker hub에서 별도로
7. 다른 곳이나 원하는 장치에서 pull 땡기고 사용하면 끝
