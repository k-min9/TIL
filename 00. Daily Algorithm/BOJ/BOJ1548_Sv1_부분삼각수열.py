'''
접근 : 선택 수열을 오름차순 정렬시 수열의 0번째와 1번째의 합이 가장 마지막 수 보다 크면 그 사이에 뭐가 들어와도 전부 성립한다.
N : 50 => 완전탐색해라
'''
import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.sort()


if N>2:
    answer = -1
    for start in range(N-2):
        for end in range(N-1, start+1, -1):
            if nums[start] + nums[start+1] > nums[end]:
                answer = max(answer, end-start+1)
    
    # 조건 만족하는 배열이 없었음 => 그냥 두개가 답
    if answer == -1:
        print(2)
    else:
        print(answer)
else:
    print(N)