def solution(n):
	answer = 0
	primes = [2]
	for i in range (3, n + 1, 2) :
		is_prime = True
		for j in range(2, i) :
			if i % j == 0 :
				is_prime = False
				break
		if is_prime:
			primes.append(i)

	prime_len = len(primes)
	for i in range(0, prime_len - 2) :
		for j in range(i + 1, prime_len - 1) :
			for k in range(j + 1, prime_len) :
				if primes[i] + primes[j] + primes[k] == n :
					answer += 1
	return answer
