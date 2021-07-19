'''
접근 : 
all or nothing 배낭채우기 게임인건 아는데 정확히 풀 줄 몰랐음.
자세한 알고리즘은 
https://www.youtube.com/watch?v=rhda6lR5kyQ
https://www.youtube.com/watch?v=A8nOpWRXQrs 
에서 공부함
'''

n, limit = map(int, input().split()) #과목수, 제한 시간

# 기초 정보 input
time = []
score = []
for i in range(n):
    t, s = map(int, input().split())
    time.append(t)
    score.append(s)

def knapsack(idx,L,l,answer): #과목인덱스, 리미트제한, 리미트, 총점수
    if idx < 0 or L < 0:
        return 0
    
    if l[idx] > L:
        return knapsack(idx-1, L, l , answer)
    else:
        left = knapsack(idx-1, L, l , answer)
        right = knapsack(idx-1, L - l[idx], l , answer)
        return max(left, answer[idx] + right)


ans = knapsack(n-1, limit, time, score)
print(ans)

'''
감상 : 
좋아했더니 결과는 시간초과였음. ㄲㅂ.
탑다운도 바텀업도 O(n)은 같을테고, 
접근 자체를 바꾸거나 획기적으로 변하지 않는 한 큰 시간단축은 없을 듯해서
푸는건 여기까지 하고 다음 문제로 가기로 했다.
'''