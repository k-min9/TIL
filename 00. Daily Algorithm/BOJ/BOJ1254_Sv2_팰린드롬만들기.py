'''
단순하다 
앞부분을 깎으면서 남은 부분이 팰린드롬이 되면 그 전까지의 글자 수가 정답이다.
이게 실버2???인 이유는 모르겠는데 아마도 컴퓨터적 구현이겠지
'''
import sys
input = sys.stdin.readline

words = input().rstrip()
for i in range(len(words)):
    if words[i:] == words[i:][::-1]:
        print(len(words)+i)
        break

'''
추가해야되는 문자수인 줄 알았던데 살짝 버벅인거 빼고는 1분컷
'''