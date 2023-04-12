'''
클래스 상속받고 함수 이름 사용하여 계산하기
'''

class Compare:
    def get_result(self):
        pass

class MaxNum(Compare):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_result(self):
        return max(max(self._a, self._b), self._c)

class MinNum(Compare):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_result(self):
        return min(min(self._a, self._b), self._c)


def solution(a, b, c):
    answer = 0

    c1 = MaxNum(a, b, c)
    c2 = MinNum(a, b, c)

    answer = c1.get_result() + c2.get_result()
    return answer