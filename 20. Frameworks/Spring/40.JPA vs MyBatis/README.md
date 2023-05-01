# JPA vs Mybatis

단순한 같은 프로그램을 각각의 기술로 구현해보고, 차이를 확인해보자.

- 환경세팅
  - IDE : VS code
    - Extension pack for java
    - Spring Boot Extension Pack
    - Lombok Annotatinos Support for VS Code
    - Vetur
    - Live Server
    - Thunder Client

## JPA

1. application.properties 구성
   - spring.datasource.url=jdbc:mariadb://localhost:3306/show                        ; JPA는 DB 스키마 이름 적어야 함
   - spring.jpa.properties.hibernate.dialect: org.hibernate.dialect.MySQL8Dialect    ; JPA는 필수로 적어줘야 함
2. Entity 구성
   - class 위에 @Entity @Table(name="t_user") @Getter @Setter @NoargsConstructor      ; Entity는 @Data 사용시 toString 무한루프 발생
   - @Id @Column(name="USER_NO") String userNo;                                      ; 언더바(_)없이 카멜케이스로
3. DTO 구성
   - class 위에 @Data @NoargsConstructor                                              ; DTO는 바로 @Data 사용해버리기
4. Service(Impl) 작성
5. Controller 작성

## Mybatis

1. application.properties 구성
   - spring.datasource.url=jdbc:mariadb://localhost:3306                             ; DB 스키마 적으면 안 됨!
2. DTO 구성
3. 해당 DTO내지 그 리스트를 반환하는 mapper interface 작성
4. main>resources>mapper에 해당 mapper class이름을 namespace로 가지는 xml 파일 작성
   - id(함수이름), parameterType, resultType
5. Service(Impl) 작성
6. Controller 작성
