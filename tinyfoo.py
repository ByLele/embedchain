tinyfoo_url = "https://www.youtube.com/watch?v=Pr4Sw6cYAfU"
cs_url = "https://www.youtube.com/watch?v=nl-32XCl3fg"
test_url = "https://www.youtube.com/watch?v=LY6tetuV-6Y"
import os
os.environ["OPENAI_API_KEY"] = "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"
from embedchain import App as ECApp

Tapp = ECApp()

# Embed Online Resources
Tapp.add("youtube_video",test_url)
# naval_chat_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
# naval_chat_bot.add("web_page", "https://nav.al/feedback")
# naval_chat_bot.add("web_page", "https://nav.al/agi")
# #
# # Embed Local Resources
#naval_chat_bot.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravihkant is an Indian-American entrepreneur and investor."))
#naval_chat_bot.query("what naval is good at?")
#res = naval_chat_bot.get_openai_answer("what is AngelList的 business? 中文回复")
#print(res)
print(Tapp.query(" why intersectoral approaches to enabling Better Health"))
print(Tapp.query("what LY6tetuV-6Y video say"))