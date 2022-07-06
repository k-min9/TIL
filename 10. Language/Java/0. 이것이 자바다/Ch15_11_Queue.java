//선입선출인 큐에 메시지 넣고 꺼내기
package ch15;

import java.util.LinkedList;
import java.util.Queue;

public class Ch15_11_Queue {
	public static void main(String[] args) {
		//Queue의 대표적 구현 클래스 LL
		Queue<Message> messageQueue = new LinkedList<Message>();
		
		//객체(command, to) 넣기(offer)
		messageQueue.offer(new Message("sendMail", "사람 1"));
		messageQueue.offer(new Message("sendSMS", "사람 2"));
		messageQueue.offer(new Message("sendKakaotalk", "사람 3"));
		
		//객체 꺼내기(poll)
		while(!messageQueue.isEmpty()) {
			Message message = messageQueue.poll();
			switch(message.command) {
				case "sendMail":
					System.out.println(message.to + "에게 메일 전송.");
					break;
				case "sendSMS":
					System.out.println(message.to + "에게 SMS 전송.");
					break;
				case "sendKakaotalk": 
					System.out.println(message.to + "에게 카카오톡 전송.");
					break;
			}
		}
	}
}

class Message {
	public String command;
	public String to;
	
	public Message(String command, String to) {
		this.command = command;
		this.to = to;
	}
}

