# https://github.com/ShumzZzZz/GPT-Rambling/blob/main/LangChain%20Specific/langchain_persist_conversation_memory.ipynb
# https://python.langchain.com/docs/modules/memory/types/summary

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.chains import ConversationalRetrievalChain, ConversationChain
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory


llm = ChatOpenAI(temperature=0.1, openai_api_key="key")

# 대화 내역을 저장하고 관리하기 위한 메모리 객체 생성.
# max_token_limit은 메모리가 저장할 수 있는 최대 토큰 수를 설정합니다.
# memory_key는 이 메모리 인스턴스를 식별하는 데 사용됩니다.
# return_messages는 메모리에서 메시지를 반환할지 여부를 결정합니다.
memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=120,
    memory_key="chat_history",
    return_messages=True,
)

template = """
    You are a helpful AI talking to a human

    {chat_history}
    Human:{question}
    You:
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI talking to a human"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{question}"),
])

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=PromptTemplate.from_template(template),
    verbose=True,
)

chain.predict(question="My name is juho")
chain.predict(question="what's my name?")




### save

extracted_messages = chain.memory.chat_memory.messages
ingest_to_db = messages_to_dict(extracted_messages)
# print(extracted_messages)

import json
# save_file = json.dumps(chain.memory.to_json())
save_file = json.dumps(ingest_to_db)
retrieve_from_db = json.loads(save_file)

# print(retrieve_from_db)
print(retrieve_from_db['repr'])

# retrieved_messages = messages_from_dict(retrieve_from_db)
# retrieved_messages = messages_from_dict(retrieve_from_db['repr'])
retrieved_chat_history = ChatMessageHistory(messages='a')
retrieved_memory = ConversationSummaryBufferMemory(chat_memory=retrieved_chat_history)



chain_load = LLMChain(
    llm=llm,
    memory=retrieved_memory,
    prompt=PromptTemplate.from_template(template),
    verbose=True,
)

response = chain_load.predict(question="what did i said?")
print(response)

# import pickle
# pickled_str = pickle.dumps(chain.memory)
# conversation2 = ConversationChain(llm=llm, memory=pickle.loads(pickled_str))

# response = chain.predict(question="What did i said?")
# print(response)