import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

Listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = Listener.listen(source)  
            command = Listener.recognize_google(voice)  
            command = command.lower()  
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            return command
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        talk("Sorry, my speech service is down.")
        return ""


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %P')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for,10)
        print(info)
        talk(info)  
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('sorry i have boyfriend ')
    else:
        talk('i dont understand but i am going to search it for you')
        pywhatkit.search(command)

# Run Alexa
while True:
 run_alexa()
