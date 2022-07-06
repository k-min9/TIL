package ch13;

public class Ch13_02_GenericMethod {
	public static void main(String[] args) {
		Pair<Integer, String> p1 = new Pair<Integer, String>(1, "사과");
		Pair<Integer, String> p2 = new Pair<Integer, String>(1, "사과");
		//메소드에 타입을 명시함
		boolean result1 = Util.<Integer, String>compare(p1, p2);
		if(result1) {
			System.out.println("1.동등한 객체");
		} else {
			System.out.println("1.동등하지 않은 객체");
		}
		
		Pair<String, String> p3 = new Pair<String, String>("user1", "홍길동");
		Pair<String, String> p4 = new Pair<String, String>("user2", "홍길동");
		//메소드가 타입을 추정함
		boolean result2 = Util.compare(p3, p4);
		if(result2) {
			System.out.println("2.동등한 객체");
		} else {
			System.out.println("2.동등하지 않은 객체");
		}
	}
}

class Pair<K, V> {
	private K key;
	private V value;

	public Pair(K key, V value) {
		this.key = key;
		this.value = value;
	}

	public void setKey(K key) { this.key = key; }
	public void setValue(V value) { this.value = value; }
	public K getKey()   { return key; }
	public V getValue() { return value; }
}

class Util {
	public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
		boolean keyCompare = p1.getKey().equals(p2.getKey()) ;
		boolean valueCompare = p1.getValue().equals(p2.getValue());
	    return keyCompare && valueCompare;
	}
}
