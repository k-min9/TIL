def solution(enemies, armies):
	answer = 0
	enemies.sort(reverse = True)
	armies.sort(reverse = True)
	
	while armies and enemies:
		if armies[-1] >= enemies[-1]:
			enemies.pop()
			armies.pop()
			answer += 1
		else:
			enemies.pop()		
		
	return answer
