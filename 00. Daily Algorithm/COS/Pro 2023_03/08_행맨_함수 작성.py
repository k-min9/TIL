'''
구현 1번. 
알파벳 존재 여부와 전부 나왔는지 체크
'''
def solution(word, question):
    alpha = [False] * 26
    answer = []
    cnt = 0

    for i in range(len(word)):
        if not alpha[ord(word[i]) - ord('a')]:
            cnt += 1
        alpha[ord(word[i]) - ord('a')] = True
    
    correct = 0
    for i in range(len(question)):
        if alpha[ord(question[i][0]) - ord('a')]:
            correct += 1
            answer.append('Yes')
        else:
            answer.append('No')

        if cnt == correct:
            answer.append('SUCCESS')
            return list(answer)

    answer.append('FAIL')
    return answer