import os
os.environ["OPENAI_API_KEY"] = "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"
from embedchain import App

naval_chat_bot = App()

# Embed Online Resources
naval_chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
naval_chat_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
naval_chat_bot.add("web_page", "https://nav.al/feedback")
naval_chat_bot.add("web_page", "https://nav.al/agi")
#
# # Embed Local Resources
naval_chat_bot.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravihkant is an Indian-American entrepreneur and investor."))
naval_chat_bot.query("what naval is good at?")
res = naval_chat_bot.get_openai_answer("what is AngelList的 business? 中文回复")
print(res)
print(naval_chat_bot.query("What unique capacity does Naval argue humans possess when it comes to understanding explanations or concepts?"))