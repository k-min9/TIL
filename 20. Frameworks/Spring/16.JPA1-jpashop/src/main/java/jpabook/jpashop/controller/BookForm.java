package jpabook.jpashop.controller;

import lombok.Getter;
import lombok.Setter;

//이번 예시에서는 책까지만
@Getter @Setter
public class BookForm {
    private Long id;

    private String name;
    private int price;
    private int stockQuantity;

    private String author;
    private String isbn;
}
