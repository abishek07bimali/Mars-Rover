
import pyttsx3

engine = pyttsx3.init()

current_rate = engine.getProperty('rate')
new_rate = 150  
engine.setProperty('rate', new_rate)
text = "Hi I am Robo built by Rover Group. I am specially designed and built for patroling system"
engine.say(text)
engine.runAndWait()





