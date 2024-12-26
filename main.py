from gtts import gTTS
import time

text = input("sese donusecek metin girin: ")
lang = input("metnin dili (tr/en) (default=tr): ")

if len(text) < 50:
    tts = gTTS(text=text, lang=lang if lang else "tr", slow=False)
    tts.save("ses.mp3")
    print("file saved successfully")
    time.sleep(3)
    exit(0)
else:
    print("metin cok uzun")
    time.sleep(2)
  
