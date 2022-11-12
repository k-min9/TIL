void main() {
  // If 문
  int number = 6;
  if (number%2 == 0) print('짝수');
  if (number%3 == 0) {
    print('나머지 0');
  } else if (number%3 == 1) {
    print('나머지 1');
  } else {
    print('나머지 2');
  }

  // Switch 문
  switch (number%3) {
    case 0:
      print('나머지 0');
      break;
    case 1:
      print('나머지 1');
      break;
    default:
      print('나머지 2');
      break;
  }

  // for
  for (int i = 0; i < 10; i++) print(i);

  List<int> nums = [1, 2, 3, 4, 5];
  for (int num in nums) {
    print(num);
  }

  // while
  int i = 0;
  while (i<10) {
    print(i);
    i++;
  }

  i = 0;
  while (true) { 
    print(i);
    i++;
    if (i == 3) continue;
    if (i == 5) break;
  }
}
