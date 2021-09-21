package hello.itemservice.domain.item;

public enum ItemType {

    BOOK("도서"), FOOD("음식"), ETC("기타");

    //설명용
    private final String description;

    ItemType(String description) {
        this.description = description;
    }

    //프록시 접근이니까 getter 당연히 필요하고.
    public String getDescription() {
        return description;
    }
}
