'''
방향은 중요하지 않고 오직 길이만 체크
서브태스크 성능 필요해보이는 문제로 보이지만
실버4라 구현만 하면 일단 통과
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().strip().split())
    arr.append([x, y])


arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
for i in range(N):
    if i == 0:  # 처음
        cnt += arr[i+1][0] - arr[i][0]
    elif i == N-1:  # 마지막
        cnt += arr[i][0] - arr[i-1][0]
    # 일반
    else:
        if arr[i][1] == arr[i+1][1] and arr[i][1] == arr[i-1][1]:
            cnt += min(arr[i+1][0] - arr[i][0], arr[i][0] - arr[i-1][0])
        elif arr[i][1] == arr[i+1][1]:
            cnt += (arr[i+1][0] - arr[i][0])
        elif arr[i][1] == arr[i-1][1]:
            cnt += (arr[i][0] - arr[i-1][0])

print(cnt)
