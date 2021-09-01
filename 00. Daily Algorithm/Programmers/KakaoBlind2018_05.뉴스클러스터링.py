from collections import Counter

def solution(str1, str2):
    charset = {'a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    cnt1 = Counter()
    cnt2 = Counter()
    
    for i in range(len(str1)-1):
        if str1[i] in charset and str1[i+1] in charset:
            cnt1[str1[i]+str1[i+1]] += 1
    for i in range(len(str2)-1):
        if str2[i] in charset and str2[i+1] in charset:
            cnt2[str2[i]+str2[i+1]] += 1
    
    union = cnt1|cnt2
    intersect = cnt1&cnt2
    a = sum(union.values())
    b = sum(intersect.values())
    
    if len(union) == 0:
        return 65536

    # print(union)
    # print(intersect)
    # print(cnt1)
    # print(cnt2)
    answer = b*65536//a
    return answer