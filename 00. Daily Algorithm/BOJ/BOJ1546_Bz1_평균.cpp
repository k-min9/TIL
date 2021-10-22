/**
 * 언어 : cpp
*/
#include <stdio.h>

int main()
{
  // 시험 갯수, 개별 시험 점수, 최대 값, 총 합
  int N, x;
  int max=0;
  int total=0;
	scanf("%d",&N);
	for (int i=0 ; i<N ; i++)
	{
		scanf("%d",&x);
		if (max<x) max=x;
		total+=x;
	}
	printf("%f",(float)total*100/(N*max));
	return 0;
}