'''
1일 1 알고
'''
import sys
input = sys.stdin.readline


def calc(prime_array, target):
    for n1 in prime_array:
        for n2 in prime_array:
            for n3 in prime_array:
                if n1 + n2 + n3 == target:
                    print(n1, n2, n3)
                    return
    print(0)
 

def findPrime(num):
    data = list(range(2, num + 1))
    result = []
 
    while len(data) != 0:
        m = data[0]
        result.append(m)
        cnt = 0
        while cnt < len(data):
            if data[cnt] % m == 0:
                data.pop(cnt)
                cnt -= 1
            cnt += 1
 
    return result
 

T = int(input())
N = []
 
for i in range(T):
    N.append(int(input()))
 
for n in N:
    calc(findPrime(n), n)