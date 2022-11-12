void main() {
  // non-nullable이 default
  // nullable : null이 될 수 있음
  String name = 'k-min9';
//   name = null;  // null이 기본 될 수 없음
  print(name!);  // ! : 절대로 null이 될 수 없음. null이 아님을 주위에 알림
  
  String? name2;  // nullable
  name2 = null;
  print(name2);
  
  // final, const
  final String name3 = 'k-min9';
  final name4 = 'k-min9';  // 타입 생략 가능 (var로 됨)
  
  const name5 = 'k-min9';  // Build 타임에 값을 알고 있어야 함.
//   const time = DateTime.now();
  
  // dateTime : 시간 날짜
  DateTime now = DateTime.now();
}
