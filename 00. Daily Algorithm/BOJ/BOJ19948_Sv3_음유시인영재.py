'''
스페이스 충분한지 확인하기
마지막 글자 저장하여 같은지 체크하기
'''
import sys
input = sys.stdin.readline

# 입력
texts = input().split()
space = int(input())
alphas = list(map(int, input().split()))

# 스페이스바 충분한지 확인
if len(texts) - 1 > space:
    print(-1)
else:
    answer = ''
    last_text = ''
    # 제목 기록
    for text in texts:
        next_text = text[0].upper()
        answer += next_text
        if last_text == next_text:
            continue
        last_text = next_text

        text_num = ord(next_text) - ord('A')
        alphas[text_num] -= 1
    
    # 내용 기록
    last_text = ''
    for text in texts:
        for t in text:
            next_text = t.upper()
            if last_text == next_text:
                continue
            last_text = next_text

            text_num = ord(next_text) - ord('A')
            alphas[text_num] -= 1

    # 키보드 망가졌나 확인
    is_break = False
    for alpha in alphas:
        if alpha < 0:
            is_break = True
    
    if is_break:
        print(-1)
    else:
        print(answer)
