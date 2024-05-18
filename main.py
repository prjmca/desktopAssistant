# conda create -n assistant python-3.8
# conda activate assistant
# pip list
# pip install -r requirements.txt
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',100)
#Speak function

def speak(text):
    """ This function takes the text and return the voice
    Args: text(_type_):string
    """
    engine.say(text)
    engine.runAndWait()

#speak("Hello I am robot, how are you, what are you doing ")

def takeCommand():
    """
    this functon will recognize voice and return text
    """
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Microphone listenig....')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognozing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as ex:
            print("Say that again Please..")
            return "None"
        return query
    
text = takeCommand()
speak(text)