'''
무료는 대단해!
pip install googletrans==3.1.0a0
'''
from googletrans import Translator

def google_trans(messages):
    google = Translator()
    result = google.translate(messages, dest="ko")
    result = google.translate(messages, dest="ja")
    result = google.translate(messages, dest="en")

    return result.text

text = "あんた、頭大丈夫？"
text = "너, 머리 괜찮아?"
text = "너 괜찮아?"

result = google_trans(text)
print(result)
