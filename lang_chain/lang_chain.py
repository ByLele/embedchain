#import lang_chain.chat_models
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

os.environ['OPENAI_API_KEY'] = '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'

chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
response = chat([ HumanMessage(content="Hello Langchain!") ])
print(response)
#llM一对一
#chat 多对一