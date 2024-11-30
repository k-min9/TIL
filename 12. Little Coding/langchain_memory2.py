from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


llm = ChatOpenAI(temperature=0.1, openai_api_key="key")

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=80,
    memory_key="chat_history",
    return_messages=True,
)

def load_memory(input):
    print(input)
    return memory.load_memory_variables({})["chat_history"]
    
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI talking to human"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}"),
])

chain = RunnablePassthrough.assign(chat_history=load_memory) | prompt | llm

def invoke_chain(question):
    result = chain.invoke({"question": question})
    memory.save_context(
        {"input": question},
        {"output": result.content},
    )
    print(result)

# invoke_chain("My name is nam.")
invoke_chain("What's my name?")

# invoke_chain("remeber what i said?")