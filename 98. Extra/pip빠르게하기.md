# PIP 빠르게 하기

- 배경 : micro 단위의 서버를 빌릴때, pip가 매우 느린 문제가 발생한다.
- 해결 : 미러서버를 사용하자

1. sudo mkdir ~/.pip
2. sudo vi ~/.pip/pip.conf
3. 아래와 같이 작성하고 저장

    ```vim
    [global]
    index-url=http://ftp.daumkakao.com/pypi/simple
    trusted-host=ftp.daumkakao.com
    ```

4. pip install 패키지명 등으로 pip 이용!
