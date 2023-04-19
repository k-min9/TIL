import math

def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i: 
			return False
	return True

def solution(a, b):
	answer = 0
	for i in range(math.ceil(pow(a, 1/2)), math.floor(pow(b, 1/2)) + 1):
		if isPrime(i):
			answer += 1
	for i in range(math.ceil(pow(a, 1/3)), math.floor(pow(b, 1/3)) + 1):
		if isPrime(i):
			answer += 1
	
	return answer