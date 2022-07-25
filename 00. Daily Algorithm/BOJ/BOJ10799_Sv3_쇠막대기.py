'''
아마 SWEA에서 이때쯤에 이정도 문제를 풀었다고 생각함.
스택을 쓰는 문제에서 나는 스택을 쓰지 않고 플래그로 해결했다.
'''
import sys
input = sys.stdin.readline

cases = input().rstrip()

answer = 0
points = 0
shot = 0
new = 0

for case in cases:
    if case == '(':
        shot = 1
        points = points + 1
        new = new + 1
    else:
        points = points - 1
        if shot == 1:
            shot = 0
            new = new - 1
            answer = answer + points

print(answer + new)

'''
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 여전하네 나.

공간복잡도랑 속도봐라.
지금도 생각없이 배웠다고 스택 쓰는건 그냥 생각을 멈춘거라고 생각한다.
여러모로 감회가 새로운 문제
'''