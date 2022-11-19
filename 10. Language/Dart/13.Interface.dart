void main() {
  
  BoyTeam team1 = BoyTeam('team10');
  GirlTeam team2 = GirlTeam('team20');

}

// interface : 별도 선언 없음. abstract를 활용
abstract class TeamInterface {
  String name;
  
  TeamInterface(this.name);
  
  void sayName() {}
}

class BoyTeam implements TeamInterface {
  String name;
  
  BoyTeam(this.name);
  
  void sayName() {
    print('제 이름은 $name 입니다.');
  }
}

class GirlTeam implements TeamInterface {
  String name;
  
  GirlTeam(this.name);
  
  void sayName() {
    print('제 이름은 $name 입니다.');
  }
}
