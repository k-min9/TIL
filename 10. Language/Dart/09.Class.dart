class Team {
  String name;
  List<String> members;
  
  // immutable 선언
//   final String name;
//   final List<String> members;
  
  // constructor
  Team(String name, List<String> members)
    : this.name = name,
      this.members = members;
  
  // named Constructor, 초기값 부여시 named constructor는 final이 여기서 충돌
  Team.fromList(List values)
    : this.members = values[0],
      this.name = values[1];
  
  // const constructor : flutter에 효율적인 방식 중 하나
//   const Team(this.name, this.members);
  
  void sayHello() {
    print('안녕하십니까');
  }
  
  void introduce() {
    print('저희 멤버는 ${this.members}가 있습니다.');
  }
  
  // getter
  String get firstMember {
    return this.members[0];
  }
  
  // setter : setter은 하나의 변수만 받을 수 있음. 거기에 collection도 못 씀
  // 애초에 immutable(final) 설정이 힘드니 잘 안 씀
  String set firstMember(String name) {
    this.members[0] = name;
  }
}


// private Class 선언 : 언더스코어(_)를 이름 앞에 붙이기
class _Group {
  //...
}

void main() {
  Team myTeam = Team('k-min9', ['memberA', 'memberB']);
  
  print(myTeam.name);
  print(myTeam.members);
  myTeam.sayHello();
  myTeam.introduce();
  print('=================');
  
  // getter, setter
  print(myTeam.firstMember);
  myTeam.firstMember = 'memberSpecial';
  print(myTeam.firstMember);
  print('=================');
  
  
  Team yourTeam = Team.fromList([
    ['memberA', 'memberC'],
    'kmin9'
  ]);
  
  print(yourTeam);
  yourTeam.introduce();
  
//   Team constTeam = const Team('team3', ['memberD', 'memberE']);

}
