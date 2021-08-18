package ch07;

public class Ch07_00_Student extends Ch07_00_People{
	public int studentNo;
	
	public Ch07_00_Student(String name, String ssn, int studentNo) {
		super(name, ssn);
		this.studentNo = studentNo;
	}
}

