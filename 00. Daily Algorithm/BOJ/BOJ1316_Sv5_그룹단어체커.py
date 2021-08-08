'''
스터디에서 공유 받은 코드 뜯어보기
'''

res = 0
for i in range(int(input())):
    s = input()
    if list(s) == sorted(s, key=s.find):
        res += 1
print(res)

'''
elem[1]이면 두번째 요소를 일일히 확인하고 정렬하듯이
.find에 각각의 요소가 있는지 확인하고 True면 정렬하는것 같다.
sorted 특유의 정렬 안정성 때문에 가능한 풀이라고 할 수 있다.
근데 실전에서 이거 못쓸거 같아요 ㄷㄷㄷ
'''