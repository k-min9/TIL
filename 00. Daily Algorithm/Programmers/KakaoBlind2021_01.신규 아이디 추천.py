def solution(new_id):
    #1. 소문자
    answer = new_id.lower()
    #2. 문자열 제거
    for char in '~!@#$%^&*()=+[{]}:?,<>/':
        answer = answer.replace(char,'')
    #3. 연속된 . 제거
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4. 양 끝의 . 제거
    answer = answer.strip('.')
    #5. 빈 문자열시 a 부여
    if not answer:
        answer = 'a'
    #6. 문자열 길이 15까지
    answer = answer[:15]
    answer = answer.rstrip('.')
    #7. 문자열 길이 3 이상으로
    while(len(answer)<3):
        answer += answer[-1]
        
    return answer