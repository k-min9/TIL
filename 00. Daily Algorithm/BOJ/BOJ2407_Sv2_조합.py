'''
접근 : C로 풀면 귀찮은 오버플로우 문제. python은 상관없음
'''

#n combination m
n, m = map(int, input().split())

#정답과 나누는 수
answer = 1
i = 1

while (m):
    answer = answer * n
    answer = answer // i
    
    n = n - 1
    i = i + 1
    m = m - 1

answer = int(answer)
print(answer)