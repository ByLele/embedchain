#LLM需要的用户特定的模型
#类型
#文档加载器
#文档转换器
#文本嵌入器  非结构化文本转化为浮点数组（向量）
#向量存储
#检索器

"""
加载文档
langchain loaders

拆分文档
ai问答基础
按照字符拆分，**分隔符**
CharacterTextSplitter
MarkDownTextSplitter

向量化
寻找相似度最高的文本段
openAiEmbedding

存储，存入向量数据库

检索

"""
# import langchain.text_splitter
# from langchain.document_loaders import TextLoader
# #form langchain.text_splitter.
#
# from langchain.embeddings import OpenAIEmbeddings
# from lang_chain_global import openai_key
#
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import Chroma
#
# loader = TextLoader("../README.md")
# OpenAIEmbeddings(openai_api_key=openai_key)
# docs = loader.load()
#
#
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# documents = text_splitter.split_documents(docs)
# db = Chroma.from_documents(documents, OpenAIEmbeddings())
from langchain.document_loaders import TextLoader
from lang_chain_global import openai_key
loader = TextLoader("../README.md")
docs = loader.load()
print(docs)


from langchain.text_splitter import CharacterTextSplitter

text_spliter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,# 续接上文
    length_function= len,
)

split_docs = text_spliter.split_documents(docs)
print(len(docs[0].page_content))

for split_doc in split_docs:
    print(len(split_doc.page_content))
"""
拆分python代码
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

PYTHON_CODE = """
def hello_langchain():
    print("hello,langchain")
hello_langchain()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 50,
    chunk_overlap = 0,
)

python_doc = python_splitter.create_documents([PYTHON_CODE])
#python_doc [
# Document(page_content='def hello_langchain():', metadata={}),
# Document(page_content='print("hello,langchain")
# hello_langchain()', metadata={})] 拆分出来的文本是有语义的
print(python_doc)


"""
markdown拆分
"""
from langchain.text_splitter import MarkdownHeaderTextSplitter

markdown_document = "# Chapter 1\n\n    ## Section 1\n\nHi this is the 1st section\n\nWelcome\n\n ### Module 1 \n\n Hi this is the first module \n\n ## Section 2\n\n Hi this is the 2nd section"

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
splits = splitter.split_text(markdown_document)
print(splits)


"""
字符递归拆分
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 100,# 不一定根据设置大小拆分，根据具体语义拆分
    chunk_overlap  = 20,
    length_function = len,
    #separators=
)
texts = text_splitter.split_documents(docs)

for split_doc in split_docs:
    print(len(split_doc.page_content))

"""
根据token拆分
"""

from langchain.text_splitter import CharacterTextSplitter
text_token_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=0
)
split_token_docs = text_token_splitter.split_documents(docs)
for split_token_doc in split_token_docs:
    print(split_token_doc)


"""
向量化文档分块
"""

from langchain.embeddings import OpenAIEmbeddings

embedchain_model = OpenAIEmbeddings(openai_api_key=openai_key)

embeddings = embedchain_model.embed_documents(
    [
        "你好!",
        "Langchain!",
        "你真棒！"
    ]
)
print(embeddings)

"""
存储
"""
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(docs)
db = Chroma.from_documents(documents, OpenAIEmbeddings(openai_api_key=openai_key))
print(db)


"""
查询
"""
query = "what is embedchain ?"

docs = db.similarity_search(query)
print(len(docs))
print(docs)