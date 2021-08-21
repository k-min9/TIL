package ch00;

public class Ch09_02_NestedInterface {
	public static void main(String[] args) {
		//중첩인터페이스 : UI 프로그래밍에서 이벤트를 처리하는 등, 긴밀한 관계를 갖기 위해
		Button btn = new Button();
		
		btn.setOnClickListener(new CallListener());
		btn.touch();
		
		btn.setOnClickListener(new MessageListener());
		btn.touch();
	}
}

class Button {
	OnClickListener listener;
	
	void setOnClickListener(OnClickListener listener) {
		this.listener = listener;
	}
	
	void touch() {
		listener.onClick();
	}
	
	//이분이 주인공
	interface OnClickListener {
		void onClick();
	}
}

class CallListener implements Button.OnClickListener {
	@Override
	public void onClick() {
		System.out.println("전화 걸기");
	}
}

class MessageListener implements Button.OnClickListener {
	@Override
	public void onClick() {
		System.out.println("메시지 보내기");
	}
}