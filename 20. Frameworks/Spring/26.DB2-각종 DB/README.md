# DB 활용 기술

개요 : 다양한 데이터 기술을 실제로 학습해보고, 실무에 활용되는 기술을 예시를 적용해보자.

## 데이터 접근 기술

- SQL Mapper : SQL만 작성하면 편리하게 Mapping
  - JDBC Template
  - Mybatis
- ORM : 객체와 관계형 DB를 자동으로 Mapping
  - JPA(자바 표준 ORM 인터페이스), Hibernate(구현체)
  - 스프링 데이터 JPA
  - Querydsl

## 실제 예제

아래 ItemRepository를 각각의 DB에서 어떻게 구현하는지 알아보자.

``` Java
public interface ItemRepository {

    Item save(Item item);

    void update(Long itemId, ItemUpdateDto updateParam);

    Optional<Item> findById(Long id);

    List<Item> findAll(ItemSearchCond cond);

}
```
