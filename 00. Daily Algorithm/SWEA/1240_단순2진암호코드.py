import sys
sys.stdin = open('input.txt')

# 코드
codes = {'0001101': 0,
         '0011001': 1,
         '0010011': 2,
         '0111101': 3,
         '0100011': 4,
         '0110001': 5,
         '0101111': 6,
         '0111011': 7,
         '0110111': 8,
         '0001011': 9, }


for t in range(int(input())):
    # 줄과 가로 길이
    N, K = map(int, input().split())
    nums_list = [input().rstrip() for _ in range(N)]

    for i in range(N):
        nums = nums_list[i]
        if '1' in nums:
            nums = nums[::-1]
            for i in range(K):
                if nums[i] == '1':
                    nums = nums[i:i+56]
                    break

            # 효율이고 자시고 거꾸로 치기 귀찮음
            nums = nums[::-1]
            nums_odd = list()
            nums_odd.append(codes[nums[:7]])
            nums_odd.append(codes[nums[14:21]])
            nums_odd.append(codes[nums[28:35]])
            nums_odd.append(codes[nums[42:49]])
            nums_even = list()
            nums_even.append(codes[nums[7:14]])
            nums_even.append(codes[nums[21:28]])
            nums_even.append(codes[nums[35:42]])
            nums_last = codes[nums[49:56]]

            if (3*sum(nums_odd) + sum(nums_even) + nums_last) % 10 == 0:
                print(f'#{t+1}', sum(nums_odd) + sum(nums_even) + nums_last)
            else:
                print(f'#{t+1}', 0)
            break
