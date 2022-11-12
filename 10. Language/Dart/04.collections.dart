void main() {
  // List (타입 혼용 불가, 준수 필수)
  List<String> teams = ['personA', 'personB'];
  List<int> nums = [1,2,3,4,5,6];
  print(nums);
  print(nums[1]);
  print(nums.length);
  
  // Map (Key - Value)
  Map<String, String> dict1 = {'1': 'k', 'min': '9', '3': 'a'};
  print(dict1['3']);
  dict1.addAll({'4':'what'});
  print(dict1);
  print(dict1.keys);
  print(dict1.values);
  
  // Set
  Set<String> players = {'player1', 'player2', 'player1'};  // 중복 제거
  print(players);
  print(players.contains('player1'));
}
