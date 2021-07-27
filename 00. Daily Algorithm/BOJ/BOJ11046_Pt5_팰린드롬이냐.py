'''
From BOJ13275.
매내처, 마나허, 마나커 뭔지는 모르겠지만 그걸 배워야 풀 수 있댄다.
그럼 배우면 되지.
https://technote-mezza.tistory.com/78
https://www.crocus.co.kr/1075
https://blog.naver.com/jqkt15/222108415284  << 추천
'''

'''
Manacher's Algorithm (마나커 알고리즘), 시간복잡도 O(N)
1. i는 0부터 N-1까지 진행된다.
2. j<i인 모든 j에 대해 r = max(r, j+P[j])를 만족하는 r을 구한다. 이때의 j값을 c라고 한다. c: center, r: radius
3. P(i)에 관한 식이다. P[i]란 i번째 문자를 중심으로 하는 가장 긴 팰린드롬의 반지름이다.
3-1. r<i일 경우, P[i] = 0이다.
3-2. 그외의 경우, P[i] = min(P[2*c-i], r-i)이다.
4. S[i - P[i]] == S[i + P[i]]일때까지 P[i]를 1씩 증가시킨다.
5. 팰런드럼 부분 문자열의 길이가 짝수일 경우를 위해 저 작업 전에 모든 문자사이와 앞 뒤에 현재 포함되어있지 않은 문자열을 더한다.(보통 #)
내는게 반지름이고 #을 끼웠으니 곱하기 2 나누기 2로 그 숫자가 팰린드롬의 길이가 된다.
'''
# 전처리 
import sys
input = sys.stdin.readline

def manacher(string):
    P = [0] * len(string)  # 예시 설명에 맞게 대문자 쓰도록 하겠다.
    c = 0  # 중심점(center) 초기화
    r = 0  # 시작점에서 가장 먼 반경

    for i in range(0, len(string)):
        #초기 시작점을 쉽게 잡을 수 있다는 거고 밑에서 보다시피 어차피 한계까지 키움
        if r < i :
            P[i] = 0
        else:
            P[i] = min(P[(2*c) - i], r - i)

        # 이부분은 BOJ16161 LIS 팰린드롬의 Ad-Hoc 버전 풀이 생각하면 이해가 빠르다.
        while(i-P[i]-1>=0 and i+P[i]+1 < len(string) and string[i-P[i]-1] == string[i+P[i]+1]): 
            P[i] = P[i] + 1

        if (r < i + P[i]):
            r = i + P[i]
            c = i
    return P

# 수열 정보
N = int(input())
numbers = list(map(int, input().split()))
numbersM = ['#']
for number in numbers:
    numbersM.append(number)
    numbersM.append('#')

P = manacher(numbersM)

# 슬라이스 정보
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    # 2번 5번을 슬라이스 했으면 인덱스가 각각 2*2-2=2, 2*5=10이 되어 mid가 (2+10)//2인 6이된다.
    # 진짜 알기 쉽게 풀어서 mid에서의 반지름 값이 문자열의 반값인 E-S+1 값보다 크면 펠런드럼의 일부이다.
    if S+E-1 + P[S+E-1] >= 2*E:
        print(1)
    else:
        print(0)