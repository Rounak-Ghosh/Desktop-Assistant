import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning!")

    elif 12 <= hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("I am your Google Assistant. Please tell me how may I help you ?")


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', '')
            print(command)
    except:
        pass
    return command


def run_google():
    wishMe()
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'created' and 'you' in command:
        talk('I was programmed by Rounak Ghosh.')


run_google()
