'''
한글 -> 가타카나

pip install hangul-romanize
'''
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
import romajitable

def korean_to_roman(text):
    transliter = Transliter(academic)
    romanized_text = transliter.translit(text)
    return romanized_text

# 1번 타자
def kor_to_romaji1(txt):
    # 로마자로 변환
    romanized_text = korean_to_roman(txt)
    # print("로마자로 변환된 텍스트:", romanized_text)
    
    result = romajitable.to_kana(romanized_text)
    katakaned = result.katakana
    katakaned = katakaned.replace('・', ' ')
    return katakaned

# 2번 타자
def kor_to_romaji2(txt):
    import transliter as tl
    a = tl.ko(txt)
    # print(a)
    result = romajitable.to_kana(a)
    katakaned = result.katakana
    katakaned = katakaned.replace('・', ' ')
    return katakaned

# Test
if __name__ == "__main__":
    korean_text = "안녕하세요."
    print(kor_to_romaji1(korean_text))
    print(kor_to_romaji2(korean_text))
