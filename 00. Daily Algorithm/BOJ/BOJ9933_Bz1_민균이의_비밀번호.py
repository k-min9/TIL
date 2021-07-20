'''
접근 : 
1. 전부 리스트에 넣고 
2. for로 내용물 뽑아서
3. 대차대조하다가 빙고 뽑으면 종료
'''

n = int(input()) #파워 친절
texts = [] #리스트 생성

#1. 전부 리스트에 넣고
for _ in range(n):
    texts.append(input())

#2. for로 내용물 뽑아서 체크
for text in texts:
    reverse = text[::-1] # 다중연산 방지용 << 딱히 빨라지지 않았다.
    #3. 빙고
    if reverse in texts:
        break

print(len(text), text[len(text)//2])
