'''
토끼 용서 못해 ㅡㅡ
'''
# 당근 종류, 총 재배일
N, T = map(int, input().split())

# 당근 맛, 영양제
points = list()

answer = 0
for _ in range(N):
    p, a = map(int, input().split())
    points.append((a, p))
    answer += p

points.sort(reverse=True)

for p, a in points:
    T -= 1
    answer += p*T

print(answer)



'''
영양제>원본. 이거 때문에 엄청 쉽다. 
T일에 가장 잘 키워진 당근 앞에 있다가 배부른 토끼에게 샷건을 먹이면 된다.
'''