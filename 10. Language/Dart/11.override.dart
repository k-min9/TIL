void main() {
  
  TimesFour tf = TimesFour(13);
  
  print(tf.calc());
  
}

class TimesTwo {
  final int num;
  
  TimesTwo(this.num);
  
  // method
  int calc() {
    return num * 2;
  }
}

class TimesFour extends TimesTwo {
  TimesFour (
    int num
  ) : super(num);
  
  @override  // 생략은 가능하지만 생략하지 말자
  int calc() {
//     return this.num * 4;
    return super.calc() * 2;
  }
}
