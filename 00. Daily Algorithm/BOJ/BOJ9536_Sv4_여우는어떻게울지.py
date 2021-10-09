'''
노래방 가면 부르는 노래;;;
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    words = input().split()
    check_list = set()
    
    # 쿼리 모음
    while True:
        query = input().rstrip()
        if query == 'what does the fox say?':
            break
        check_list.add(list(query.split())[2])

    # 정답 출력
    answers = list()
    for word in words:
        if word not in check_list:
            answers.append(word)
    print(*answers)

'''
replace나 split 쓰니까 pow의 ow를 빼가서 p만 남고 그럼... 맹점이었다;;
'''