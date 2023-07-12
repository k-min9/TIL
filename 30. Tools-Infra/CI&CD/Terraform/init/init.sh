#!/bin/hash        # << 스크립트 파일을 실행할 때 어떤 인터프리터를 사용해야 하는지를 지정

adduser m9  # "m9" 사용자를 추가합니다.
usermod -aG docker m9  # "m9" 사용자를 "docker" 그룹에 추가합니다.

cd /practie  # "/practie" 디렉토리로 이동합니다.
sudo git clone [git주소].git  # 지정된 git 주소로부터 클론하여 소스 코드를 가져옵니다.

chown -R m9:m9 /practice  # "/practice" 디렉토리와 그 하위 모든 파일 및 디렉토리의 소유자와 그룹을 "m9"로 변경합니다.
chown -R m9:m9 /practice -*  # "/practice" 디렉토리 내의 파일 이름이 "-"로 시작하는 모든 파일의 소유자와 그룹을 "m9"로 변경합니다.

systemctl start jenkins  # Jenkins 서비스를 시작합니다.
