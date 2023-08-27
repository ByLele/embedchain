import os
os.environ["OPENAI_API_KEY"] = "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"
from embedchain import App

opapp = App()

# Embed Online Resources
#naval_chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
#naval_chat_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
#res = naval_chat_bot.add("web_page", "https://time.geekbang.org/column/article/369457")
#opapp.add("web_page", "https://time.geekbang.org/column/article/374474")
opapp.add("web_page", "https://time.geekbang.org/column/article/375278")
opapp.add("web_page", "https://time.geekbang.org/column/article/376064")
opapp.add("web_page", "https://time.geekbang.org/column/article/374474")
opapp.add("web_page", "https://time.geekbang.org/column/article/376711")
opapp.add("web_page", "https://time.geekbang.org/column/article/377913")
opapp.add("web_page", "https://time.geekbang.org/column/article/378870")
opapp.add("web_page", "https://time.geekbang.org/column/article/379291")
opapp.add("web_page", "https://time.geekbang.org/column/article/380507")
opapp.add("web_page", "https://time.geekbang.org/column/article/381157")

# Embed Local Resources
#naval_chat_bot.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravihkant is an Indian-American entrepreneur and investor."))
#naval_chat_bot.query("what naval is good at?")
res = opapp.query("初始化内核栈 是为什么 ")
print(res)