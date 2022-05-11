'''
문자열길이 300만 => (O(N))
투포인터 전진
'''

import sys
 
words = sys.stdin.readline().strip()

# l, r의 위치까지 k를 몇개 가지고 있는지!
lk = []
rk = []
cnt = 0
for i in words:
    if i == 'K':
        cnt += 1
    else:
        lk.append(cnt)

cnt = 0
for i in words[::-1]:
    if i == 'K':
        cnt += 1
    else:
        rk.append(cnt)
rk.reverse()

l, r = 0, len(lk) - 1
ans = 0
while l <= r:
    # r-l+1은 R의 개수, 2*~ : R의 양끝에 존재하는 K의 개수
    ans = max(ans, r - l + 1 + 2 * min(lk[l], rk[r]))
    if lk[l] < rk[r]:
        l += 1
    else:
        r -= 1
print(ans)
