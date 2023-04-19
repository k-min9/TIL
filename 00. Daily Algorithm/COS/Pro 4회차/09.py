def solution(hour, minute):
	answer = ''
	
	hour = hour % 12
	hour_angle = 30*hour + 0.5*minute
	
	minute_angle = 6 * minute
	
	answer = abs(hour_angle - minute_angle)
	
	return "{:.1f}".format(answer)

