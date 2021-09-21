package hello.itemservice.domain.item;

public enum ItemType {

    BOOK("도서"), FOOD("음식"), ETC("기타");

    //설명용
    private final String description;

    ItemType(String description) {
        this.description = description;
    }
}
