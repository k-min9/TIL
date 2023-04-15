'''
클래스 구현
'''
class Study:
    def calFatigability(self, t):
        pass

class Korean(Study):
    def calFatigability(self, t):
        fatigability = 20
        t -= 2
        if t > 0:
            fatigability += t * 40
        return fatigability

class Math(Study):
    def calFatigability(self, t):
        fatigability = 30
        t -= 3
        if t > 0:
            fatigability += t * 50
        return fatigability

class English(Study):
    def calFatigability(self, t):
        fatigability = 40
        t -= 4
        if t > 0:
            fatigability += t * 10
        return fatigability

def solution(subjects, t):
    study = [None for _ in range(10)]
    
    for i in range (len(subjects)):
        if subjects[i] == 'korean':
            study[i] = Korean()
        elif subjects[i] == 'math':
            study[i] = Math()
        elif subjects[i] == 'english':
            study[i] = English()

    answer = 0
    for i in range (len(subjects)):
        answer += study[i].calFatigability(t)
        answer -= 20

    return answer
