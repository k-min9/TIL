'''
N 5000 K 5000
그럼 사람처럼 풀면 된다.
'''

# 사람 수, 제거 단위
N, K = map(int,input().split())

mans = [i for i in range(1,N+1)]

result = []

kill = K -1   # 0번 인덱스부터 출발
while True:  
    result.append(mans.pop(kill))  # 다 죽을때까지 뽑아낸다
    if not mans:
        break  # 전멸 체크
    kill = (kill + K - 1) % len(mans) # 본인이 빠지면서 인덱스 조절 되서 K-1

print('<'+', '.join(map(str,result))+'>')

'''
왜 이게 한시간 가까이 걸리지 orz
'''