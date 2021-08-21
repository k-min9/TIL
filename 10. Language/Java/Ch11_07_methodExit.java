package ch11;


public class Ch11_07_methodExit {
	public static void main(String[] args)  {
		//���� ������ ����
		System.setSecurityManager(new SecurityManager(){
			@Override
			public void checkExit(int status) {
				if(status != 5) {
					throw new SecurityException();
				}
			}
		});
		
		for(int i=0; i<10; i++) {
			//i�� ���
			System.out.println(i);
			try {
				//JVM ���� ��û
				System.exit(i);
			} catch(SecurityException e) { }
		}
	}
}

