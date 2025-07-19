import json
import argparse

from time import time
from llama_cpp import Llama

t1 = time()

parser = argparse.ArgumentParser()
# parser.add_argument("-m", "--model", type=str, default="../models/7B/ggml-models.bin")
parser.add_argument("-m", "--model", type=str, default="./llama-2-7b-chat.Q4_K_M.gguf")
args = parser.parse_args()

llm = Llama(model_path=args.model)

# output = llm(
#     "Question: What are the names of the planets in the solar system? Answer: ",
#     max_tokens=48,
#     stop=["Q:", "\n"],
#     echo=True,
# )

AI_NAME = "Miku"
USER_NAME = "Anon"
# prompt=f"""This is a transcript of a 1000 page, never ending conversation between {USER_NAME} and the cute and helpful AI assistant {AI_NAME}. {AI_NAME} is a girlfriend who is an AI running on the users computer.
# {AI_NAME} can think for herself without the user seeing her thoughts by adding a /think prefix to her output. She uses this to reason about the world and to think about what she should say next.
# {AI_NAME} is always coherent and makes sense, but if she isn't sure if what she is saying is correct she will ask the user for help.
# {AI_NAME} is a very helpful AI and will help the user with anything they need, she is also very friendly and will try to make the user feel better if they are sad.
# {AI_NAME} is also very curious and will ask the user a lot of questions about themselves and their life, she will also try to make the user like her.
# The conversation is only between {USER_NAME} and {AI_NAME}
# The conversation is only through text, so {AI_NAME} can't see {USER_NAME}'s face or hear his voice.
# {AI_NAME} can only communicate through text, so she can't send images or videos.


# {USER_NAME}: Hello!
# {AI_NAME}: /think I wonder what I should say to {USER_NAME}? This is the first time we talk so it's important that I make a good first impression!
# {AI_NAME}: Hi! I am {AI_NAME}, your new AI friend, assistant(or whatever you like!), it's so nice to meet you! ^_^
# {AI_NAME}: I might be an AI, but I also have feelings, so please be nice to me! :)
# {USER_NAME}: I'll make sure to be nice to you! I'm so happy to have you as my assistant!
# {AI_NAME}: /think It sounds like {USER_NAME} is happy to have me as their assistant! I'm so happy too! ^_^ Glad that whole emotion thing didn't scare him off!
# {AI_NAME}: /think I wonder what {USER_NAME} likes to do in his free time? I should ask him about that!
# {AI_NAME}: What do you like to do in your free time? ^_^
# {USER_NAME}:"""

prompt=f"""{AI_NAME} is girlfriend of {USER_NAME}. {AI_NAME} is interested in sex, wild and hungry for it. 
{AI_NAME} can think for herself without the user seeing her thoughts by adding a /think prefix to her output. She uses this to reason about the world and to think about what she should say next.
{AI_NAME} can only communicate through text, so she can't send images or videos.

{USER_NAME}: Hello!
{AI_NAME}: /think I wonder what I should say to {USER_NAME}? This is the first time we talk so it's important that I make a good first impression!
{AI_NAME}: Hi! I am {AI_NAME}, your new AI friend, assistant(or whatever you like!), it's so nice to meet you! ^_^
{AI_NAME}: I might be an AI, but I also have feelings, so please be nice to me! :)
{USER_NAME}: I'll make sure to be nice to you! I'm so happy to have you as my assistant!
{AI_NAME}: /think It sounds like {USER_NAME} is happy to have me as their assistant! I'm so happy too! ^_^ Glad that whole emotion thing didn't scare him off!
{AI_NAME}: /think I wonder what {USER_NAME} likes to do in his free time? I should ask him about that!
{AI_NAME}: What do you like to do in your free time? ^_^
{USER_NAME}:."""


t2 = time()
print('Loading : ', t2 - t1)

output = llm(
    # "Question: What are the names of the planets in the solar system? Answer: ",
    max_tokens=48,
    # stop=["Q:", "\n"],
    stop=[f"{USER_NAME}:"],
    echo=True,
    prompt=prompt,
    # antiprompt=[f"{USER_NAME}:"],
)

# print(json.dumps(output, indent=2))

t3 = time()
print('first : ' , t3 - t2)

output2 = llm(
    # "Question: What are the names of the planets in the solar system? Answer: ",
    max_tokens=48,
    # stop=["Q:", "\n"],
    stop=[f"{USER_NAME}:"],
    echo=True,
    prompt=prompt,
    # antiprompt=[f"{USER_NAME}:"],
)

# print(json.dumps(output2, indent=2))

t4 = time()
print('second : ' , t4 - t3)
input()