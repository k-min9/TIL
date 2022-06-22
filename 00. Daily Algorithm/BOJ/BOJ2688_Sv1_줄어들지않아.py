'''
NQueen 최속풀이때도 느꼈지만, 이런 문제 O(1)로 풀려버려서 아마 안나올거라고 생각함
뭐 진지하게 풀기는 하겠는데
dp[자리수][마지막수] = 시그마(0~마지막수-1) dp[자리수-1][마지막수] 잖아?
솔직히 걍 산수문제
'''
import sys
input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    dp = [1] * 10

    for i in range(N-1):
        for j in range(10):
            dp[j] = sum(dp[j:])
    print(sum(dp))

