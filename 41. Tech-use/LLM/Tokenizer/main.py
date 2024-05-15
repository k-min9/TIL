'''
tokenizer.json이 있는 사용자이름/repo나 local을 지정
'''
from transformers import AutoTokenizer, AutoModel

# base_model = 'meta-llama/Meta-Llama-3-8B'
base_model = 'Xenova/llama-3-tokenizer'
base_model = 'lmms-lab/llama3-llava-next-8b-tokenizer'
base_model = 'sh2orc/llama-3-korean-8b-awq'
# base_model = 'yanolja/EEVE-Korean-Instruct-10.8B-v1.0'

tokenizer = AutoTokenizer.from_pretrained(base_model)

output = tokenizer('나는 아침을 먹었다.')
print(output.tokens())