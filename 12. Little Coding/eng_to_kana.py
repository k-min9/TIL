english_text = "hello this is mingu speaking"

import romajitable
result = romajitable.to_kana(english_text)
katakaned = result.katakana
katakaned = katakaned.replace('・', ' ')
print(katakaned)
