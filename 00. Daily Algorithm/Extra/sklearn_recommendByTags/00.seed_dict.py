from random import randint

a_01={2:1,3:2,4:3}

for x in range(10,100):
    answer = 'a_'
    answer += str(x)
    answer += '={'
    for i in range(1, randint(3,5)):
        dist = 5
        answer += str(randint((i-1)*dist+1, i*dist))
        answer += ':'
        answer += str(randint(1,5))
        answer += ', '
    answer = answer[:-2]
    answer += '}'

    print(answer)
