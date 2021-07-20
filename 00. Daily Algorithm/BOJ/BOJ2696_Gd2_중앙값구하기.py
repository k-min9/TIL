'''
키워드 : 자료구조, 우선순위 큐
아마 시간 초과로 끝장내는 타입인거 같은데...
자료구조 안쓰고도 통과하고 있는 것 같아서 일단 ㄱㄱ
'''

n = int(input())

for _ in range(n):
    m = int(input())

    # 적재
    lists = []

    for _ in range((m+9)//10):
        lists.extend(list(map(int,input().split())))

    #출력

    print(len(lists)//2 + 1)

    for i in range((m//2) + 1):
        slists = sorted(lists[:2*i+1])
        if (i+1)%10 != 0:
            print(slists[i], end = " ")
        else:
            print(slists[i])

'''
감상 : 
시간 2756ms 나왔다.
다른사람들 84 96ms 나온거 봐서는 이거는 나중에 다시 풀어야할 듯
'''