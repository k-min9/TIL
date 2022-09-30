'''
간단한 구현
가까울수록 밑에 있을수록 좋다.
'''
import sys
input = sys.stdin.readline

for i in range(int(input())):
    # 호텔 층 수 , 각층 방 수 X번째 손님
    h, w, n = map(int, input().split())
    floor = 0
    ho = 0
    if n % h == 0:
        floor = h * 100
        ho = n // h
    else:
        floor = (n % h) * 100
        ho = 1 + n // h
    
    # 방 번호 = 층 + 호
    print(floor + ho)
