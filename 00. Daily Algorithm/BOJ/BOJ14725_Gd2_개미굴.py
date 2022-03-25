'''
단어 - 트라이라는건 알겠는데
'''
import sys
input = sys.stdin.readline

N = int(input())
ant = {}

# 사전순 나열
def getResult(t, i):
    target_key = sorted(t.keys())
    for s in target_key :
        print('--'*i + s)
        getResult(t[s],i+1)

# 트라이
for i in range(N):
    name = list(input().split())
    target_dict = ant
    for j in name[1:]:
        if j not in target_dict:
            target_dict[j] = {}
        target_dict = target_dict[j]

# 출력
getResult(ant,0)

'''
예술이네
'''