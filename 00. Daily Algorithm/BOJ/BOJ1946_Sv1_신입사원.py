'''
대전제로 어떠한 점수던지 1등을 하면 그 사람은 뽑힌다.
그러면 그 사람의 다른쪽 점수보다 높은 사람은 전부 뽑힘. 
이거 면접 서류 각각 한 번만 해주면 된다.
-> 시간 초과

서류 순으로 정렬 한 후, 면접 순위가 기존의 최소치보다 높은지만 체크하면 O(N)
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores = sorted(scores)

    answer = 1
    score_min = scores[0][1]  # 서류 최강자의 면접 순위

    for i in range(1, N):
        if scores[i][1] < score_min:
            score_min = scores[i][1]
            answer += 1
    
    print(answer)
