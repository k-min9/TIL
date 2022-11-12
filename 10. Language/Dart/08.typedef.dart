typedef Operation = int Function(int x, int y, int z);

// 시그내쳐가 완전히 동일한 함수를 선언
int add(int x, int y, int z) => x + y + z;
int subtract(int x, int y, int z) => x - y - z;

// 실제 사용
int calc(int x, int y, int z, Operation operation) {
  return operation(x, y, z);
}

void main() {
  Operation operation = add;  // 함수를 변수처럼 사용
  int result;
  
  result = operation(10, 20, 30);
  print(result);
  
  operation = subtract;
  
  result = operation(10, 20, 30);
  print(result);
  
  result = calc(10, 20, 30, add);
  print(result);
  
}
