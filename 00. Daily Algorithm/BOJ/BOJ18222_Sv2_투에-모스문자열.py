'''
k <= 10**18 : 니가 처음 생각한대로 풀지마시오 내지 O(logN)
'''
import sys
input = sys.stdin.readline


# 재귀
def calc(k):
    if k == 0:
        return 0
    else:
        # 문자열 위치
        n = 0
        while (k >= 2**n):
            n += 1
        return 1 - calc(k-2**(n-1))


# 입력
k = int(input()) - 1
print(calc(k))

'''
아늬 이거 그냥 산수문제잖아...
'''