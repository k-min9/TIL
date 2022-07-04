'''
첫 전구를 키는 것과 키지 않는 것 둘로 나뉜다고 한다.
이걸 어케 생각해내지;; 다음부터 이런 타입 접근 방식이 하나 늘었다.
'''
import sys
input = sys.stdin.readline

n = int(input())
now = list(map(int, input().rstrip())) 
target = list(map(int,input().rstrip())) 

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

def switch(now, cnt):
    count = cnt
    if count == 1:
        now[0] = change(now[0])
        now[1] = change(now[1])
    for i in range(1, n):
        if now[i-1] != target[i-1]:
            count += 1
            now[i-1] = change(now[i-1])
            now[i] = change(now[i])
            if i != n-1:
                now[i+1] = change(now[i+1])
    if now == target:
        return count
    else:
        return -1

res1 = switch(now[:], 0)
res2 = switch(now[:], 1)
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1>=0 and res2 < 0:
    print(res1)
elif res1 <0 and res2 >= 0:
    print(res2)
else:
    print(-1)
