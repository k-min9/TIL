# https://leetcode.com/problems/implement-queue-using-stacks/
# 풀이 1: 스택 두개 사용해서 output 함수로 pop

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # 밑에 함수 호출해서 output 갱신에 썼음
        return self.output.pop()        

    def peek(self) -> int:
        # output 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output ==[]
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(4)

print(obj.input)
print(obj.output)

param_2 = obj.pop()

print(obj.input)
print(obj.output)

param_3 = obj.peek()
param_4 = obj.empty()

print(obj.input)
print(obj.output)