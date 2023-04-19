from itertools import permutations
def solution(card, n):
	answer = 0
	cards = []
	card.sort()
	
	for comb in permutations(card, len(card)):
		cards.append(''.join(list(map(str, comb))))
	
	for c in cards:
		answer += 1
		if c == str(n):
			break
	else:
		answer = -1
	
	return answer
