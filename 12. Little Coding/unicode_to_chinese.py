'''
유니코드 인코딩 된 중국어를 디코딩하자.
방법 1 : ast
방법 2 : codecs
방법 3 : unicode_escape

>> 전부 내장라이브러리지만, ast 값이 가장 안정적이었음
'''
import ast

encoded_str = "\u611a\u4eba\u4f17\u58eb\u5175b"
decoded_str = ast.literal_eval(f'"{encoded_str}"')

print(1, decoded_str)
################################
import codecs

encoded_str = "\u611a\u4eba\u4f17\u58eb\u5175b"
decoded_str = codecs.decode(encoded_str, 'unicode_escape')

print(2, decoded_str)
################################
encoded_str = "\u611a\u4eba\u4f17\u58eb\u5175b"
decoded_str = bytes(encoded_str, 'utf-8').decode('unicode_escape')

print(3, decoded_str)