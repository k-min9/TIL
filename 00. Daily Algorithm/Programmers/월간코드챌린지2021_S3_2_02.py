def solution(n, left, right):
    answer = []
    
    x = left%n
    y = left//n
    
    for _ in range(right-left+1):
        if x<=y:
            answer.append(y+1)
        else:
            answer.append(x+1)
        x+=1
        if x==n:
            x=0
            y+=1
            
    return answer

print(solution(3, 2, 5))
'''
좌표마다 체크해서 넣기
'''