package jpabook.jpashop.domain;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Category {

    @Id @GeneratedValue
    private Long id;

    private String name;

    // Parent가 되게 흥미로운 구조라는데 일단 자세한 설명은 다음 강의
    @ManyToOne
    @JoinColumn(name = "PARENT_ID")
    private Category parent;

    @OneToMany(mappedBy = "parent")
    private List<Category> child = new ArrayList<>();

    @ManyToMany // 실무에서 저얼때쓰면 안되지만 어떻게 돌아가는지 확인하기 위해서 한번 예시
    @JoinTable( name = "CATEGORY_ITEM",
            joinColumns = @JoinColumn(name = "CATEGORY_ID"), // 내가 조인하는건 얘고
            inverseJoinColumns = @JoinColumn(name = "ITEM_ID") // 반대쪽에서 조인하는건 얘야
    )
    private List<Item> items = new ArrayList<>();


}
