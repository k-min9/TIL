'''
곱하는 대상이 바뀜
(n % multi_day) * multi_day_price + (n // multi_day) * one_day_price -> multi_day_price, one_day_price 위치 변경
'''
def solution(one_day_price, multi_day, multi_day_price, n):
	if one_day_price * multi_day <= multi_day_price:
		return n * one_day_price
	else:
		return (n % multi_day) * one_day_price + (n // multi_day) * multi_day_price
	