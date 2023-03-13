import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

/**
 * 만들어진 DTO. key와 형태를 정의할 수 있다.
 */
public class MyDto extends HashMap<String, Object> {
    private String name = null;
    private Integer age = null;
    private BigDecimal price = null;
    private Boolean isActive = null;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
        this.put("name", name);
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
        this.put("age", age);
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
        this.put("price", price);
    }

    public Boolean getIsActive() {
        return isActive;
    }

    public void setIsActive(Boolean isActive) {
        this.isActive = isActive;
        this.put("isActive", isActive);
    }

    public MyDto(HashMap parent) {
        super(parent);
        this.put("name", null);
        this.put("age", null);
        this.put("price", null);
        this.put("isActive", null);
    }

    private void validateKey(String key) {
        switch (key) {
            case "name":
            case "age":
            case "price":
            case "isActive":
                break;
            default:
                throw new IllegalArgumentException("Invalid key: " + key);
        }
    }

    @Override
    public Object put(String key, Object value) {
        validateKey(key);
        return super.put(key, value);
    }

    @Override
    public Object get(Object key) {
        validateKey(key.toString());
        return super.get(key);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        for (Map.Entry<String, Object> entry : this.entrySet()) {
            sb.append("\"").append(entry.getKey()).append("\": ").append(entry.getValue()).append(", ");
        }
        sb.delete(sb.length() - 2, sb.length());
        sb.append("}");
        return sb.toString();
    }
}
