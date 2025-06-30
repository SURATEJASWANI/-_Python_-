

import pyttsx3
import time

data=pyttsx3.init()
voices=data.getProperty('voices')
for voice in voices:
  if "zira" in voice.name.lower():    # zira is common female voice in Windows
    data.setProperty('voice', voice.id)
    break
    
data.setProperty('rate',150)          # voice speed increase, lower voice--> lower value

g=['tej', 'vinod', 'haadya', 'swani']
h=[]
for x in g:
  time.sleep(1)
  data.say(x)
  h.append('present')
else:
  h.append('absent')
  data.runAndWait()
