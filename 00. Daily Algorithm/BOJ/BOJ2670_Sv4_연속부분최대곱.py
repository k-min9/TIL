'''
DP요? 이럴때 카데인 알고리즘 안쓰면 손해!
'''
import sys
input = sys.stdin.readline

N = int(input())
cur = 1
answer = 1
max_num = 0
for _ in range(N):
    num = float(input())
    max_num = max(num, max_num)

    cur = max(num, cur*num)
    answer = max(answer, cur)

if answer > 1:
    print("{:.3f}".format(answer))
else:
    print("{:.3f}".format(max_num))

'''
시간복잡도는 DP와 동일하지만 리스트가 하나도 필요없다. 공간복잡도 O(1)
'''