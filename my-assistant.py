import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if (hour>0 and hour<12):
        speak("Good morning prajwal!")
    elif(hour>12 and hour<18):
        speak("Good Afternoon prajwal!")
    else:
        speak("Good Evening prajwal!")

    speak("How may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = 'E:\\english songs'
            songs = os.listdir(music_dir)
            #print(len(songs))
            os.startfile(os.path.join(music_dir,songs[random.randint(1,75)]))

        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strtime}")
            #speak("you can see down")

        elif"how are you" in query:
            speak("I am cool what about you!")

        elif "open discord" in query:
            path = "C:\\Users\\prajw\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe"
            os.startfile(path)
        elif "quit" or "get lost" or "exit" in query:
            break
