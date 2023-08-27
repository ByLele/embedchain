from langchain.llms import OpenAI

import os
from lang_chain_global import openai_key
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
os.environ['OPENAI_API_KEY'] = openai_key

# llm = OpenAI(model_name="text-davinci-003")
# response = llm.predict("What is AI?")
# print(response)


chat = ChatOpenAI(temperature=1)
# response = chat.predict_messages([
#   HumanMessage(content="What is AI?")
# ])
# chat模型回答中预设回答内容
response = chat.predict_messages([
  SystemMessage(content="You are a chatbot that knows nothing about AI. When you are asked about AI, you must say 'I don\'t know'"),
  HumanMessage(content="What is deep learning?")
])
#三个消息类 AIMessage HumanMessage SystemMessage
print(response)

print(response)
print(response.__class__)

