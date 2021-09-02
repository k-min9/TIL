package hello.itemservice.web.basic;

import hello.itemservice.domain.item.Item;
import hello.itemservice.domain.item.ItemRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.annotation.PostConstruct;
import java.util.List;

@Controller
@RequestMapping("/basic/items")
@RequiredArgsConstructor// 주입 받을 곳에 생성자 + @autowired 생략
public class BasicItemController {

    private final ItemRepository itemRepository;

    @GetMapping
    public String items(Model model){
        List<Item> items = itemRepository.findAll();
        model.addAttribute("items", items);
        return "basic/items";
    }

    @GetMapping("/{itemId}")
    public String item(@PathVariable long itemId, Model model) {
        Item item = itemRepository.findbyId(itemId);
        model.addAttribute("item", item);
        return "basic/item";
    }

    //상품등록 URL과 처리 URL을 통일하면서 메서드로 기능을 구분한다. 그러면 하나의 URL로 등록폼과 처리를 깔끔하게 할 수 있다.
    @GetMapping("/add")
    public String addForm() {
        return "basic/addForm";
    }

    //변수의 이름 Form의 name
    //@PostMapping("/add")
    public String addItemV1(@RequestParam String itemName,
                            @RequestParam int price,
                            @RequestParam Integer quantity,
                            Model model) {

        Item item = new Item();

        item.setItemName(itemName);
        item.setPrice(price);
        item.setQuantity(quantity);

        itemRepository.save(item);

        model.addAttribute("item", item);

        //저장된 상세 화면으로
        return "basic/item";
    }

    //@PostMapping("/add")
    public String addItemV2(@ModelAttribute("item") Item item, Model model) {

        itemRepository.save(item);
 //       model.addAttribute("item", item); // 자동 추가 => 생략 가능

        return "basic/item";
    }

    //이것저것 생략하기
    //@PostMapping("/add")
    //타입의 첫 문자를 소문자로 한 것이 Item>item 객체의 이름이 된다.
    public String addItemV3(@ModelAttribute Item item, Model model) {

        itemRepository.save(item);
        //       model.addAttribute("item", item); // 자동 추가 => 생략 가능

        return "basic/item";
    }

    //이것저것 생략하기
    //@PostMapping("/add")
    //@ModelAttribute까지 생략
    public String addItemV4(Item item, Model model) {

        itemRepository.save(item);
        //       model.addAttribute("item", item); // 자동 추가 => 생략 가능

        return "basic/item";
    }

    // 새로고침 무한 등록 문제 해결 >> 리다이렉트
    //@PostMapping("/add")
    public String addItemV5(Item item, Model model) {
        itemRepository.save(item);
        return "redirect:/basic/items/"+item.getId();
    }

    //리다이렉트의 문제를 해결해주는 redirectattribute
    @PostMapping("/add")
    public String addItemV6(Item item, RedirectAttributes redirectAttributes) {
        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true); //저장 상태 변수 true= 성공 이거 item.html에서 써먹어보자
        return "redirect:/basic/items/{itemId}"; //+item.getId();는 URL 인코딩 오류가 생길 수 있다.
    }

    //상품 수정 폼
    @GetMapping("/{itemId}/edit")
    public String editForm(@PathVariable Long itemId, Model model) {
        Item item = itemRepository.findbyId(itemId);
        model.addAttribute("item", item);
        return "basic/editForm";
    }

    //상품 등록과 매우 유사
    @PostMapping("/{itemId}/edit")
    public String edit(@PathVariable Long itemId, @ModelAttribute Item item) {
        itemRepository.update(itemId, item);
        //리다이렉트
        return "redirect:/basic/items/{itemId}";
    }


    //테스트용 자료
    @PostConstruct
    public void init() {
        itemRepository.save(new Item("testA", 10000, 10));
        itemRepository.save(new Item("testA", 20000, 20));
    }

}
