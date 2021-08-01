# https://leetcode.com/problems/daily-temperatures
# 풀이 1: 스택을 이용해서 내림차순 정렬
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택값보다 높으면 거기서 날짜 쓰고 갱신
        while stack and cur>temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

        print('1', stack)
        
    return answer

print(dailyTemperatures([73,74,75,71,69,72,76,73]))