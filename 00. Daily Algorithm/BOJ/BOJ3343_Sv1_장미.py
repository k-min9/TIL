'''
호랑이와 토끼의 발걸음 문제인가 그거다.
이건 왕복하지 않는 만큼 상냥한데 
호랑이와 토끼의 스텝을 둘 다 밟는 만큼 엄격하다.
스텝 종류가 셋이면 머리 좀 굴려야하겠지만 아닌 만큼 컴퓨터의 영역

1. 개당 가격 비교
2. 가성비 싼 쪽을 끝까지 구매했을때를 case 1
3. 가성비 싼 쪽 하나 덜 구매하고 남은 쪽을 가성비 비싼 쪽으로 구매하는게 case 2
4. 비교하고 끝

>>>>> 끝은 개뿔
이 밑에 코드 120줄 정도 있었다면 믿겠나. 다 지웠다.
가격 비교, 최소 공배수, 스왑 다 해봤는데 구멍 숭숭이라고 지적당했음.

결국 인간의 지성을 포기하고 1초 2천만번의 힘으로 풀었다. 
이 문제가 O(N)의 풀이가 성립한다면, 둘 중 한 쪽은 구매 제품수가 10^7 미만이라는거다. 
안 그러면 문제가 성립안하거나 O(logN)의 풀이가 필요함.
한 마디로 10^7번 돌리면 된다. 일단 A,B,C,D의 최대값인 1e5 넣음. 됨. ㅎㅎㅎㅎㅎㅎㅎ 풀이 찾습니다.
'''
import sys
input = sys.stdin.readline

# 이름에 너무 직관성이 없어서 멋대로 고치겠다.
N, num1, price1, num2, price2 = map(int, input().split())

# 최대 루프 수
max_num = 1e5

# 초기치 : 1번 풀매수
answer2 = ((N - 1) // num1 + 1) * price1

# 첫번째 제품 cnt개 강제 구매
cnt = 0
while(cnt <= max_num):    
    num = N - cnt * num1
    if num < 0:
        break
    answer3 = cnt * price1
    if num % num2 == 0:
        answer2 = min(answer2, answer3 + ((num//num2) * price2))
        break
    # 남은 물건 첫번째 제품으로 도배
    cnt = cnt + 1
    num = ((num - 1)//num2) + 1
    answer2 = min(answer2, answer3 + num * price2)

# 두번째 제품 cnt개 강제 구매
cnt = 0
while(cnt <= max_num):    
    num = N - cnt * num2
    if num < 0:
        break
    answer3 = cnt * price2
    if num % num1 == 0:
        answer2 = min(answer2, answer3 + ((num//num1) * price1))
        break
    # 남은 물건 첫번째 제품으로 도배
    cnt = cnt + 1
    num = ((num - 1)//num1) + 1
    answer2 = min(answer2, answer3 + num * price1)

print(answer2)

'''
사람이 머리가 나빠서 미치면 이렇게 됩니다.
머리가 대충 미니어처 로즈 당함
'''


'''
1차 시도 <<< 평범하게 틀림
# 이름에 너무 직관성이 없어서 멋대로 고치겠다.
N, num1, price1, num2, price2 = map(int, input().split())

# 1. 개당 가격 비교
# 개당 가격 0이 있을 경우, 0을 출력하고 exit >> A,B,C,D는 양의 정수였다.
# if price1 == 0 or price2 == 0:
#     print(0)
#     exit()
# 가성비가 같지만, 단위가 이쪽이 큼. 파이써ㅡ닉 스위치
if abs((price1/num1)-(price2/num2)) <= 1e-10 and num1 > num2:  # 우리는 파이썬식 비교
    num1, num2 = num2, num1
    price1, price2 = price2, price1 
elif price1/num1 > price2/num2:
    # 2가 쌈 -> 파이써ㅡ닉 스위치
    num1, num2 = num2, num1
    price1, price2 = price2, price1 

<미적용>
# N을 num1과 num2의 최소공배수로 나눈다. 그러면 N의 규모는 10^(5+5)까지 낮출수있다.
# lcm = num1 * num2 // math.gcd(num1, num2)
# answer = (N // lcm) * (lcm // num1) * price1
# N = N % lcm

# 2. 가성비 싼 쪽을 끝까지 구매
buy = (N - 1) // num1 + 1
answer = buy * price1
# 3. 가성비 싼 쪽을 하나 덜 구매 >> 적어도 num2를 하나 이상 구매하게 변경
N = N - num2  # 하나 강제 구매
if N < 0:
    print(answer)
    exit()
buy = (N - 1) // num1 + 1  #  그 이후 똑같이 구매
answer2 = buy * price1 + price2
answer = min(answer, answer2)

buy = buy - 1
buy = N - buy * num1
buy = ((buy - 1) // num2) + 1 
answer = min(answer, answer2 - price1 + price2 * buy)

#print('input', num1, price1, num2, price2)
print(answer)

이런 한 문장만 틀려도 삐끗하는 구현이 하면서 제일 살 떨린다.
#3. 부분이 문제였다. 근데 7 2 2 3 3 이 8 출력하는거 찾는데도 한참 걸림.
'''