package ch11;

//equals. 객체(Object)수준에서 동등한지 확인
public class Ch11_00_methodEquals {
	public static void main(String[] args) {
		Member obj1 = new Member("blue");
		Member obj2 = new Member("blue");
		Member obj3 = new Member("red");
		
		if(obj1.equals(obj2)) {
			System.out.println("obj1= obj2");
		} else {
			System.out.println("obj1!= obj2");
		}
		
		if(obj1.equals(obj3)) {
			System.out.println("obj1= obj3");
		} else {
			System.out.println("obj1!= obj3");
		}
	}
}

class Member {
	public String id;
	
	public Member(String id) {
		this.id = id;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Member) {
			Member member = (Member) obj;
			if(id.equals(member.id)) {
				return true;
			}
		}
		return false;
	}
}

