from gtts import gTTS

import os
#opening the text file
f=open('sample.txt')

#reading the text file into varibale ---> "x"
x=f.read()

#select the laanguage
language='en'

#create audio using gTTs --> takes in three parameters --> (text || lang || slow)
audio=gTTS(text=x,lang=language,slow=False)

#save the audio
audio.save("sample.wav")

#open the audio when script runs
os.system("sample.wav")
