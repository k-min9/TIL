# NFTicket Plus

- 대상 : <https://github.com/NFTTicketProject/NFTicket-Plus>
클론하자

- 준비물
  - AWS EC2
  - MobaXterm 내지 Linux 서버 제어 도구

- 순서
  - EC2 구매

## EC2 인스턴스 세팅

1. EC2 인스턴스 시작
2. Ubuntu Server 18.04 (LTS 버전 고름)
3. 일단 적절하게 ram 설정(4GB)
4. 키페어 pem키로 생성
5. 보안 규칙 : OpenServer
     - 포트 22, 80, 443 0.0.0.0/0으로 열리게
6. 용량은 30GB

## MobaXterm 세팅

1. 세션 생성 / 호스트 이름 : ubuntu@[퍼블릭 IPv4 DNS]
   ex) ubuntu@ec2-01-234-567-8.compute-1.amazonaws.</span>com
2. 방화벽 설정
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 8080 // showipfs 테스트용 (안 열어도 포팅에 문제 없음)
sudo ufw enable
3. 기초설정 (설정에 따라 설치 되어 있을 수 있음)
sudo apt update
sudo apt install net-tools
sudo apt install nginx
sudo apt install letsencrypt -y
sudo apt install openjdk-11-*
sudo apt -y install nodejs
sudo apt install python3-pip  // 본 프로젝트에는 필요 없긴 함
sudo apt install docker-compose -y
4. IPFS 도커 옮기기
   - IPFS 클러스터 관리 도구 다운
  
   ```Shell
   wget https://dist.ipfs.io/ipfs-cluster-ctl/v0.14.5/ipfs-cluster-ctl_v0.14.5_linux-amd64.tar.gz
   ```

   - IPFS 압축 해제
  
   ```Shell
   tar xvzf ipfs-cluster-ctl_v0.14.5_linux-amd64.tar.gz
   ```

   - IPFS 클러스터를 실행 할 docker-compose 파일 다운
  
   ```Shell
   wget https://raw.githubusercontent.com/ipfs/ipfs-cluster/master/docker-compose.yml
   ```

   - 프로젝트에 맞게 docker-compose 파일 수정
   인증 노드 수 : 3 -> 1 // 사유 : 서버 가격이요!
  
   ```Shell
   vim docker-compose.yml
   ```
  
   ```Vim
    version: '3.4'

    # This is an example docker-compose file to quickly test an IPFS Cluster
    # with multiple peers on a contained environment.

    # It runs 3 cluster peers (cluster0, cluster1...) attached to go-ipfs daemons
    # (ipfs0, ipfs1...) using the CRDT consensus component. Cluster peers
    # autodiscover themselves using mDNS on the docker internal network.
    #
    # To interact with the cluster use "ipfs-cluster-ctl" (the cluster0 API port is
    # exposed to the locahost. You can also "docker exec -ti cluster0 sh" and run
    # it from the container. "ipfs-cluster-ctl peers ls" should show all 3 peers a few
    # seconds after start.
    #
    # For persistance, a "compose" folder is created and used to store configurations
    # and states. This can be used to edit configurations in subsequent runs. It looks
    # as follows:
    #
    # compose/
    # |-- cluster0
    # |-- cluster1
    # |-- ...
    # |-- ipfs0
    # |-- ipfs1
    # |-- ...
    #
    # During the first start, default configurations are created for all peers.

    services:

    ##################################################################################
    ## Cluster PEER 0 ################################################################
    ##################################################################################

      ipfs0:
        container_name: ipfs0
        image: ipfs/go-ipfs:latest
        ports:
          - "4001:4001" # ipfs swarm - expose if needed/wanted
          - "5001:5001" # ipfs api - expose if needed/wanted
          - "8080:8080" # ipfs gateway - expose if needed/wanted
          #- "20000:8080" # ipfs gateway - expose if needed/wanted
        volumes:
          - ./compose/ipfs0:/data/ipfs

      cluster0:
        container_name: cluster0
        image: ipfs/ipfs-cluster:latest
        depends_on:
          - ipfs0
        environment:
          CLUSTER_PEERNAME: cluster0
          CLUSTER_SECRET: ${CLUSTER_SECRET} # From shell variable if set
          CLUSTER_IPFSHTTP_NODEMULTIADDRESS: /dns4/ipfs0/tcp/5001
          CLUSTER_CRDT_TRUSTEDPEERS: '*' # Trust all peers in Cluster
          CLUSTER_RESTAPI_HTTPLISTENMULTIADDRESS: /ip4/0.0.0.0/tcp/9094 # Expose API
          CLUSTER_MONITORPINGINTERVAL: 2s # Speed up peer discovery
        ports:
              # Open API port (allows ipfs-cluster-ctl usage on host)
              - "127.0.0.1:9094:9094"
              # The cluster swarm port would need  to be exposed if this container
              # was to connect to cluster peers on other hosts.
              # But this is just a testing cluster.
              # - "9095:9095" # Cluster IPFS Proxy endpoint
              # - "9096:9096" # Cluster swarm endpoint
        volumes:
          - ./compose/cluster0:/data/ipfs-cluster
   ```

   - IPFS 클러스터 docker-compose 실행
  
   ```Shell
   // 실행전 docker 그룹에 유저 포함하고, 로그인, 로그아웃
   sudo usermod -aG docker ${USER} 
   docker-compose up -d
   ```

   - 첫 실행 시, compose 폴더가 설치 되었을것임
   IPFS 클러스터 종료후 config로 CORS 설정 후 다시 실행
  
   ```Shell
   docker-compose down

   cd compose/ipfs0
   vim config

   ### config 내 첫 API 설정 이하로 변경
    "API": {
      "HTTPHeaders": {
        "Access-Control-Allow-Origin": [
          "*"
        ],
          "Access-Control-Allow-Methods": [
          "PUT", "GET", "POST"
        ]
      }
    },
   ###

   docker-compose up -d
   ```

