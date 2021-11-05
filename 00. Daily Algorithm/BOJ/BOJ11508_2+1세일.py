'''
산수 데이??? 쭉 세워서 3 6 9 하는 느낌으로 팡팡 쳐버리면 됨
'''
import sys
input = sys.stdin.readline

answer = 0
for idx, cost in enumerate(sorted([int(input()) for _ in range(int(input()))], reverse=True)):
    if idx % 3 != 2: answer += cost
print(answer)

'''
한번 숏코딩 의식해봤는데... 위에는 위가 있었다.
'''