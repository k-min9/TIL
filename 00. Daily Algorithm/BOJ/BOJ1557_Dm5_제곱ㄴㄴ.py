'''
오늘의 학습 내용 : 뫼비우스 함수
뫼비우스 함수 : 정수가 제곱 인수가 없는 정수인지 여부에 따라 분류하는 곱셈적 함수 (notation : mu(n), 제곱인수가 있는 정수 0 아닐 경우 (-1)^소인수 수)
곱셈적 함수 : gcd(m,n) = 1인 m,n에 대하여 f(mn) = f(m)*f(n)이 성립하는 함수
n       1 2 3 4 5 6 7 8 9 10
mu(n)   1 -1 -1 0 -1 1 -1 0 0 1
참조 : 
https://peisea0830.tistory.com/53 (왠일로 예시가 파이썬)
https://algospot.com/wiki/read/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_%EB%8C%80%ED%9A%8C%EC%97%90_%ED%95%84%EC%9A%94%ED%95%9C_%EC%88%98%ED%95%99
'''
import sys
input = sys.stdin.readline

# MAX가 200001인 이유는 최대 인풋의 제곱근보다 크기 때문이다
MAX = 200001

# mo : 뫼비우스 배열
mo = [0] * MAX
mo[1] = 1

# 뫼비우스 함수 생성(위키 생성함수에 1 대입)
for i in range(1, MAX):
    j = 2 * i
    while j < MAX:
        mo[j] -= mo[i]
        j += i

# 체치기 + 1부터 num까지의 제곱ㄴㄴ수의 갯수를 리턴하는 함수 + 뫼비우스 함수로 이걸 빼는지 더하는지 냅두는지 판단한다.
def found(num):
    res = 0
    for i in range(1, int(num ** 0.5) + 1):
        res += mo[i] * (num // (i * i))
    return res

n = int(input())
left = 1
right = 20000000000

# 이분탐색
while left < right:
    mid = (left + right) // 2
    now = found(mid)
    if now < n:
        left = mid + 1
    elif now > n:
        right = mid - 1
    else:
        right = mid

# 정답출력
print(left)

'''
이거보다 훨씬 무식하게 체 치면 끝날 문제 같은데...
진짜 조금 비튼게 8464 제곱 ㅇㅇ수
'''


