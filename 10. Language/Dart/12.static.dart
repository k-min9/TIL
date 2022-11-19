void main() {
  Employee employee1 = Employee('k-min9');
  Employee employee2 = Employee('kk');
  
  Employee.building = '빌딩이름';
  
  employee1.printNameAndBuilding();
  employee2.printNameAndBuilding();
  Employee.printBuilding();
}

class Employee {
  static String? building;
  final String name;
  
  Employee(this.name,);
  
  void printNameAndBuilding() {
    print('저는 $name, $building에서 근무중이죠');
  }
  
  static void printBuilding() {
    print('저는 $building 건물에서 근무중입니다.');
  }
}