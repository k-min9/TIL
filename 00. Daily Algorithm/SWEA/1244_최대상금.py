import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    # 숫자, 교환 횟수
    nums, K = input().split()
    N = len(nums)
    K = int(K)

    now = set([nums])
    next = set()

    for _ in range(K):
        for s in now:
            s = list(s)
            for i in range(N):
                for j in range(i+1, N):
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now = next
        next = set()

    print(f'#{t+1}', max(map(int, now)))
