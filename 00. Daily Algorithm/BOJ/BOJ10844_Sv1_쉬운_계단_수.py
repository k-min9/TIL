'''
감상 : 머엉
접근 : 
X로 끝난 길이 N의 계단수를 부르고 불러서... 
0 1 2 3 4 5 6 7 8 9
0 1 1 1 1 1 1 1 1 1 = 9
1 1 2 2 2 2 2 2 2 1 = 17 = 9 * 2 - 1
1 3 3 4 4 4 4 4 3 2 = 32 = 17 * 2 - 2
3 4 7 7 8 8 8 7 6 3 = 61 = 32 * 2 - 3
기존거*2 - 양쪽 끝이라는 뭔가 그럴싸한거 나왔지만 무시하고...
'''

n = int(input())

#2차원 리스트 생성
stairs = [[1]*10 for _ in range(n)] 
stairs[0][0] = 0

for i in range(1,n):
    stairs[i][0] = stairs[i-1][1]
    stairs[i][9] = stairs[i-1][8]
    for j in range(1,9):
        stairs[i][j] = stairs[i-1][j-1] + stairs[i-1][j+1]

print(sum(stairs[n-1])%1000000000)


'''
감상
1. 나머지를 출력하시오 안 읽고 한번 틀림. 앞으로 주의
2. C++ 0ms 무엇... 데이터 용량 1/10 무엇...
3. 문제 딱 보고 10초 멍때렸는데 이런건 문제 많이 풀이면 보완할 수 있을 것 같다고 느낌
'''