from sys import stdin
from functools import reduce
from operator import mul

def get_modulo_inverse(a, b):
    '''
    Calculate inverse of a (mod b)
    '''
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

factorial = {} # factorial[m][n] : n! (mod m)
inverse = {} # inverse[m][n]: inverse of n! (mod m)

def choose_modulo_prime(n, m, p):
    '''Calculate C(n, m) % p
    1 <= n <= 10^18, 0 <= m <= n, 2 <= p <= 2000
    p must be prime

    Return: int
    '''
    def get_factorial(num):
        if p not in factorial:
            factorial[p] = {0: 1, 1: 1}
        for idx in range(2, num+1):
            factorial[p][idx] = factorial[p][idx-1] * idx % p
        return factorial[p][num]

    def get_inverse(num):
        if p not in inverse:
            inverse[p] = {0: 1, 1: 1}
        for idx in range(2, num+1):
            inverse[p][idx] = get_modulo_inverse(get_factorial(idx), p)
        return inverse[p][num]

    choose_prod = 1
    while n != 0 or m != 0:
        n_digit = n % p
        n //= p
        m_digit = m % p
        m //= p

        if n_digit < m_digit:
            choose_prod = 0
            break
        else:
            choose_prod *= get_factorial(n_digit) * get_inverse(m_digit) * get_inverse(n_digit-m_digit)
            choose_prod %= p
        
    return choose_prod    

p_adic_factorial = {} # p_adic_factorial[m][n]: (n!)_m (mod m)
p_adic_inverse = {} # p_adic_inverse[m][n]: inverse of (n!)_m (mod m)

def choose_modulo_prime_power(n, m, p, q):
    '''Calculate C(n, m) % p^q.
    1 <= n <= 10^9, 0 <= m <= n, q >= 1
    p must be prime
    
    Return: int
    '''
    modulo = p ** q

    def expand_by_p(n, m, r):
        '''Expand number with given base (p).
        Each n, m, r will expanded until their length is more than d_min.
        
        Return: tuple(list, list, list, int)
        '''
        n_expand, m_expand, r_expand = [], [], []
        d = 0
        d_min = q-1
        while n > 0 or m > 0 or r > 0 or d <= d_min:
            n_expand.append(n % p)
            n //= p
            m_expand.append(m % p)
            m //= p
            r_expand.append(r % p)
            r //= p

            d += 1
        return n_expand, m_expand, r_expand, d-1
    
    def least_positive_residue(n, m, r, d):
        '''Calculate x // p^j % p^q where x = n, m, r and j = 0, 1, ..., d

        Return: tuple(list, list, list)
        '''
        n_lpr, m_lpr, r_lpr = [], [], []
        for _ in range(d+1):
            n_lpr.append(n % modulo)
            n //= p
            m_lpr.append(m % modulo)
            m //= p
            r_lpr.append(r % modulo)
            r //= p
        return n_lpr, m_lpr, r_lpr
    
    def carry_count(m_expand, r_expand, d):
        '''Count number of carries occur when add m and r with base p.

        Return: tuple(int, int)
        '''
        has_carry = [0] * (d+1)
        prev_carry = 0
        for idx in range(d+1):
            value = m_expand[idx] + r_expand[idx] + prev_carry
            if value >= p:
                has_carry[idx] = 1
                prev_carry = 1
            else:
                prev_carry = 0
        
        eq1 = sum(has_carry[q-1:])
        e0 = sum(has_carry[:q-1]) + eq1
        return e0, eq1
    
    def get_p_adic_factorial(num):
        if p not in p_adic_factorial:
            p_adic_factorial[p] = {0: 1, 1: 1}
        begin = len(p_adic_factorial[p])
        for idx in range(begin, num+1):
            p_adic_factorial[p][idx] = p_adic_factorial[p][idx-1] * (1 if idx % p == 0 else idx) % modulo
        return p_adic_factorial[p][num]
    
    def get_p_adic_inverse(num):
        if p not in p_adic_inverse:
            p_adic_inverse[p] = {0: 1, 1: 1}
        begin = len(p_adic_inverse[p])
        for idx in range(begin, num+1):
            p_adic_inverse[p][idx] = get_modulo_inverse(get_p_adic_factorial(idx), modulo)
        return p_adic_inverse[p][num]

    r = n - m
    _, m_expand, r_expand, d = expand_by_p(n, m, r)
    n_lpr, m_lpr, r_lpr = least_positive_residue(n, m, r, d)
    e0, eq1 = carry_count(m_expand, r_expand, d)

    n_factorial = map(get_p_adic_factorial, n_lpr)
    m_inverse = map(get_p_adic_inverse, m_lpr)
    r_inverse = map(get_p_adic_inverse, r_lpr)

    p_adic_choose = (n * m * r % modulo for n, m, r in zip(n_factorial, m_inverse, r_inverse))
    choose_prod = reduce(mul, p_adic_choose) % modulo

    sign = 1 if p == 2 and q >= 3 else -1
    pm = 1 if sign == 1 or eq1 % 2 == 0 else -1

    return p ** e0 * pm * choose_prod % modulo

def get_crt_root(a_list, n_list):
    '''Calculate root of x ≡ a_i (mod n_i) for each a_i and n_i.
    Length of a_list and n_list must be same.

    Result: int (in bound of 0 and N where N is product of each n_i)
    '''
    n_mul = reduce(mul, n_list)
    root_list = (a * n_mul // n * (n_mul // n % a) for a, n in zip(a_list, n_list))
    return sum(root_list) % n_mul

n_list = [27, 11, 13, 37]

input = stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a_list = [choose_modulo_prime_power(n, k, 3, 3), choose_modulo_prime(n, k, 11), choose_modulo_prime(n, k, 13), choose_modulo_prime(n, k, 37)]
    print(str(get_crt_root(a_list, n_list)))
    print('\n')
