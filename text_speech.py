from gtts import gTTS
import os
f=open("text_to_speech_data.txt")
x=f.read()
language='en'
audio= gTTS(text=x,lang=language,slow=False)
audio.save("text_to_speech_data.wav")
os.system("text_to_speech_data.wav")
