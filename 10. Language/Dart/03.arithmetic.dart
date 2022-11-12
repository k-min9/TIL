void main() {
  // 다른 언어에도 있는 arithmetic
  int num = 1;
  
  num++;
  print(num);
  
  double num2 = 2.0;
  num2++;
  print(num2);
  num2 += 5;
  print(num2);

  // 값이 null 일경우 바꿔라
  double? num3 = 4.0;
  num3 = null;
  num3 ??= 3.0; 
  print(num3);
  
  num3 = 2.0;
  num3 ??= 3.0;
  print(num3);
  
  // 비교(생략) : != == > >= < <=
  
  // 타입비교 (null 값일때는 제대로 안 나옴)
  int num4 = 1;
  print(num4 is int);
  print(num4 is String);
  print(num4 is !int);
  
  // 비교 연산(생략) : && ||  
  
}
