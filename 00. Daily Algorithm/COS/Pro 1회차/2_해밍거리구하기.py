'''
아직 빈칸 채우기. 더럽게 구현 못했지만 참자
'''
def func_a(string, length):
	padZero = ""
	padSize = len(string)
	for i in range(padSize):
		padZero += "0"
	return padZero + string

def solution(binaryA, binaryB):
	max_length = max(len(binaryA), len(binaryB))
	binaryA = func_a(binaryA, max_length)
	binaryB = func_a(binaryB, max_length)

	hamming_distance = 0
	for i in range(max_length):
		if binaryA[i] != binaryB[i]:
			hamming_distance += 1
	return hamming_distance