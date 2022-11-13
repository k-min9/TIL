void main() {
  
  BoyTeam teamA = BoyTeam('BoyTeam1', 3);
  teamA.sayName();
  
  GirlTeam teamB = GirlTeam('GirlTeam1', 7);
  teamB.sayName();
  teamB.sayGirl();
  
  print(teamB is Team);
  
}

class Team{
  String name;
  int membersCnt;
  
  Team({
    required this.name,
    required this.membersCnt,
  });
  
  void sayName() {
    print('저희 팀 이름은 ${this.name}입니다.');
  }
}

class BoyTeam extends Team{
  
  BoyTeam(String name, int membersCnt): super(name: name, membersCnt: membersCnt);
  
}

class GirlTeam extends Team{
  
  GirlTeam(String name, int membersCnt): super(name: name, membersCnt: membersCnt);
  
  void sayGirl() {
    print('girlTeam!');
  }
  
}