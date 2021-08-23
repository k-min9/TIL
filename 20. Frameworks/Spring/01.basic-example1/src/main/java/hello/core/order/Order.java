package hello.core.order;

public class Order {
    private Long memberId;
    private String itemName;
    private int itemPrice;
    private int dicountPrice;

    public Order(Long memberId, String itemName, int itemPrice, int dicountPrice) {
        this.memberId = memberId;
        this.itemName = itemName;
        this.itemPrice = itemPrice;
        this.dicountPrice = dicountPrice;
    }

    public int calculatePrice(){
        return itemPrice - dicountPrice;
    }

    public Long getMemberId() {
        return memberId;
    }

    public void setMemberId(Long memberId) {
        this.memberId = memberId;
    }

    public String getItemName() {
        return itemName;
    }

    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public int getItemPrice() {
        return itemPrice;
    }

    public void setItemPrice(int itemPrice) {
        this.itemPrice = itemPrice;
    }

    public int getDicountPrice() {
        return dicountPrice;
    }

    public void setDicountPrice(int dicountPrice) {
        this.dicountPrice = dicountPrice;
    }

    //객체 tostring 출력으로 내용물 편하게 보려고 넣었음.
    @Override
    public String toString() {
        return "Order{" +
                "memberId=" + memberId +
                ", itemName='" + itemName + '\'' +
                ", itemPrice=" + itemPrice +
                ", dicountPrice=" + dicountPrice +
                '}';
    }
}
