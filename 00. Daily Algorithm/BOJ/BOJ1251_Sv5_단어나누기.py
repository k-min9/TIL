'''
1. idx 1~ len-1 까지 돌면서 사전상 가장 낮은거 찾아서 1부터 뒤집고
2. 한번 더
끝?
'''

# words = input()

# min_word = 200
# point = 0  # 슬라이스 포인트

# for i in range(len(words)-2):
#     if ord(words[i]) <=  min_word and words[:i+1][::-1] <= words[:point+1][::-1]:
#         min_word = ord(words[i])
#         point = i

# answer = words[:point+1][::-1]
# words = words[point+1:len(words)]

# # print('1', point, answer, words)


# # 두 바퀴째
# min_word = 200

# for i in range(len(words)-1):
#     if ord(words[i]) <=  min_word and words[:i+1][::-1] <= words[:point+1][::-1]:
#         min_word = ord(words[i])
#         point = i

# answer = answer + words[:point+1][::-1] + words[point+1:len(words)][::-1]

# print(answer)

'''
ord(words[i]) == min_word 일때를 대응하지 못해서 이것저것 더 붙여버린 누더기 풀이지만 80% 이상 안올라간다. 뭐가 틀린지 몰겠으니까...
'''

answers = []
words = input()
for i in range(len(words)-2):
    for j in range(i+1, len(words)-1):
        answers.append(words[:i+1][::-1] + words[i+1:j+1][::-1] + words[j+1:][::-1])

print(min(*answers))

'''
오 금방이네
'''