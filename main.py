from genericpath import isfile
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3




def speak(text):
    tts = gTTS(text=text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


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


speak("oh, my name is Jarvis")
text = get_audio()

if "name" in text:
    speak("oh, my name is Jarvis")