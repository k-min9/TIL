from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain

# 키 관리는 철저히
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_KEY = os.environ.get('OPENAI_KEY')

# 파일 읽기
file_path = 'summary.txt'
file_content = ''
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# chunk 분할
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,  # 거의 토큰값과 유사. 3.5-turbo인 경우 4096 토큰(16k면 4배) / 우리는 chunk 4개와 prompt와 질문을 보내야 함...!
    chunk_overlap=100,  # chunk끼리 약간 겹치게 해야, 내용이 이어짐
    length_function=len
)
chunks = text_splitter.split_text(file_content)

# 임베딩 학습
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
knowledge_base = FAISS.from_texts(chunks, embeddings)
