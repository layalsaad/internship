import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def utter(text):
    engine.say(text)
    engine.runAndWait()

def getAudio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening you ...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing ...")
        query = recognizer.recognize_google(audio,language = "en-US")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Sorry, didn't get you.")
        return "None"
    return query

def main():
    utter("Hello! How can I assist you?")
    while True:
        query = getAudio().lower()
        if 'exit' in query:
            speak("Goodbye!")
            break
        if 'your name' in query:
            speak("I am your voice assistant.")
            ## actions to be done according to user request
        else:
            speak("Sorry, I didn't understand that command.")
