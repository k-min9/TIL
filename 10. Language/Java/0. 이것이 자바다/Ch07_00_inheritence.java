package ch07;

public class Ch07_00_inheritence {
	public static void main(String[] args) {
		Ch07_00_Student student = new Ch07_00_Student("강민구", "123456-1234567", 1);
		System.out.println("name : " + student.name);
		System.out.println("ssn : " + student.ssn);
		System.out.println("studentNo : " + student.studentNo);
	}
}
