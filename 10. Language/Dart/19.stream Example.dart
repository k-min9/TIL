import 'dart:async';  // dart-async 패키지 필요
  
void main() {
  
  playAllStream().listen((val){
    print(val);
  });
  
  calculate(2).listen((val){
    print('calculate(2) : $val');
  });  
  
  calculate(4).listen((val){
    print('calculate(4) : $val');
  });
}

// calc(1)이 다 실행되어야 calc(1000)이 시작됨
Stream<int> playAllStream() async* {
  yield* calculate(1);
  yield* calculate(1000);
}

Stream<int> calculate(int num) async* {
  for (int i = 0; i < 5; i++) {
    yield i * num;  // yield 볼때마다 값을 뿌려줌
    
    await Future.delayed(Duration(seconds: 1));  // 1초 대기도 넣을 수 있음
  }
}