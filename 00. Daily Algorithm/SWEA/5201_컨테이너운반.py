import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # 컨테이너 수, 트럭 수
    N, M = map(int, input().split())
    # 화물 무게, 적재용량
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    answer = 0
    next = 0
    for i in range(M):
        for j in range(next, N):
            if t[i] >= w[j]:
                answer += w[j]
                next = j + 1
                break

    print(f'#{tc+1}', answer)
