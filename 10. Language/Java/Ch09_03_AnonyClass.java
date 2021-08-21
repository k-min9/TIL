package ch00;

//익명 클래스 : 어차피 한번 쓰고 버릴꺼 이름조차 지을필요 없지 않아??? 안쓰는게 깔끔할듯
//위와 비교해보자
public class Ch09_03_AnonyClass {
	public static void main(String[] args) {
		Window w = new Window();
		w.button1.touch();
		w.button2.touch();
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
	
	interface OnClickListener {
		void onClick();
	}
}

class Window {
	Button button1 = new Button();
	Button button2 = new Button();
	
	//필드 초기값 대입
	Button.OnClickListener listener = new Button.OnClickListener() {
		@Override
		public void onClick() {
			System.out.println("전화 걸기");
		}
	};
	
	Window() {
		
		////이 부분 부터가 완전 다르다
		//매개값 초기화
		button1.setOnClickListener(listener);
		
		//매개값 필드 대입
		button2.setOnClickListener(new Button.OnClickListener() {
			@Override
			public void onClick() {
				System.out.println("메시지 걸기");
			}
		});
	}
}