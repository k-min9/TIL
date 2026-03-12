import re

def extract_quoted_sentences(text):
    pattern = r'(["“‘\(])(.*?)(["”’\)])'  # ["“‘\(]: "“‘( 네가지 중 하나  (.*?) : 임의의 문자열
    matches = re.findall(pattern, text)
    
    found_quoted = False
    for match in matches:
        print(match)
        quoted_sentence = match[1]
        print(quoted_sentence)
        found_quoted = True
    
    if not found_quoted:
        print('없음 : ', text.strip())

# 입력된 문자열 리스트
input_texts = [
    '[s1] “맞습니다.”',
    '[s] “너희들이라면 분명 저번에…….”',
    '[s] “대놓고 그런 말을 하는 건 좀 그렇지 않아?”',
    '[s] (고용주라면 전에 말했던…….)',
    '[ns] "<브랜드>?"',
    '그런거없다'
]
