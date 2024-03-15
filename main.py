import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

# changing to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  #google api
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # talk(command)
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print("Current time is "+time)
        talk("Current time is " + time)

    elif 'who'  in command:
        person = command.replace('who','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('I have a Boyfriend')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        # print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'send message' in command:
        talk('Whom do you want to send the message to?')
        recipient = take_command()
        talk('What is the message?')
        message = take_command()
        pywhatkit.sendwhatmsg_instantly(recipient, message)  #i have to resolve it
        talk('Message sent.')


    else:
        talk('Please say the command again.')


while True:
    run_alexa()