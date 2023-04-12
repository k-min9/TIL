'''
클래스 상속하고 이름 사용하기
'''
class Diet:
    def cal_calories(self):
        pass

class Food(Diet):

    def __init__(self, food_gram, calories_per_gram):
        self._food_gram = food_gram
        self._calories_per_gram = calories_per_gram

    def cal_calories(self):
        return self._food_gram * self._calories_per_gram


class Exercise(Diet):

    def __init__(self, exercise_hour, calories_per_hour):
        self._exercise_hour = exercise_hour
        self._calories_per_hour = calories_per_hour

    def cal_calories(self):
        return self._exercise_hour * self._calories_per_hour


def solution(food, exercise):
    answer = 0

    i = 0
    while i < len(food):
        f = Food(food[i][0], food[i][1])
        answer += f.cal_calories()
        i += 1

    i = 0
    while i < len(exercise):
        e = Exercise(exercise[i][0], exercise[i][1])
        answer -= e.cal_calories()
        i += 1

    return answer