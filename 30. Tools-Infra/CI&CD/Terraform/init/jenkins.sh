#!/bin/bash
# install wget && unzip && git

yum install -y wget
yum install -y unzip
yum install -y git

mkdir -p /var/lib/jenkins
touch /var/lib/jenkins/metadata_script.log
echo "작업중... 대기해주세요" >> /var/lib/jenkins/metadata_script.log

# jenkins repo
wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

echo "nameserver 8.8.8.8" >> /etc/resolv.conf

# install dependencies
yum install -y python3 java-11-openjdk-devel.x86_64
yum install -y jenkins

# install pip
wget -q https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm -f get-pip.py

# install terraform
...

# install war file
...

# install docker community edition + kubectl
...

echo "메타데이터 작업종료" >> /var/lib/jenkins/metadata_script.log

# practice env
sudo mkdir /practice
cd /practice
sudo git clone [깃주소].git

sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
adduser m9
chown -R m9:m9 /practice


### Terraform 작업 시작하기 전에 세팅을 하기 위한 코드

