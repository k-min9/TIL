package ch08;

//인터페이스 사용 선언은 implements
public class Ch08_01_Television implements Ch08_01_RemoteControl {
	//필드
	private int volume;
	
	//메뉴에서 source > override/implements method 선택시, 
	//implement한 인터페이스의 추상 메소드가 자동 생성된다.(선택부분만)
	
	//turnOn() 추상>실체
	public void turnOn() {
		System.out.println("TV킴");
	}	
	//turnOn() 추상>실체
	public void turnOff() {
		System.out.println("TV끔");
	}
	//setVolume() 추상>실체
	public void setVolume(int volume) {
		if(volume>Ch08_01_RemoteControl.MAX_VOLUME) {
			this.volume = Ch08_01_RemoteControl.MAX_VOLUME;
		} else if(volume<Ch08_01_RemoteControl.MIN_VOLUME) {
			this.volume = Ch08_01_RemoteControl.MIN_VOLUME;
		} else {
			this.volume = volume;
		}
		System.out.println("현재 볼륨: " + volume);
	}
}
