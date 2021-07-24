'''
접근 : 자리수 십만. 이건 밀어 붙이면 타임 아웃일것 같다...만
숫자 자리수까지 리스트 쌓고, 거기서부터 하면?
'''

import sys
input = sys.stdin.readline

answer = 0
n, d = map(int, input().split())
for i in range(1, n+1):
    answer = answer + str(i).count(str(d))

print(answer)

'''
아니 이게 왜 됨???????????????
count 시간 복잡도 O(1)이라도 됨??????? O(n)아니고?????
안되면 소트하고 보텀업,탑다운하고
그래도 안되면 캐싱해서 거기서부터 연산하려고 했는데

인터넷 찾아보니까 시간복잡도 O(n)맞다 그럼 O(n^2)인데 왜 통과 되었는지 지금도 의문
'''