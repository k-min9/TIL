package ch11;

//객체 비교
import java.util.Comparator;
import java.util.Objects;

public class Ch11_05_methodCompare {
	public static void main(String[] args) {
		Student s1 = new Student(1);
		Student s2 = new Student(1);
		Student s3 = new Student(2);
		
		//a와 b와 a와b의 비교메소드<제너릭>
		int result = Objects.compare(s1, s2, new  StudentComparator());
		System.out.println(result);
		result = Objects.compare(s1, s3, new  StudentComparator());
		System.out.println(result);
	}
	
	static class Student {
		int sno;
		Student(int sno) {
			this.sno = sno;
		}
	}
	
	static class StudentComparator implements Comparator<Student> {
		@Override
		public int compare(Student a, Student b) {
			/*if(a.sno<b.sno) return -1;
			else if(a.sno == b.sno) return 0;
			else return 1;*/
			return Integer.compare(a.sno, b.sno);
		}
	}
}
