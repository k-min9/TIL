def solution(matrix):
	answer = []
	coords = func_b(matrix)
	nums = func_a(matrix)

	matrix[coords[0][0]][coords[0][1]] = nums[0]
	matrix[coords[1][0]][coords[1][1]] = nums[1]
	if func_c(matrix):
		for i in range(0, 2):
			answer.append(coords[i][0] + 1)
			answer.append(coords[i][1] + 1)
			answer.append(nums[i])
	else:
		matrix[coords[0][0]][coords[0][1]] = nums[1]
		matrix[coords[1][0]][coords[1][1]] = nums[0]
		for i in range(0, 2):
			answer.append(coords[1-i][0] + 1)
			answer.append(coords[1-i][1] + 1)
			answer.append(nums[i])
	return answer
