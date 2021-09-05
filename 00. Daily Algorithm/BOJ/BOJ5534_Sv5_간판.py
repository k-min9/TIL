'''
숫자가 작은 브루트포스
'하나의 오래된 간판에서 만들 수 있는 방법이 여러 개인 경우에도 만들 수 있는 간판은 하나이다.'
없었으면 DP행이었다.
'''
     
import sys
input = sys.stdin.readline


def chk(i):
    #간격
    dist = 0
    while True:
        dist+=1
        flag = False
        for j in range(1,name_len):  
            if dist*j + i < words_len:
                if words[dist*j + i] == name[j]:
                    flag = True
                else:
                    flag = False
                    break
            else:
                # 타임 아웃까지 일치하는 간판 없었음
                return False
        if flag:
            return True

N = int(input())
name = input().rstrip()
name_len = len(name)
answer = 0
for _ in range(N):
    words = input().rstrip()
    words_len = len(words)

    for i, w in enumerate(words):
        # 간판 만들수 있는지 여부
        if w == name[0] and chk(i):
            # print('c', i, words)
            answer += 1
            break

print(answer)
