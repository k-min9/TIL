'''
dp 바텀 업으로 숫자를 갱신하면 가장 최소의 합으로 구하는 법을 할 수 있지
'''
n = int(input())
dp = [0] * (n+1)
square = [i * i for i in range(1, int(100000 ** 0.5))]

for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
    
print(dp[n])
