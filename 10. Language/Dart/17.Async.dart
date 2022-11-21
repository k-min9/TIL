void main() {
  // Future - 미래에 받아올 값  
  Future<String> name = Future.value('k-min9');
  Future<int> num = Future.value(1);
  
  
  // delayed - 지연되다. (지연기간, 지연시간 후 수행할 함수)를 params로
  print('함수 시작');
  Future.delayed(Duration(seconds:2), (){
    print('2초 경과');
  });
  
  addNum(2,3);
  // int result = await addNum2(2,2);
}

// async - await (main이 async이고 함수를 await으로 쓰려면 Future<void>를 리턴해야 함)
void addNum(int num1, int num2) async {
  
  print('await 시작');
  await Future.delayed(Duration(seconds: 1), (){
    print('await 계산: $num1 + $num2 = ${num1+num2}');
  });
  print('await 종료');
}

Future<int> addNum2(int num1, int num2) async {
  return num1 + num2;
}