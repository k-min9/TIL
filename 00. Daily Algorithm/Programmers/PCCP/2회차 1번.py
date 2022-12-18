MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(commands):
    answer = [0, 0]
    move = 0
    for command in commands:
        if command == 'G':
            answer[0] += MOVES[move][0]
            answer[1] += MOVES[move][1]
        elif command == 'B':
            answer[0] += MOVES[(move+2)%4][0]
            answer[1] += MOVES[(move+2)%4][1]
        elif command == 'R':
            move = (move + 1) % 4
        elif command == 'L':
            move = (move - 1) % 4
            
    return answer

# [2, 2]
print(solution("GRGLGRG"))

# [2, 0]
print(solution("GRGRGRB"))
