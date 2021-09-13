'''
비트연산 연습
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    a, b = input().split()
    for i in range(len(a)):
        # 둘이 같지 않음
        if not int(a[i])^int(b[i]):
            cnt += 1
    print(cnt)