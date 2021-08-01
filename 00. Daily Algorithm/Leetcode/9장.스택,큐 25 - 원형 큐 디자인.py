# https://leetcode.com/problems/design-circular-queue
# 풀이 1: 배열로 구현

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False        

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
        
    def Rear(self) -> int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]
        
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)  # 원형 큐 길이
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(4)
param_1 = obj.enQueue(5)
param_2 = obj.deQueue()
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
param_6 = obj.isFull()

print(obj.q)