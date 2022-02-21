'''
아침을 여는 상큼한 DP
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    # 마지막을 1에서 선택
    dp1 = [0] * (N+1)
    dp2 = [0] * (N+1)
    dp1[1] = nums1[0]
    dp2[1] = nums2[0]

    for i in range(1, N):
        dp1[i+1] = max(dp2[i-1], dp2[i], dp1[i-1]) + nums1[i]
        dp2[i+1] = max(dp1[i-1], dp1[i], dp2[i-1]) + nums2[i]

    print(max(dp1[N], dp2[N]))


'''
RGB 계열 DP는 왜케 인상이 깊을까
'''


