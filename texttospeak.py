from gtts import *
from playsound import *

txt=input("enter any text")
print(txt)
speak=gTTS(txt)
speak.save('raj.mp3')
playsound('raj.mp3')