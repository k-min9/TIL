'''
연속된 수의 합 2를 곱해서 홀수인 약수의 갯수를 구하면 된다.
'''

N = int(input()) * 2
cnt = 0
for i in range(1, N+1):
    if N % i == 0 and i % 2 == 1:
        cnt = cnt + 1
print(cnt)

# 컴공적으로 틀린접근이다. 근데 N이 천만이 아니라 천오백만만 됐어도 이렇게 안 풀었음