package hello.itemservice.domain.item;

import lombok.Getter;
import lombok.Setter;

//@Data 같은 복합은 너무 방대해서 어디서 뭐가 잘못될지 모르기 때문에 주의(비추천)
@Getter @Setter
public class Item {

    private Long id;
    private String itemName;
    private Integer price;
    private Integer quantity;

    //생성자 두 가지 만들어두고
    public Item() {
    }

    public Item(String itemName, Integer price, Integer quantity) {
        this.itemName = itemName;
        this.price = price;
        this.quantity = quantity;
    }
}
