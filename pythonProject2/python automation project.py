import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import ssl

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning my dear friend")
    elif 12 <= hour < 18:
        speak("Good afternoon my dear friend")
    else:
        speak("Good Evening my dear friend")
    speak("Let me know how can I help you, what are you looking for?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you sheela......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing your voice......")
        query = r.recognize_google(audio, language='en-in')
        print(f"My dear friend you said: {query}\n")
        return query
    except Exception as e:
        print("Sheela say that again please......")
        return "None"

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'open wikipedia' in query:
             speak('Searching wikipedia.......')
             query=query.replace("wikipedia")
             results=wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)
        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open paint' in query:
            npath ="C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)
        elif 'open Youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open Great learning academy' in query:
            webbrowser.open("https://www.greatlearning.in/academy")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'text me the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"My dear friend, the time is{strTime}")
        elif 'open great learning youtube channel' in query:
            webbrowser.open("https://www.youtube.com/c/GreatLearningOfficial")
        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")
port=465 # for ssl
smtp_server="smtp.gmail.com"
sender_email="varshi141178@gmail.com"#Enter the address
receiver_email="varshithat.ug22.cs@francisxavier.ac.in"#Enter receiver address
password=input(PASSWORD)


