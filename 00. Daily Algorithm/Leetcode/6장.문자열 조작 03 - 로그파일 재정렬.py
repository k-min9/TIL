# https://leetcode.com/problems/reorder-data-in-log-files
# 풀이. 람다 + 연산자

def reorderLogFiles(self, logs: list[str]) -> list[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
            
    letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
    return letters + digits
