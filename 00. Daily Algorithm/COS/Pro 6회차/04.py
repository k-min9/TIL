'''
card_b[i]를
card_b[i-n//2] = card[i]로
'''
def solution(n, mix, k):
	answer = 0
	card = [_ for _ in range(1, n+1)]
	while mix != 0:
		mix = mix - 1
		card_a, card_b = [0 for _ in range(n//2)], [0 for _ in range(n//2)]
		for i in range(0, n):
			if i < n//2:
				card_a[i] = card[i]
			else:
				card_b[i-n//2] = card[i]
		for i in range(0, n):
			if i % 2 == 0:
				card[i] = card_a[i//2]
			else:
				card[i] = card_b[i//2]
	answer = card[k-1]
	return answer