'''
로그 txt를 읽고 특정 문장/단어가 포함된 문장의 로그 시간을 계산하여 출력
'''
file_input = 'input.txt'
file_output = 'output.txt'

# 문장/단어 리스트
search_list = list()
search_list.append('INSERT INTO')
search_list.append('DELETE')

filtered_list = list()

with open(file_input, 'r', encoding='utf-8') as file:
    for line in file:
        if any(word in line for word in search_list):
            filtered_list.append(line)

logs = list()
time = 0
for sentence in filtered_list:
    # 02:03:12 ~~~ 같은 형태였다고 가정
    h = int(sentence[0:2])
    m = int(sentence[3:5])
    s = int(sentence[6:8])
    tmp_time = s + 60 *m + 60*60* h
    elapsed_time = tmp_time - time
    time = tmp_time

    logs.append(str(elapsed_time) + 's : ' + sentence[10:])

# 출력물 저장
with open(file_output, 'w', encoding='utf-8') as output_file:
    for log in logs:
        output_file.write(log)
