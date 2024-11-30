# from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI


llm = ChatOpenAI(temperature=0,
                    openai_api_key="key1",
                    max_tokens=3000,
                    model_name="gpt-3.5-turbo",
                    request_timeout=120
                )

schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100, return_messages=True)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, {"output": f"{schedule}"})

conversation = ConversationChain(
   llm=llm,
   memory=memory,
   verbose=True
)

response = conversation.predict(input="what are you doing now?")

# print(conversation)
print(response)