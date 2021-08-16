
public class Ch04_01_switchOR {
	public static void main(String[] args) {
		char grade = 'B';
		
		//break 잡는 시점으로 cascading 해도 되고, 이렇게 다중 변수 해도 되고
		switch(grade) {
			case 'A':
			case 'a':
				System.out.println("��� ȸ���Դϴ�.");
				break;
			case 'B':
			case 'b':
				System.out.println("�Ϲ� ȸ���Դϴ�.");
				break;							
			default:
				System.out.println("�մ��Դϴ�.");
		}
	}
}
