# Flyway

- DB의 형상관리 툴
- 명명 규칙
  - prefix
    - V : 버전 migrate
    - U : 실행취소
    - R : 반복가능한 migration
  - Seperator : '_' 2개! 1개 아님 주의!
  - Description : 실질적 파일명. 밑줄이나 공백으로 단어 구분
  - Suffix : 접미사는 보통 .sql
- flyway.conf
  
  ```flyway
    flyway.url=jdbc:sqlite:demo.sqlite3
    flyway.location=filesystem:scripts
    flyway.user=user
    flyway.password=password
  ```

- 예시
  1. vi V1.1.1__create_group_table.sql로 테이블 생성

      ```sql
      CREATE TABLE groups(
        group_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
      )
      ```

  2. vi V1.1.2__insert_group_table.sql로 테이블 변경

      ```sql
      INSERT INTO groups (group_id, name) VALUES (1, 'GM');
      ```

  3. flyway -configFiles=="flayway.conf"로 migrate로 내용 반영
  4. flyway -configFiles=="flayway.conf"로 info로 확인 가능
  5. 결과물 : sqlite3 demo.sqlite3 > .tables로 확인 가능
