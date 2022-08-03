'''
내용물이 변한다! 세그먼트 트리!
최근 푼 구간합구하기(2042)와 매우 유사한 문제
'''
import sys
input = sys.stdin.readline

# 상수
MOD = 1000000007

# 세그먼트 트리 생성
def init(node, start, end): 
    # node가 leaf 노드인 경우 배열의 원소 값을 반환.
    if start == end :
        tree[node] = nums[start]
        return tree[node]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node*2, start, (start+end)//2) * init(node*2+1, (start+end)//2+1, end)
        return tree[node]

# 구간 곱 구하기
# node가 담당하는 구간 [start, end]
# 곱을 구해야하는 구간 [left, right]
def subMul(node, start, end, left, right) :
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.    
    if left > end or right < start :
        return 1

    # 구해야하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적이다. (애초에 중복연산)
    if left <= start and end <= right :
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야한다.
    return subMul(node*2, start, (start+end)//2, left, right) * subMul(node*2 + 1, (start+end)//2+1, end, left, right) % MOD


def update(node, start, end, index, value) :
    if index < start or index > end :
        return

    # 리프 노드
    if start == end:
        tree[node] = value
        return
    
    update(node*2, start, (start + end)//2, index, value)
    update(node*2+1, (start + end)//2 + 1, end, index, value)

    tree[node] = tree[node*2] * tree[node*2+1] % MOD



# 수의 개수, 변경 횟수, 쿼리 수
N, M, K = map(int, input().rstrip().split())
nums = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

init(1, 0, N-1)

for _ in range(M+K) :
    # a는 쿼리 종류 : 1이 변경 / 2가 합 출력
    a, b, c = map(int, input().rstrip().split())

    if a == 1 :
        b = b-1
        update(1, 0, N-1, b, c)
        nums[b] = c
    elif a == 2 :                
        print(int(subMul(1, 0, N-1 ,b-1, c-1)))

'''
곱하기 0 때문에 계산할때 전부 새로 갱신해줘야 한다.
워메
'''