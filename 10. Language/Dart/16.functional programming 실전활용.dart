void main() {
  final List<Map<String, String>> members = [
    {
      'team' : 'team1',
      'name' : 'member1',
    },
    {
      'team' : 'team2',
      'name' : 'member2',
    },
    {
      'team' : 'team2',
      'name' : 'member3',
    },
    {
      'team' : 'team1',
      'name' : 'member4',
    },
  ];
  
  // 기존 class에 input 값을 mapping
  final parsedMembers = members.map(
    (x) => Person(
      team: x['team']!,
      name: x['name']!,
    ),
  );
  
  print(parsedMembers);
  
  // 실전
  for (Person person in parsedMembers) {
    print(person.name);
  } 
  
  final team1 = parsedMembers.where(
    (x) => x.team == 'team1',
  );
  print(team1);
  
}


// class를 사용해서 들어오는 값을 확신할 수 있음
class Person {
  final String name;
  final String team;
  
  Person({
    required this.name,
    required this.team,
  });
  
  @override
  String toString() {
    return 'Person(name:$name, team:$team)';
  }
}