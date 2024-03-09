from genericpath import isfile
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import datetime
import random


Hello_Qe = ["hello", "hey", "how are you", "hi", "good day", "what's up"]
Hello_Res = ["hello sir", "hello, nice to see you", "hey, how are you?", "good day, how do you feel?"]

Left_Qe = ["good by", "cya", "i have to go", "i am leaving", "bye", "see you"]
Left_Res = ["love you", "it was nice", "good bye", "see ya"]

Times_Qwestions = ["hour", "time"]
Times_Respons = ["now is ", "the hour now is ", "now is "]




engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')



# listen function, say what you want
def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said




def wishme():
    hour = int(datetime.datetime.now().hour)




# speak function
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()



speak("hello, my name is jarvis")

text = get_audio()

print(text)


if "hello" in text:
    answer = random.choice(Hello_Res)
    speak(answer)

if "bye" in text:
    answer = random.choice(Left_Res)
    speak(answer)
    

