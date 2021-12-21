'''
위상정렬 문제
'''
import sys
input = sys.stdin.readline

# 건물 종류, 건물 관계 수, 쿼리 수
N, M, K = map(int, input().split())

graphs = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
build = [0] * (N + 1)

failure = False

# 입력
for i in range(M):
    first, second = map(int, input().split())
    graphs[first].append(second)
    indegree[second] += 1

# 쿼리
for i in range(K):
    method, number = map(int, input().split())

    # 건설
    if method == 1:
        # 건설 실패
        if indegree[number] != 0:
            failure = True
            break

        # 종류 증가
        build[number] += 1

        # 첫 건설
        if build[number] == 1:
            for second in graphs[number]:
                indegree[second] -= 1
    # 파괴
    else:
        # 파괴 실패
        if build[number] <= 0: # 건설 된 것이 없으면 파괴를 할 수 없다.
            failure = True
            break

        build[number] -= 1

        # 마지막 빌딩
        if build[number] == 0: # 개수가 0개가 되면 관련된 건물들을 못 짓게 해줘야한다.
            for second in graphs[number]:
                indegree[second] += 1

if failure:
    print("Lier!")
else:
    print("King-God-Emperor")