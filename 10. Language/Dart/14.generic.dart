void main() {
  Lecture<String, String> lecture1 = Lecture('1234', 'lecture1', 'math');
  Lecture<int, String> lecture2 = Lecture(12, 'lecture1', 'English');
}

// generic : 타입을 외부에서 넣자
class Lecture<T, X> {
  final T id;
  final String name;
  final X type;
  
  Lecture(this.id, this.name, this.type);
}