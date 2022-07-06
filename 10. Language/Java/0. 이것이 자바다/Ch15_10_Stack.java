//후입 선출인 스택에 동전 넣고 꺼내기
package ch15;

import java.util.Stack;

public class Ch15_10_Stack {
	public static void main(String[] args) {
		Stack<Coin> coinBox = new Stack<Coin>();
		
		//넣은 순서(put) 100 50 500 10
		coinBox.push(new Coin(100));
		coinBox.push(new Coin(50));
		coinBox.push(new Coin(500));
		coinBox.push(new Coin(10));
		
		//pop으로 꺼내기 >> 10 500 50 100 순서로 꺼냄
		while(!coinBox.isEmpty()) {
			Coin coin = coinBox.pop();
			System.out.println("다음 동전 : " + coin.getValue() + "원");
		}

	}
}

class Coin {
	private int value;
	
	public Coin(int value) {
		this.value = value;
	}
	
	public int getValue() {
		return value;
	}
}