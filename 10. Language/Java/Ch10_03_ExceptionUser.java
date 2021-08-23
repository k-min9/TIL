package ch00;

public class Ch10_03_ExceptionUser {
	public static void main(String[] args) {
		Account account = new Account();
		//예금
		account.deposit(10000);
		System.out.println("저축: " + account.getBalance());
		//비정상적 출금(10000<30000)
		try {
			account.withdraw(30000);
		} catch(BalanceInsufficientException e) {
			String message = e.getMessage();
			System.out.println(message);
			System.out.println();
			e.printStackTrace();
		}
	}
}

class Account {
	private long balance;

	public Account() { }	

	public long getBalance() {
		return balance;
	}	
	public void deposit(int money) {
		balance += money;
	}
	//사용자 정의 예외 throw
	public void withdraw(int money) throws BalanceInsufficientException {
		//발생 조건
		if(balance < money) {
			throw new BalanceInsufficientException("잔고부족:"+(money-balance)+"모자람");
		}
		balance -= money;
	}
}

//예외이름은 Exception으로 끝내는게 기본적인 convention
class BalanceInsufficientException extends Exception {
	public BalanceInsufficientException() { }
	public BalanceInsufficientException(String message) {
		super(message);
	}
}
