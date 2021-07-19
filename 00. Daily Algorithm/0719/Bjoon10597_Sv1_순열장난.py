'''
접근 : N은 쉽게 구할수 있다. 근데 안쓰는 법도 있을것 같다.
키워드 백트래킹. 근데 백트래킹 안쓰는 풀이도 있을것 같다. 
죄다 나중에 생각해보고, 일단 시키는대로 풀어보자.
답은 하나만 나와도 되니까, 쭉 밀어서 죄다 방문 visit chk 전부 통과하면 넘기는 식으로
'''

datas = input()

#최대 인덱스 N
n = max(len(datas)-9, 0)//2 + min(len(datas),9)
max_idx = len(datas)

chk = [0]*51 #list index out of range 수정

def backtrack(idx, num, answer): #참조 인덱스, 현재 번호, 정답

    global flag

    # 이미 찾음
    if flag:
        return

    # 목표 도달
    if idx == max_idx and num == n:
        flag = True
        answer = answer[:-1]
        print(answer)

    #탐색 1자리
    if idx < max_idx:
        i = int(datas[idx]) #잘라낸 1자리 번호     
        if not chk[i]:
            chk[i] = 1
            backtrack(idx+1, num+1, answer + str(i) + ' ') # 재귀
            chk[i] = 0 # 돌아왔을때 대비해서 초기화

    #탐색 2자리
    if idx < max_idx - 1:
        i = int(datas[idx:idx+2]) #잘라낸 2자리 번호
        if i<= n and not chk[i]: #list index out of range 수정
            chk[i] = 1
            backtrack(idx+2, num+1, answer + str(i) + ' ')
            chk[i] = 0

flag = False
answer = ''
ans = backtrack(0,0,answer)


'''
엉뚱한 감상 : 이거 chk 안써도 set이랑 list랑 len 비교하면 되지 않았을까
'''