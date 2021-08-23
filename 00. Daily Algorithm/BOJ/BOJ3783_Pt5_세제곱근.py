'''
파이썬 뽕에 취한다!
'''

import decimal
# 천자리까지 정확도 주기
decimal.getcontext().prec = 1000


N = int(input())
for _ in range(N):
    d = decimal.Decimal(input().rstrip() + '.0000000000') 
    pow = decimal.Decimal('1') / decimal.Decimal('3')
    d = decimal.Decimal(d ** pow)
    # decimal 파이썬 자체 내장 함수에 대응, 500자리에서 대충 올렸다.
    d = round(d, 500)
    d = decimal.Decimal(d).quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN)
    print(d)
