'''
1줄 수정 : 14번째 줄 : vote_counter[idx] > idx로
'''
def solution(N, votes):
	vote_counter = [0 for i in range(N+1)]
	for i in votes:
		vote_counter[i] += 1

	max_val = max(vote_counter)

	answer = []
	for idx in range(1, N + 1):
		if vote_counter[idx] == max_val:
			answer.append(idx)
	return answer