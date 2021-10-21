#include <cstdio>
using namespace std;

int main(){
  int arr[101];
  int N, answer = 0;

  scanf("%d", &N);
  for (int i = 1; i <= N; i++){
    scanf("%d", arr+i);
  }

  // 역순으로 읽어오면서 정리
  for (int i = N-1 ; i >= 1; i--){
    if (arr[i+1] <= arr[i])
      answer += arr[i] - arr[i+1] + 1;
      arr[i] = arr[i+1] - 1;
  }
  printf("%d", answer);

  return 0;
}
