# Kafka

Messaging Channels, Streaming & messaging 담당
이것만으로도 하나의 강좌가 나올 정도로 방대하므로 주의!

- 참조 링크 모음
  - Kafka 홈페이지 : <http://kafka.apache.org>
  - Kafka와 데이터를 주고받기 위해 사용하는 Java Library : <https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients>

## 개요

Apache Software Foundation의 Scalar 언어로 된 오픈 소스 메시지 브로커 프로젝트
LinkedIn에서 개발 → 오픈소스화 → Apache 재단에서 관리

- 특징
  - 높은 처리량, 낮은 지연 시간, 안정성이 좋음
  - 모든 시스템으로 데이터를 실시간으로 전송하여 처리할 수 있는 시스템
  - 데이터가 많아져도 확장(스케일 아웃)이 용이
- 데이터 동기화 문제 : 데이터를 분산 저장해서 생기는 문제
  - 해결법
    - 하나의 DB 사용
    - DB 간 동기화
    - Kafka Connector + DB 단일화 << KAFKA식 해결법!

## Notation

- 메시지 브로커 : 특정한 서비스에서 다른 서비스로 메세지를 전달하는 서버
  - 이후 kafka 어플리케이션 서버를 브로커로 호칭
  - 3대 이상 권장의 Broker Cluster 구성 (1대는 Controller(리더) 기능)
- Zookeeper : 브로커 관리자

## Kafka Connect

- Kafka Connect를 통해 Data를 Import/Export 가능
- 코드 없이 Configuration으로 데이터를 이동
- Standalone mode, Distribution mode 지원
  - REST API를 통해 지원
  - Stream 또는 Batch 형태로 데이터 전송 가능
  - 커스텀 Connector을 통한 다양한 Plugin 제공
- 기존 DB에서 가져오는 쪽 : connect source / 새로운 DB로 보내는 쪽 connect sink

## 실제 작업

1. Kafka 홈페이지에서 다운로드 다운
2. 다운 받고 열면 자주 쓰이는건 bin(실행), config(설정) 폴더

실행

```cmd
# 포트 번호
zookeeper : 2181
kafka server : 9092
kafka connector : 8083

# 실행 순서 : zookeeper -> server -> connect
nohup sudo sh kafka/bin/zookeeper-server-start.sh  kafka/config/zookeeper.properties &
nohup sudo sh kafka/bin/kafka-server-start.sh kafka/config/server.properties &
nohup sudo sh kafka-connect-7.1.0/bin/connect-distributed kafka-connect-7.1.0/etc/kafka/connect-distributed.properties &

# 토픽 확인
sudo sh KAFKA/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

## 기타

일반 세팅

```vim
Zookeeper 및 Kafka 서버 기동 (순서 주의)
$KAFKA_HOME/bin/zookeeper-server-start.sh  $KAFKA_HOME/config/zookeeper.properties
$KAFKA_HOME/bin/kafka-server-start.sh  $KAFKA_HOME/config/server.properties

Topic 생성
$KAFKA_HOME/bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092 \

--partitions 1

Topic 목록 확인
$KAFKA_HOME/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

Topic 정보 확인
$KAFKA_HOME/bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092

Windows에서 기동
- 모든 명령어는 $KAFKA_HOME\bin\windows 폴더에 저장
- .\bin\windows\zookeeper-server-start.bat  .\config\zookeeper.properties

메시지 생산
$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic quickstart-events

메시지 소비
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic quickstart-events \

 --from-beginning

Kafka Connect 설치
curl -O http://packages.confluent.io/archive/7.1/confluent-community-7.1.0.tar.gz

tar xvf confluent-community-7.1.0.tar.gz

cd  $KAFKA_CONNECT_HOME

Kafka Connect 실행
bin/connect-distributed etc/kafka/connect-distributed.properties
.\bin\windows\connect-distributed.bat .\etc\kafka\connect-distributed.properties

JDBC Connector 설치
- https://docs.confluent.io/5.5.1/connect/kafka-connect-jdbc/index.html

- confluentinc-kafka-connect-jdbc-10.0.1.zip 

etc/kafka/connect-distributed.properties 파일 마지막에 아래 plugin 정보 추가
- plugin.path=[confluentinc-kafka-connect-jdbc-10.0.1 폴더]

JdbcSourceConnector에서 MariaDB 사용하기 위해 mariadb 드라이버 복사
./share/java/kafka/ 폴더에 mariadb-java-client-2.7.2.jar  파일 복사
```

gradle 이용 자바 세팅

```vim
./gradlew bootRun --args='--server.port=8888'

mvn compile package => ./gradlew build

java -D"server.port"=9004 -jar ./build/libs/user-service-0.0.1-SNAPSHOT.jar

mariadb-java-client GRADLE 사용시 위치

홈디렉토리\.gradle\caches\modules-2\files-2.1\org.mariadb.jdbc\mariadb-java-client\버전

kafka connect 윈도우에서 connect-distributed 수정해야함( log4j 오류날때 )
rem Log4j settings
IF ["%KAFKA_LOG4J_OPTS%"] EQU [""] (
  set KAFKA_LOG4J_OPTS=-Dlog4j.configuration=file:%BASE_DIR%/etc/kafka/connect-log4j.properties
)
```

예제

```vim

1) 주키퍼를 실행
명령어 : zookeeper-server-start.bat ../../config/zookeeper.properties

2) 카프카를 실행
명령어 : kafka-server-start.bat ../../config/server.properties

3) 토픽 생성 << --zookeeper 옵션 작동 안하거나 필요 없을 수 있음
명령어 : kafka-topics.bat --zookeeper localhost:2181 --topic test --create --partitions 1 --replication-factor 1

4) 토픽 리스트 확인 << --zookeeper 옵션 작동 안하거나 필요 없을 수 있음
kafka-topics.bat --zookeeper localhost:2181 --list  
kafka-topics.bat --bootstrap-server localhost:9092 --list

5) 컨슈머 생성

kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test

6) 프로듀서 생성 및 메시지 보내기

kafka-console-producer.bat --broker-list localhost:9092 --topic test
```
