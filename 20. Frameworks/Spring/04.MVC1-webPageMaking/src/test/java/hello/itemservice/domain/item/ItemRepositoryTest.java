package hello.itemservice.domain.item;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class ItemRepositoryTest {

    ItemRepository itemRepository = new ItemRepository();

    @AfterEach
    void 끝나고정리() {
        itemRepository.clearStore();
    }

    @Test
    void save(){
        // given
        Item item = new Item("ItemA", 10000, 10);

        // when
        Item saved = itemRepository.save(item);

        //then
        Item find = itemRepository.findbyId(item.getId());
        assertThat(find).isEqualTo(saved);
    }

    @Test
    void findAll(){
        //given
        Item item1 = new Item("1번", 10000, 10);
        Item item2 = new Item("2번", 25000, 10);

        itemRepository.save(item1);
        itemRepository.save(item2);

        //when
        List<Item> result = itemRepository.findAll();

        //then
        assertThat(result.size()).isEqualTo(2);
        assertThat(result).contains(item1, item2);
    }

    @Test
    void updateItem(){
        //given
        Item item = new Item("1번", 10000, 10);

        Item saved_item = itemRepository.save(item);
        Long saved_id = saved_item.getId();

        //when
        Item updateParam = new Item("1번 재고충전", 20000, 30);
        itemRepository.update(saved_id, updateParam);

        //then
        Item findItem = itemRepository.findbyId(saved_id);

        assertThat(findItem.getItemName()).isEqualTo(updateParam.getItemName());
        assertThat(findItem.getPrice()).isEqualTo(updateParam.getPrice());
        assertThat(findItem.getQuantity()).isEqualTo(updateParam.getQuantity());

    }




}