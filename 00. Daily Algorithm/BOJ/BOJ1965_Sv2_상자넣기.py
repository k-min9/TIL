# 이거 가장 긴 LIS아님???

n = int(input())
s = list(map(int, input().split()))
dp = [1]
for i in range(1, n):
    d = []
    for j in range(i):
        if s[i] > s[j]:
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))