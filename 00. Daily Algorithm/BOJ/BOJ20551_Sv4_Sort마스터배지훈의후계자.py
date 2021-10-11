'''
1.소트하고 O(NlogN)
2.쭉읽어서 딕셔너리로 만들고 O(N)
3.get하면 되지 않을까 O(1)
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(int(input()))

# 소트
arr.sort(reverse=True)

# 딕셔너리
find_dic = defaultdict(int)
for idx, value in enumerate(arr):
    find_dic[value] = N-1-idx

# 쿼리
for _ in range(M):

    answer = find_dic.get(int(input()))
    if answer == None: # get은 key가 없으면 None 반환
        answer = -1
    print(answer)


'''
메모리만 충분하면 이게 이분탐색보다 빠르다고 생각함
'''