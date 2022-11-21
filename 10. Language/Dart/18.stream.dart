import 'dart:async';  // dart-async 패키지 필요
  
void main() {
  final controller = StreamController();
  final stream = controller.stream.asBroadcastStream();
  
  final streamListener1 = stream.listen((val){
    print('Listener 1 : $val');
  });
  
  final streamListener2 = stream.listen((val){
    print('Listener 2 : $val');
  });
  
  // functional programming 처럼 쓸 수 있음
  final streamListener3 = stream.where((val) => val%2 == 0).listen((val){
    print('Listener 3 : $val');
  });
  
  controller.sink.add(1);  // Listener에게 값 전달
  controller.sink.add(2);
  controller.sink.add(3);
  controller.sink.add(4);
}