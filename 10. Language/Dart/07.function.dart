// 괄호 내는 기본 값. optional parameter
addNums(int x, [int y = 20, int z = 30]) {
  return x + y + z;
}

// named parameter을 쓴 함수
addNumsNamed({
  required int x,
  required int y,
  int z = 30  // required 없으면 optional
}) {
  return x + y + z;
}

void main() {
  print(addNums(10));
  print(addNums(10, 15));
  print(addNums(10, 15, 20));
  
  print(addNumsNamed(x: 10, y: 15, z: 20));
  print(addNumsNamed(x: 10, z: 20, y: 15));  // named는 순서가 중요하지 않음
  print(addNumsNamed(x: 10, y: 15));
}
