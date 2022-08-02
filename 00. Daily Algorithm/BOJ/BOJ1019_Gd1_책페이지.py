'''
처음에는 10억이라 O(N)도 애매하지 않나 했더니,
알고리즘이 아니라 수학문제,
1. 10이 더해질때마다 모든값에 1이 증가하고 첫번째 자리수는 추가로 10 증가
2. 100이 더해질때마다 20이 증가하는 동시에 첫번째 자리수 100 증가
1234면 1999에서 700을 빼고 60을 빼고 5를 빼고
...
반복
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
answers = [0]*10
b = 1
while N != 0:
    while N % 10 != 9:
        for i in str(N):
            answers[int(i)] += b
        N -= 1
        
    if N < 10:
        for k in range(N+1):
            answers[k] += b
        answers[0] -= b
        break
    
    else:
        for i in range(10):
            answers[i] += (N//10 + 1) * b
    answers[0] -= b
    b *= 10
    N //= 10
    
print(*answers)
