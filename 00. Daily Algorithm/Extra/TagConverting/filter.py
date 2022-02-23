'''
인스타그램 태그를 받아 가공해서, 사용할 수 있는 데이터로 정제
'''

import sys
sys.stdin = open("input.txt", encoding='utf-8')
sys.stdout = open("output.txt", 'w', encoding='utf-8')

# 상수
banned = ['insta', 'gram', '인스타', '그램']  # 금지어

tags = set()
while True:
    txt = input().rstrip()
    if txt != 'end':
        for t in txt.split():
            tags.add(t)
    else:
        break

cnt = 0
print('[', end='')
for tag in tags:
    # 금지어 체크
    flag = False
    for ban in banned:
        if ban in tag:
            flag = True
    if flag:
        continue

    tag = "'" +tag[1:] + "'"
    print(tag, end=', ')
    cnt += 1

print(']')




# 결과물 출력하기
# print(cnt)
# python filter.py > output.txt