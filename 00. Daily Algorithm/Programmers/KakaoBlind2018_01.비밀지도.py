def calc(a, b, n):
    ret = bin(a|b)[2:]
    ret = ret.zfill(n)
    ret = ret.replace('1','#')
    ret = ret.replace('0',' ')
    return ret

def solution(n, arr1, arr2):
    
    answer = []
    
    for i in range(n):
        answer.append(calc(arr1[i], arr2[i], n))
    
    return answer

'''
문자열 조작 공부 조금 더 하긴 해야겠는데
'''