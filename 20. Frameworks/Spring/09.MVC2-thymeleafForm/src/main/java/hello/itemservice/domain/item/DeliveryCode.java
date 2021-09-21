package hello.itemservice.domain.item;

import lombok.AllArgsConstructor;
import lombok.Data;

// 배송방식 : 빠른, 일반, 느린 배송
@Data
@AllArgsConstructor
public class DeliveryCode {

    private String code;
    private String displayName;

}
