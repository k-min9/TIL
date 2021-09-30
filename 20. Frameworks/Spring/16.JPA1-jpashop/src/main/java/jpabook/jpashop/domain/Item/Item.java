package jpabook.jpashop.domain.Item;

import jpabook.jpashop.domain.Category;
import jpabook.jpashop.exception.NotEnoughStockException;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "dtype")
public class Item {

    @Id
    @GeneratedValue
    @Column(name = "item_id")
    private Long id;

    private String name;
    private int price;
    private int stockQuantity;

    @ManyToMany(mappedBy = "items")
    private List<Category> categories = new ArrayList<>();

    //비지니스 로직 : 제품 수량 증가 감소 >> 직접 실행하는 것보다, Entity쪽에서 비지니스 로직을 가지는 쪽이 관리가 편하다.

    // 수량 증가
    public void addStock(int quantity){
        this.stockQuantity += quantity;
    }

    // 수량 감소
    public void removeStock(int quantity) {
        int restStock = this.stockQuantity - quantity;
        if (restStock < 0) {
            throw new NotEnoughStockException("재고 부족"); // 아예 예외를 하나 만들자.
        }
        this.stockQuantity = restStock;
    }


}
