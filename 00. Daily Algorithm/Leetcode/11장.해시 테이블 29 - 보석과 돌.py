# https://leetcode.com/problems/jewels-and-stones
# 풀이 4: 파이써닉 다운 풀이


def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum(stone in jewels for stone in stones)



# 예ㅡ술적이긴하네
# sum [True, True, False, False] 같은 느낌으로 해결