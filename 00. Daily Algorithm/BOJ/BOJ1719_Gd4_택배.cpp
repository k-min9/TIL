/*cpp로 플로이드 와셜, 중간경로(k) 구하기*/
#include <cstdio>
#define INF 987654321;

//using namespace std;

// 초기 값
int N, M;
int graphs[201][201], answers[201][201];

int main()
{
  // 입력
  scanf("%d %d", &N, &M);

  for (int y = 1; y <= N; y++)
    for (int x = 1; x <= N; x++)
      {
        graphs[y][x] = INF;
        if (x == y){
          graphs[y][x] = 0;
        }
      }
  
  int a, b, w;
  for (int i = 0; i < M; i++)
  {
    scanf("%d %d %d", &a, &b, &w);
    graphs[a][b] = w;
    graphs[b][a] = w;
    answers[a][b] = b;
    answers[b][a] = a;
  }

  // 플로이드
  for(int k = 1; k <= N; k++)
    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= N; j++){
        if (graphs[i][j] > graphs[i][k] + graphs[k][j])
        {
          graphs[i][j] = graphs[i][k] + graphs[k][j];
          if (i!=k) answers[i][j] = answers[i][k];
        }
      }

  // 출력
  for (int y = 1 ; y <= N; y++)
  {
    for (int x = 1 ; x <= N; x++)
    {
      if (answers[y][x])
      {
        printf("%d ", answers[y][x]);
      }
      else
      {
        printf("- ");
      }
    }
    printf("\n");
  }
}
