package ch00;

public class Ch10_01_try_with_resource {
	public static void main(String[] args) {
		try (FileInputStream fis = new FileInputStream("file.txt")) {
			fis.read();
			//강제 예외 발생 코드
			throw new Exception();
		} catch(Exception e) {
			System.out.println("리소스 반환.");
		}
	}
}

//AutoCloseable을 implement해야 작동(java.lang에 있음)
class FileInputStream implements AutoCloseable {
	private String file;
	
	public FileInputStream(String file) {
		this.file = file;
	}
	
	public void read() {
		System.out.println(file + "읽기.");
	}
	
	@Override
	public void close() throws Exception {
		System.out.println(file + "닫기.");
	}
}
