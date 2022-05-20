'''
LIS??
'''
import sys
input = sys.stdin.readline

def count(arr):
    cnt = 1
    max_cnt = 0
    for i in range(1,N):
        if arr[i-1] <= arr[i]:
            cnt += 1
        else:
            max_cnt = max(cnt,max_cnt)
            cnt = 1
    max_cnt = max(cnt,max_cnt)
    return max_cnt

N = int(input())
if N==1:
    print(1)
    exit()
arr = list(map(int, input().split()))
length1 = count(arr)
arr.reverse()
length2 = count(arr)
print(max(length1,length2))
