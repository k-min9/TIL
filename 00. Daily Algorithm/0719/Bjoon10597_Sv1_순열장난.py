'''
접근 : N은 쉽게 구할수 있다. 근데 안쓰는 법도 있을것 같다.
키워드 백트래킹. 근데 백트래킹 안쓰는 풀이도 있을것 같다. 
죄다 나중에 생각해보고, 일단 시키는대로 풀어보자.
답은 하나만 나와도 되니까, 쭉 밀어서 죄다 방문 visit chk 전부 통과하면 넘기는 식으로
'''

num = input()

#최대 인덱스 N
n = max(len(num)-9, 0)//2 + min(len(num),9)

def BT(idx, answer):

    if idx == n:
        return answer