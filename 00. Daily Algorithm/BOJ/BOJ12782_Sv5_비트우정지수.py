'''
XOR 쓰고 몸도 풀고
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()

    ans = abs(a.count('1') - b.count('1'))
    cnt = 0
    for i in range(len(a)):
        # 둘이 같지 않음
        if int(a[i])^int(b[i]):
            cnt += 1
    ans = (cnt - ans)//2 + ans
    print(ans)