package ch11;
//15장에서 더 자세히
import java.util.HashMap;

//hashcode는 객체를 식별하는 유일한 코드를 의미한다.
public class Ch11_01_methodHashcode {
	public static void main(String[] args) {
		//15장에서 더 자세히
		HashMap<Key, String> hashMap = new HashMap<Key, String>();
		
		//식별키 new Key(1)으로 홍길동 저장
		hashMap.put(new Key(1), "홍길동");
		
		//new Key(1)로 홍길동 읽어오기
		String value  = hashMap.get(new Key(1));
		System.out.println(value);
		
		Object obj = new Object();
		System.out.println(obj);
		System.out.println(obj.hashCode());
	}
}

class Key {
	public int number;
	
	public Key(int number) {
		this.number = number;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Key) {
			Key compareKey = (Key) obj;
			if(this.number == compareKey.number) {
				return true;
			}
		} 
		return false;
	}
	//이부분의 hashcode를 오버라이드 하지 않는 한, 홍길동을 찾지 못하고 null이 된다.(기존 key != 생성 key)
	// id가 동일할 경우, 같은 해시코드를 리턴
//	@Override
//	public int hashCode() {
//		return number;
//	}
}
