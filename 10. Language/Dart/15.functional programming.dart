void main() {
  List<String> members = ['member1', 'member2', 'member3', 'member3'];
  // collection간 형변환
  print(members);
  print(members.asMap());
  print(members.asMap().keys);  
  print(members.toSet());
  
  Map membersMap = members.asMap();
  print(membersMap.values.toList());
  
  Set membersSet = Set.from(members);
  print(members);
  
  // map1
  var helloMembers = members.map((x) {
    return 'hello $x';
  });
  print(helloMembers);
  
  // map2
  String nums = '13579';
  final parsed = nums.split('').map((x)=> '$x.jpg').toList();
  print(parsed);
  
  // map3
  final memberEntry = membersMap.map(
    (key, value) => MapEntry(
      '멤버이름 $key',
      '영어이름 $value'
    )
  );
  print(memberEntry);
  final memberKeys = membersMap.keys.map((x) => '이름 $x').toList();
  print(memberKeys);
  
  // where
  List<Map<String, String>> teams = [
    {
      'name' : '이름1',
      'group' : 'teamA'
    },
    {
      'name' : '이름2',
      'group' : 'teamB'
    },
    {
      'name' : '이름3',
      'group' : 'teamB'
    },
    {
      'name' : '이름4',
      'group' : 'teamA'
    },
  ];
  final teamWhere = teams.where((x) => x['group']=='teamA').toList();
  print(teamWhere);
  
  // reduce : return값이 첫 parameter로 쓰임
  List<int> numbers = [1,3,5,7,9];
  final result = numbers.reduce((prev, next){
    print('----------------');
    print('prev : $prev');
    print('next : $next');
    print('total : ${prev + next}');
    
    return prev + next;
  });
  print(result);
  
  // fold : reduce의 리턴값 타입이 동일해야되는 제약을 해제
  List<String> words = ['오늘은', '매우', '맑은 날씨입니다.'];
  final wordsCnt = words.fold<int>(0, (prev, next) => prev + next.length);
  print(wordsCnt);
  
  // List 합치기
  List<int> even = [2, 4, 6];
  List<int> odd = [1, 3, 5];
  List<int> newList = [...even, ...odd];
  print(newList);
  
}
