import pyttsx3
voice=input()
engine = pyttsx3.init()
engine.say(voice)
engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()