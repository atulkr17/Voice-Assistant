import openai
import datetime
import pyttsx3
import os
import speech_recognition as sr
import webbrowser

openai.api_key="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"

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak(f"Good Morning! It's {datetime.datetime.now().strftime('%I:%M %p')}.")
        print(f"Good Morning! It's {datetime.datetime.now().strftime('%I:%M %p')}.")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon! It's {datetime.datetime.now().strftime('%I:%M %p')}.")
        print(f"Good Afternoon! It's {datetime.datetime.now().strftime('%I:%M %p')}.")
    elif hour>18 and hour<19:
        speak(f"Good Evening! It's {datetime.datetime.now().strftime('%I:%M %p')}.")
        print(f"Good Evening! It's {datetime.datetime.now().strftime('%I:%M %p')}.")
    else:
        speak("good night It's {datetime.datetime.now().strftime('%I:%M %p')}.")
        print("good night It's {datetime.datetime.now().strftime('%I:%M %p')}.")


    speak("I am speech recogniser. Please tell me how may I help you")
    print("I am speech recogniser. Please tell me how may I help you")

completion=openai.Completion()

def Reply(question):
    prompt=f'atul: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=100)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hello How Are You? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("atul Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        speak("Say That Again")
        return takeCommand()
    
    return query


if __name__ == '_main_':
    wishMe()
    while True:
        query=takeCommand().lower()
        
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print("time is ", strTime)  
            speak(f"Sir, the time is {strTime}")

        elif 'what is the date' in query:
            now = datetime.datetime.now()
            date_string = now.strftime("%B %d, %Y")
            print("Today's date is:", date_string)
            speak(date_string)  

        elif 'bye' in query:
            speak("have a nice day sir")
            break    

        else:
            ans=Reply(query)
            print(ans)
            speak(ans)
            

