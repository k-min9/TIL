'''
mort의 로그형식 txt를 파싱하여 대화 형태의 txt를 출력
'''
# 필터링 작업에 사용할 key와 value를 정리한 자료구조
filters = {
    'key1': 'value1 : ',
    'key2': 'value2 : ',

    '- (': '(',

    '- arona': 'arona : ',
}

read_filename = 'read.txt'
write_filename = 'write.txt'

with open(read_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

last_sentence = ''
skip_length = 0 # 특정 문장수까지 skip
flag = False # 문장추가 여부

output = []
for i in range(len(lines)):
    if lines[i].strip() == '/s':
        sentence = lines[i+1].strip()
        # 문장이 동일하면 skip
        if last_sentence == sentence:
            continue
        # 빈 문장 스킵
        if not sentence:
            continue
        # x번째 문장까지 skip
        if skip_length > 0:
            skip_length -= 1
            continue

        # last_sentence가 sentence 안에 있는지 확인하고, 없을 경우 flag True로
        if last_sentence not in sentence:
            flag = True

        if flag:
            for key, value in filters.items():
                if last_sentence.startswith(key):
                    last_sentence = last_sentence.replace(key, value, 1)  # 첫 번째로 일치하는 부분만 변경
                    last_sentence = value + last_sentence[len(value):]  # 변경된 부분을 문장 맨 앞에 배치
            
            output.append(last_sentence) # 추가

        # 초기화
        flag = False
        last_sentence = sentence

# 최후의 문장
for key, value in filters.items():
    if last_sentence.startswith(key):
        last_sentence = last_sentence.replace(key, value, 1)  # 첫 번째로 일치하는 부분만 변경
        last_sentence = value + last_sentence[len(value):]  # 변경된 부분을 문장 맨 앞에 배치
output.append(last_sentence)

with open(write_filename, 'w', encoding='utf-8') as file:
    file.write('\n'.join(output))