## 배포

1. nginx 설정
cd /etc/nginx/sites-available들어가서 sudo vim default

    ```Shell
      server {
              listen 80 default_server;
              listen [::]:80 default_server;

              server_name nfticket.plus;

              return 301 https://$server_name$request_uri;
      }

      server {
              listen 443 ssl;
              listen [::]:443 ssl;

              server_name nfticket.plus;

              ssl_certificate /etc/letsencrypt/live/nfticket.plus/fullchain.pem;
              ssl_certificate_key /etc/letsencrypt/live/nfticket.plus/privkey.pem;

              root /var/www/html/build;
              index index.html;

              location / {
                      try_files $uri $uri/ /index.html;
              }

              location /api/v1 {
                      rewrite /api/v1/(.*) /$1 break;
                      proxy_pass http://localhost:8000/;
                      proxy_redirect off;
                      proxy_set_header Host $host;
              }

              location /ipfs {
                      rewrite /ipfs/(.*) /$1 break;
                      proxy_pass http://localhost:5001/;
                      proxy_redirect off;
                      proxy_set_header Host $host;
              }

              location /showipfs {
                      rewrite /showipfs/(.*) /$1 break;
                      proxy_pass http://localhost:8080;
                      proxy_redirect off;
                      proxy_set_header Host $host;
              }
      }
    ```

2. [spring back 서버]\build\libs에서 파일 옮기고

    ```Shell
      nohup java -jar nfticket-0.0.1-SNAPSHOT.jar & 로 구동
      (Python 보조 서버 Flask 등 있을 경우, nohup python3 [앱이름].py &)

      // 관련 오류 체크
      tail -n 200 nohup.out
    ```

3. 도메인 설정
호스팅 케이알 들어가서, 도메인 관리
DNS 레코드 관리에서 A 유형 이름 @, www으로
EC2에서 [curl http://</span>checkip.amazonaws.</span>com]으로 확인한 주소 넣기

4. let’s encrypt(하기 전에 nginx 켰으면 종료)

    ```Shell
    // nginx 설정 후, 기존 작동시 stop
    sudo service nginx stop
    sudo letsencrypt certonly --standalone -d nfticket.plus
    ```

5. 프론트 서버 옮기기
(yarn install 로 구동 확인 후,)
yarn build
build 파일 옮기고

    ```Shell
    sudo rm -rf /var/www/html/build/
    sudo mv build/ /var/www/html/
    ```

6. sudo service nginx start
