package hello.itemservice.domain.item;

import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Repository
public class ItemRepository {

    //Long 부분에 id 들어와서 타입맞춤
    //실제로는 해쉬맵 쓰면 안됩니다 (멀티스레드 환경에서 망가짐) >> ConcurrentHashmap 쓰자, Long도 AtomicLong쓰자.
    //static 주의!
    private static final Map<Long, Item> store = new HashMap<>();
    private static long sequence = 0L;

    public Item save(Item item){
        item.setId(++sequence);
        store.put(item.getId(), item);
        return item;
    }

    public Item findbyId(Long id){
        return store.get(id);
    }

    public List<Item> findAll() {
        return new ArrayList<>(store.values());
    }

    // id와 변경 파라미터만 넘겨서 변경해보자.
    public void update(Long itemId, Item updateParam){
        Item item = findbyId(itemId);
        item.setItemName(updateParam.getItemName());
        item.setPrice(updateParam.getPrice());
        item.setQuantity(updateParam.getQuantity());
    }

    // 테스트용 (해쉬 맵 초기화)
    public void clearStore(){
        store.clear();
    }

}
