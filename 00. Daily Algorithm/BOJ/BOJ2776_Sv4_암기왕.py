'''
접근 : set의 in이 O(1)인거 알고 있냐고 묻는거 아님?
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 테스트 대상
    N = int(input())
    tests = set(map(int, input().split()))
    # 쿼리
    M = int(input())
    queries = list(map(int, input().split()))

    for query in queries:
        if query in tests:
            print(1)
        else:
            print(0)